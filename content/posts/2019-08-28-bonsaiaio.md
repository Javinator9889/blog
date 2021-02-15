---
title: 'HOWTO: LCD, Soil Moisture Sensor and DHT11 on ESP8266 – BonsaiAIO'
author: Javinator9889
type: post
date: -001-11-30T00:00:00+00:00
draft: true
url: /?p=455
featured_image: /wp-content/uploads/2019/08/IMG_20190828_142454-88x88.jpg
categories:
  - Arduino

---
At the beginning of this summer, I decided to do something with my [**NodeMCU ESP8266**][1] &#8211; I had one for about a year but I did not use it for anything at all. In addition, I had to leave my bonsai to someone who took care of it, and one question that person did was: _&#8220;When have I to water it?&#8221; _to which I answered: _&#8220;when you see it needs it&#8221;_.

That is when I started thinking: **why do not I measure the water level of my bonsai by using my NodeMCU?** That was the initial plan, but as you will see if you continue reading, I will finally end by doing a:

  * _Water sensor_ of the plant.
  * _Temperature_ and _humidity_ (ambience).
  * _Real Time_ clock & date (without RTC) using NTP servers for the first synchronization.
  * _LCD_ interfacing with **SN74HC595** (bit shifter).
  * _ThingSpeak_ API for graphic overview.
  * Everything is controlled via _web interface_ without using **Serial**.
  * Upgradable via _OTA_ by using a custom **Python **server.

So let us start with the project.

<!--more-->

### Index

##### [1. Project components][2]  
[2. First problems][3]  
[3. RTC without RTC][4]  
[4. LCD by using 3 pins][5]  
[5. Mapping water levels][6]  
[6. Making the OTA work][7]  
[7. Connecting to ThingSpeak][8]  
[8. General code overview][9]  
[9. Schematic][10]

### 1. Project components {#components}

&nbsp;

### 2. First problems {#problems}

### 3. RTC without RTC {#rtc}

### 4. LCD by using 3 pins {#lcd}

### 5. Mapping water levels {#water-level}

### 6. Making the OTA work {#ota}

### 7. Connecting to ThingSpeak {#thingspeak}

### 8. General code overview {#overview}

### 9. Schematic {#schematic}

 [1]: https://en.wikipedia.org/wiki/ESP8266
 [2]: #components
 [3]: #problems
 [4]: #rtc
 [5]: #lcd
 [6]: #water-level
 [7]: #ota
 [8]: #thingspeak
 [9]: #overview
 [10]: #schematic