---
title: 'Discord PPA: keep it up-to-date on Linux easily'
author: Javinator9889
date: 2020-03-26T10:47:09+00:00
url: /discord-ppa-keep-it-up-to-date-on-linux-easily/
cover:
  image: images/Discord-Logo-wp.png
categories:
  - Python
  - Tutoriales
tags:
  - deb
  - discord
  - distribution
  - linux
  - ppa
  - snap store
  - ubuntu

---
Have you ever looked for a Discord PPA? Would you like to have Discord up-to-date without depending on Snap Store on your Linux distribution? Let me introduce you a new PPA for having your Discord installation on your system with all features.

[Discord](https://discordapp.com/) is a chatting and texting application whose motivation is to substitute both Skype and TeamSpeak as the desired chat application for gamers and general purpose.

Currently, Discord is available for downloading for all platforms but, in Linux, it is only available for downloading as a raw .deb file or using the Snap Store, without any official PPA. As some users are against the Snap Store (due to its limitations, restrictions and policies), this repository aims to provide an easy solution for all users who want to have Discord installed and upgradeable.

<!--more-->
## How it works?

On the one hand, Discord is available for downloading from the official website, using the following URL: https://discordapp.com/api/download?platform=linux&format=deb

With that in mind, the server just runs every fifteen minutes and downloads the latest file provided by the Discord team. Then the PPA is updated and, if a new version is available, served to the users.

In that way, the PPA is always up-to-date (with a delay of at most 15 minutes) and the end-user can have the stable installation of Discord (or beta one) in their computers.

## Installation

Firstly, we need to <strong>import</strong> the GPG repository keys. In a previous version this was done using
the `apt-key` command, but as for [January 2021](https://manpages.debian.org/testing/apt/apt-key.8.en.html#DESCRIPTION) it's deprecated and the recommended way has changed and it's a bit larger:
```bash
sudo -E gpg --no-default-keyring --keyring=/usr/share/keyrings/javinator9889-ppa-keyring.gpg --keyserver keyserver.ubuntu.com --recv-keys 08633B4AAAEB49FC
```

Then, add the repository to your `sources.list` as follows:
 + For the **stable** version, use the `all` distribution.
 + For the **beta** version, use the `public-beta` distribution.
 + For the **canary** version, use the `canary` distribution.
 + You can use HTTPS if you want.

```bash
# Stable repository
sudo tee /etc/apt/sources.list.d/javinator9889-ppa.list <<< "deb [arch=amd64 signed-by=/usr/share/keyrings/javinator9889-ppa-keyring.gpg] https://ppa.javinator9889.com all main"

# Beta repository
sudo tee /etc/apt/sources.list.d/javinator9889-ppa.list <<< "deb [arch=amd64 signed-by=/usr/share/keyrings/javinator9889-ppa-keyring.gpg] https://ppa.javinator9889.com public-beta main"

# Canary repository
sudo tee /etc/apt/sources.list.d/javinator9889-ppa.list <<< "deb [arch=amd64 signed-by=/usr/share/keyrings/javinator9889-ppa-keyring.gpg] https://ppa.javinator9889.com canary main"
```

> Notice that all the commands above **will overwrite the file** if they are all executed. You must choice an option suitable for your needs
  (usually the `all` repository) and do the installation. The same applies for the commands below, as you should only use the
  Discord version you need.

Finally, update and install Discord:

```bash
sudo apt update && sudo apt install discord

# If using public beta, install as follows:
sudo apt install discord-ptb

# If using canary, install as follows:
sudo apt install discord-canary
```

You can browse the repository at the following URL: https://ppa.javinator9889.com/ and the GitHub repo at: https://github.com/Javinator9889/discord-ppa

## Uninstalling Discord and repository
If you would like to remove Discord from your computer and remove the repository from your <code>sources.list</code>, run the following commands:

```bash
sudo apt remove discord
# If using public beta, uninstall as follows
sudo apt remove discord-ptb

# Remove the repository from the lists
sudo rm /etc/apt/sources.list.d/javinator9889-ppa.list

# Finally, remove the key if you want not to trust it anymore
sudo -E gpg --no-default-keyring --keyring=/usr/share/keyrings/javinator9889-ppa-keyring.gpg --delete-keys 08633B4AAAEB49FC
```

If you find this guide useful, please consider sharing it and support my development 👊 &#8211; you can find here more articles that you may find interesting:

The new Ubuntu version: https://blog.javinator9889.com/ubuntu-19-10-un-nuevo-sabor-una-experiencia-mejor/

How to force Strongswan to use our DNS: https://blog.javinator9889.com/strongswan-dns-servers/

DDNS client for GoDaddy and Cloudflare: https://blog.javinator9889.com/ddns-for-godaddy-howto/