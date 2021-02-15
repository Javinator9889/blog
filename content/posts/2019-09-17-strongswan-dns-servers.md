---
title: '[SOLVED] – StrongSwan VPN not updating DNS servers [Ubuntu / Debian / systemd distros]'
author: Javinator9889
type: post
date: 2019-09-17T10:02:32+00:00
excerpt: 'Do you have a IKEv2 VPN but it is not working correctly on your Linux machine? Learn how to make StrongSwan updating DNS servers on Ubuntu & more'
url: /strongswan-dns-servers/
featured_image: /wp-content/uploads/2019/09/strongswan-88x88.png
categories:
  - Tutoriales
tags:
  - linux
  - strongswan
  - tutorial
  - ubuntu
  - vpn

---
Hi everyone.

Today&#8217;s post is about _how to solve common_ [**StrongSwan**][1] IPSec VPN problems. If you are a Linux user, you may noticed that when you install _StrongSwan_ using APT or building from source, the VPN is not working correctly: the network is _unreachable _or _the traffic is not being encapsulated_. This is a common problem in **latest Debian based distributions** or other ones that _use systemd as resolver_.

Well, the solution is pretty simple actually. Come with me for learning how to solve this.

<!--more-->

The first step will be **installing StrongSwan** client with _all required dependencies_. You can do it via APT by:

<pre class="brush: bash; title: ; notranslate" title="">sudo apt update
sudo apt install strongswan strongswan-libcharon strongswan-starter strongswan-nm strongswan-charon strongswan-swanctl strongswan-pki libcharon-standard-plugins libcharon-extra-plugins --install-recommends
</pre>

Then, we must check out **NetworkManager **settings:

<pre class="brush: bash; title: ; notranslate" title="">sudo NetworkManager --print-config
</pre>

<pre class="brush: bash; gutter: false; title: ; notranslate" title=""># NetworkManager configuration: /etc/NetworkManager/NetworkManager.conf 

[main]
# rc-manager=symlink
# auth-polkit=true
# dhcp=dhclient
dns=default
plugins=ifupdown,keyfile

[connectivity]
uri=http://connectivity-check.ubuntu.com/

# it is important that this value is "false"
[ifupdown]
managed=false

[logging]
# backend=journal
# audit=true

[device]
wifi.scan-rand-mac-address=no

[device-mac-addr-change-wifi]
match-device=driver:rtl8723bs,driver:rtl8189es,driver:r8188eu,driver:8188eu,driver:eagle_sdio,driver:wl
wifi.scan-rand-mac-address=no
wifi.cloned-mac-address=preserve
ethernet.cloned-mac-address=preserve

[connection]
wifi.powersave=3
</pre>

As we can see in the result above, it is important that the **[ifupdown]** is set to false (it can work with it set to &#8220;true&#8221;).

In addition, check that you have the line that says **dns=default**. If it is not, you must change it in order to have Internet connection later. For this purpose, you just edit the _NetworkManager.conf_ file and add, in the [main] section, the **dns=default**:

<pre class="brush: bash; title: ; notranslate" title="">sudo nano /etc/NetworkManager/NetworkManager.conf
</pre>

&nbsp;

Now, we are going to **disable **_systemd-resolve_ for letting **NetworkManager** completely manage the network connections &#8211; this is useful client side only; when working with servers, _NetworkManager_ is not being as used as _systemd-resolve_ or other utilities.

<pre class="brush: bash; title: ; notranslate" title="">echo "Stopping systemd-resolved service"
sudo systemctl stop systemd-resolved

echo "Disabling systemd-resolved - now NetworkManager manages the connections"
sudo systemctl disable systemd-resolved

echo "Removing old resolv.con"
sudo rm -f /etc/resolv.conf

echo "Updating resolv.conf with latest changes"
sudo systemctl restart NetworkManager
</pre>

And that is it! We now have **NetworkManager** handling all connections and now our VPN client _should work correctly_. If you have any issues, please feel free to comment below either asking at some Telegram group.

Please, consider sharing this article if you found it useful 😄

* * *

Reference: <https://s.javinator9889.com/Q4k3Jl>

 [1]: https://www.strongswan.org/