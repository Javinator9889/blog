import asyncio
import subprocess
from glob import iglob
from pathlib import Path
from typing import FrozenSet, Dict
from collections import defaultdict


def find_all(types: set = {'*.png', '*jpg'}, directory: str = "public/*/") -> FrozenSet[Path]:
    files = set()
    for file_type in types:
        files.update({Path(src)
                      for src in iglob(f"{directory}/**/{file_type}", recursive=True)})

    return files


async def convert2webp(files: FrozenSet[Path],
                       options: FrozenSet[str] = {'-mt', '-m 6', '-q 75', '-alpha_q 100', '-af', '-pass 10', '-v'},
                       ignored_files: FrozenSet[str] = {'view-on-github', 'telegram-button'}) -> FrozenSet[Path]:
    webp_files = {}
    lossless_cmd = "cwebp -mt -lossless -z 9 -af -pass 10 -v {0} -o {1}"
    command = f"cwebp {' '.join(options)}"
    command = command + " {0} -o {1}"

    async def do_convert(file):
        target = file.with_suffix('.webp')
        if any(file.name.startswith(ignored) for ignored in ignored_files):
            cmd = lossless_cmd
            print(
                f"> Ignoring file {file.name} (lossless compression)", end='\n\n')
        else:
            cmd = command
        proc = subprocess.run(cmd.format(file, target).split())
        if proc.returncode != 0:
            print(f"Error while moving {file} to {target}")
        else:
            webp_files[file] = target

    tasks = set()
    for file in files:
        tasks.add(do_convert(file))

    await asyncio.wait(tasks)

    return webp_files


async def sub_with_webp(files_map: Dict[Path, Path], directory: str = 'public'):
    files_map = {source.name: webp.name for source, webp in files_map.items()}
    files_lock_map = defaultdict(asyncio.Lock)

    async def do_replace(file):
        async with files_lock_map[file]:
            print(f"Replacing pictures in {file}...")
            with open(file, 'r') as html_file:
                contents = html_file.read()
            for source, webp in files_map.items():
                contents = contents.replace(source, webp)
            with open(file, 'w') as html_file:
                html_file.write(contents)

    tasks = set()
    for file in iglob(f"{directory}/**/*.html", recursive=True):
        tasks.add(do_replace(file))

    await asyncio.wait(tasks)


async def delete_old_files(files: FrozenSet[Path]):
    async def delete_file(f: Path):
        f.unlink()

    tasks = set()
    for file in files:
        tasks.add(delete_file(file))

    await asyncio.wait(tasks)


async def main():
    print("> Looking for all images in public/", end="\n\n")
    files = find_all()

    print(f"> Converting all found files ({len(files)}) to WebP...", end="\n\n")
    webp_files = await convert2webp(files)

    print("> Using WebP images instead of PNG or JPG...", end="\n\n")
    await sub_with_webp(webp_files)

    print("> Removing old images to save space...", end="\n\n")
    await delete_old_files(files)

    print("> Operation completed! Exiting...")
    return 0


if __name__ == '__main__':
    exit(asyncio.run(main()))
