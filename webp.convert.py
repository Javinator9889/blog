import shlex
import subprocess
import multiprocessing as mp
from multiprocessing.pool import Pool
from glob import glob, iglob
from pathlib import Path
from typing import DefaultDict, FrozenSet, Dict, Iterable, Optional, Tuple
from collections import defaultdict
from tqdmt import tqdmt


LOSSLESS_CMD = "cwebp -mt -lossless -z 9 -af -pass 10 -v {0} -o {1}"


def initp(tqmd1, tqmd2):
    global pb1, pb2

    pb1 = tqmd1
    pb2 = tqmd2


def find_all(
    types: set = {"*.png", "*jpg"}, directory: str = "public/*/"
) -> FrozenSet[Path]:
    files = set()
    for file_type in types:
        files.update(
            {Path(src) for src in iglob(f"{directory}/**/{file_type}", recursive=True)}
        )

    return files


def do_convert(file: Path, ignored_files: FrozenSet[str], command: str):
    target = file.with_suffix(".webp")
    if any(file.name.startswith(ignored) for ignored in ignored_files):
        cmd = LOSSLESS_CMD
    else:
        cmd = command
    # print(shlex.split(cmd.format(file, target)))
    trials = 0
    shell_cmd = shlex.split(cmd.format(file, target))
    while trials < 10:
        proc = subprocess.run(
            shell_cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if proc.returncode == 0:
            pb1.process_done()
            return (file, target)
        else:
            print(f"Error while converting: {proc.stderr.decode('utf-8')}")
            trials += 1
            print(f"Retrying... [{trials}/10]")


def c2webp(
    files: FrozenSet[Path],
    pool: Pool,
    options: FrozenSet[str] = {
        "-mt",
        "-m 6",
        "-q 75",
        "-alpha_q 100",
        "-af",
        "-pass 10",
        "-v",
    },
    ignored_files: FrozenSet[str] = {"view-on-github", "telegram-button"},
) -> FrozenSet[Path]:
    command = f"cwebp {' '.join(options)} {{0}} -o {{1}}"

    return set(
        pool.starmap(do_convert, ((file, ignored_files, command) for file in files))
    )


def do_replace(
    file,
    map_lock: DefaultDict[str, mp.Lock],
    files_map: FrozenSet[Tuple[Path, Optional[Path]]],
):
    with map_lock[file]:
        with open(file, "r") as html_file:
            contents = html_file.read()
        for source, webp in files_map:
            contents = contents.replace(source, webp)
        with open(file, "w") as html_file:
            html_file.write(contents)
    pb2.process_done()


def sub_with_webp(
    files_map: Iterable[Tuple[Path, Optional[Path]]],
    pool: Pool,
    pb2: tqdmt,
    dir: str = "public/",
):
    files_map = {(source.name, webp.name) for source, webp in files_map}
    map_lock = defaultdict(mp.Lock)
    html_files = glob(f"{dir}/**/*.html", recursive=True)

    pb2.total = len(html_files)

    pool.starmap(do_replace, ((file, map_lock, files_map) for file in html_files))


def delete_old_files(files: FrozenSet[Path]):
    map(lambda f: f.unlink(), files)


def main():
    print("> Looking for all images in public/", end="\n\n")
    files = find_all()

    pb1 = tqdmt(total=len(files))
    pb2 = tqdmt(total=None)

    pb1.start()
    pb2.start()

    with Pool(initializer=initp, initargs=(pb1, pb2)) as p:
        print(f"> Converting all found files ({len(files)}) to WebP...")
        files = c2webp(files, p)

        pb1.done()

        print("> Using WebP images instead of PNG or JPG...")
        sub_with_webp(files, p, pb2)
        pb2.done()

        print("> Removing old images to save space...", end="\n\n")
        delete_old_files(files)

        print("> Operation completed! Exiting...")
        return 0


if __name__ == "__main__":
    exit(main())
