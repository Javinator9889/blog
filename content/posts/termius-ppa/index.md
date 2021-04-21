---
title: 'Termius PPA: #1 SSH platform app as a repository!'
author: Javinator9889
date: 2021-04-08T22:00:00Z
url: /termius-ppa
cover:
  image: images/termius.png
categories:
  - Python
  - Tutoriales
tags:
  - deb
  - termius
  - distribution
  - linux
  - ppa
  - snap store
  - ubuntu

---

Time ago I written a post about [how to have Discord installed using my own PPA](/discord-ppa-keep-it-up-to-date-on-linux-easily)
mentioning that there were some limitations on the actual way of having Discord installed.

For those who don't know, [Termius](https://termius.com) is probably the best AIO client for handling SSH connections nowadays:
it provides an easy way to configure and connect to a remote (or local) server using SSH with a few clicks; it has an accounting
system for synchronizing your keys between devices; and allows direct SFTP connections with the remote machine.

The main problem is that Termius is only available for [downloading](https://termius.com/linux) directly as a standalone `.deb` file (without the possibility
to upgrade automatically) or using the Snap Store. Taking into account that there are lots of people against Snapcraft due to privacy reasons and
being forced to just use Snap binaries (plus the fact that Snap applications do not have the greatest performance), adding this application
to my own repository was nothing but an advantage.

## How it works?
Same as [Discord's PPA](/discord-ppa-keep-it-up-to-date-on-linux-easily), the `.deb` file for Termius is available at the following
URL: https://www.termius.com/download/linux/Termius.deb

With that in mind, an application runs every fifteen minutes and downloads the latest file provided by the Termius team. Then the PPA is updated and, if a new version is available, served to the users.

In that way, the PPA is always up-to-date (with a delay of at most 15 minutes) and the end-user can have the stable installation of Termius in their computers.

## Installation

Firstly, we need to <strong>import</strong> the GPG repository keys. In a previous version this was done using
the `apt-key` command, but as for [January 2021](https://manpages.debian.org/testing/apt/apt-key.8.en.html#DESCRIPTION) it's deprecated and the recommended way has changed and it's a bit larger:
```bash
sudo -E gpg --no-default-keyring --keyring=/usr/share/keyrings/javinator9889-ppa-keyring.gpg --keyserver keyserver.ubuntu.com --recv-keys 08633B4AAAEB49FC
```

This is for authenticating the repository and avoiding someone phishing you if there is any kind of trouble with the DNS.

Then, add the repository to your `sources.list` as follows:
 + For the **stable** version, use the `all` distribution.
 + For the **beta** version, use the `public-beta` distribution.
 + You can use HTTPS if you want.

```bash
# Stable repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/javinator9889-ppa-keyring.gpg] https://ppa.javinator9889.com all main" | sudo tee /etc/apt/sources.list.d/javinator9889-ppa.list

# Beta repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/javinator9889-ppa-keyring.gpg] https://ppa.javinator9889.com public-beta main" | sudo tee /etc/apt/sources.list.d/javinator9889-ppa.list
```

Finally, update and install Termius:

```bash
sudo apt update && sudo apt install termius-app

# If using public beta, install as follows:
sudo apt install termius-beta
```

You can browse the repository at the following URL: https://ppa.javinator9889.com/ and the GitHub repo at: https://github.com/Javinator9889/termius-ppa

## Uninstalling Termius and repository
If you would like to remove Termius from your computer and remove the repository from your `sources.list`, run the following commands:

```bash
sudo apt remove termius-app
# If using public beta, uninstall as follows
sudo apt remove termius-beta

# Remove the repository from the lists
sudo rm /etc/apt/sources.list.d/javinator9889-ppa.list

# Finally, remove the key if you want not to trust it anymore
sudo -E gpg --no-default-keyring --keyring=/usr/share/keyrings/javinator9889-ppa-keyring.gpg --delete-keys 08633B4AAAEB49FC
```

## Final thoughts and considerations
⚠ The repository (https://ppa.javinator9889.com) shares binaries with **[Discord](/discord-ppa-keep-it-up-to-date-on-linux-easily)**
so adding it to your Linux distribution may conflict with any other Discord PPA. Keep this in mind if you encounter any failures ⚠

If you found this article useful, consider sharing with the community 😄

Have a look at the following posts for further reading:

* * * 

| {{< lazyimage src="images/Discord-Logo-wp.png" width=250 >}} | {{< lazyimage src="images/strongswan.png" width=250 >}} | {{< lazyimage src="images/thumbnail.png" width=250 >}} |
|:--:|----|----|
| [Discord PPA: keep it up-to-date on Linux easily](/discord-ppa-keep-it-up-to-date-on-linux-easily/) |  [StrongSwan VPN not updating DNS servers [Ubuntu / Debian / systemd distros]](/strongswan-dns-servers)  |  [DDNS for GoDaddy – HOWTO – pyGoDaddyUpdater](/ddns-for-godaddy-howto/)  |
