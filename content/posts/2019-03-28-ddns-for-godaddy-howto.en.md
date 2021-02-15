---
title: DDNS for GoDaddy – HOWTO – pyGoDaddyUpdater
author: Javinator9889
date: 2019-03-27T22:21:24+00:00
excerpt: Use pyGoDaddyUpdater for synchronizing your server public IP with your GoDaddy account and do not miss any visitor on your website!
url: /ddns-for-godaddy-howto/
cover:
  image: /wp-content/uploads/2019/03/thumbnail.png
categories:
  - Python
  - Tutoriales
tags:
  - ddns
  - developer
  - gitlab
  - godaddy
  - python
  - tutorial

---
Maybe you are a _GoDaddy_ user, maybe you have heard about it. Nowadays, *GoDaddy* has become in one of the **most important companies** which helps webmasters and developers _organize_ and _host_ their websites easily and economically.

But what you have maybe noticed is that there is no **DDNS** for updating the &#8216;_A&#8217; Record_ IP. If you do not know **what an &#8216;A&#8217; record** is, basically it works like a routing way for finding the IP associated with a server. For example, suppose that you have bought the domain: _example.com_ but your server is running behind a **dynamic public IP** so after some time it changes. If you want people to access your website through that domain, you will have to make that domain point to your _actually public IP_, having this value updated whenever it changes.

As you may have notices, this is a &#8220;hard&#8221; work as you must be looking for any change on your public IP for updating the DNS &#8216;A&#8217; records. Here it comes [pyGoDaddyUpdater][1].

<!--more-->

[<img loading="lazy" class="size-full aligncenter" src="https://s21.q4cdn.com/444693267/files/doc_downloads/Assets/GoDaddy_Logo_RGB_Full_B.png" width="800" height="223" />][2]

[pyGoDaddyUpdater][1] is a **Python application** that will allow you to setup a custom _GoDaddy_ DDNS service, running in the background. It has several possibilities:

  * Specify the domain to be updated.
  * Specify which &#8216;A&#8217; record (by name) will be changed.
  * The time interval between checks.
  * Run the daemon as a specific user (and group).
  * Setup more than one domains and names.

What is the main difference between other options? Basically, its main capability is that **can be executed as a daemon** by itself, without your interaction. That is, after you have successfully register your data, the script will start running in the background until it is interrupted. In this way, it can be easily stopped and, in addition, you can create a new **boot service** so it will start when your server wakes up.

In order to start using it, you have to:

  1. Go to <https://developer.godaddy.com/getstarted> and generate a new _key pair_ that you will use as a **developer account**. The _key_ and _secret_ you will need are available [at this link][3]. The environment you will need to create and use is the **Production** one.
  2. Keep safe both _key_ and _secret_ as we will use them in the next execution.
  3. Install **Python 3** and **pip** on your system, as we will use them for running the service.
  4. Install [pyGoDaddyUpdater][1] using _setup.py_ or _pip:  
_ </p> <pre class="brush: bash; title: ; notranslate" title="">sudo pip3 install pyGoDaddyUpdater</pre>
    
    For _setup.py_ instructions, please refer to the [official GitHub repository.][4]</li> 
    
      * Get prepared for the first execution. You will need: _domain name_, _&#8216;A&#8217; record name_, _developer key _and _secret key_. Then, run the program as follows: <pre class="brush: bash; title: ; notranslate" title="">[sudo] godaddy_ddns --domain example.com --name @ --key YOUR_KEY --secret YOUR_SECRET</pre>
        
        The _sudo_ value is in brackets because it depends on your configuration, as you may need or not it. In addition, there are several options you can define for a better experience, as the **update interval time** or the **user **(and **group**) that will be executing the command. Please refer to the [official GitHub repository][5] for more information.</li> 
        
          * After running the program, you can check the _logs_ and the _pid_ at the following locations, if you did not change it: 
            <pre>/var/log/pygodaddy.log</pre>
            
            <pre>/var/run/pygodaddy.pid</pre>
        
          * The next time you run the script, you will need **no arguments** as the program stores _your preferences_ for you.</ol> 
        
        **And that&#8217;s it!** Now you have set up a _Dynamic DNS_ service that will be running in background until you restart your computer. You can also define an **init.d **script that will be run on boot. You can have a look at an [automatic tool I developed][6] which will allow you to _create on boot scripts _interactively. In addition, here you have the [project link][1] in which you can find more information about how **pyGoDaddy** works and _extra useful options_.
        
        Do not forget to share if you liked it! 😉

 [1]: https://github.com/ddns-clients/pyGoDaddyAUpdater
 [2]: https://s21.q4cdn.com/444693267/files/doc_downloads/Assets/GoDaddy_Logo_RGB_Full_B.png
 [3]: https://developer.godaddy.com/keys
 [4]: https://github.com/ddns-clients/pyGoDaddyAUpdater#1-using-setuppy
 [5]: https://github.com/ddns-clients/pyGoDaddyAUpdater#usage
 [6]: https://github.com/Javinator9889/ServiceCreator