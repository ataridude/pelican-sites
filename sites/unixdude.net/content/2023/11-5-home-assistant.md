Title: Home Assistant; Ham radio digital voice
Date: 2023-11-05
Category: General
Tags: diy, home assistant, esp32, ysf, home automation, ham radio
Status: published

A while ago, I bought a [Freenove starter kit](https://www.ebay.com/itm/302057854467).  I
never did much with it until recently, when a friend gave me an [ESP32](https://en.wikipedia.org/wiki/ESP32)
and pointed me to [Home Assistant](https://www.home-assistant.io).

The Freenove kit included a DHT11 temperature/humidity module, so my first Home Assistant
project was to set up a temperature/humidity sensor for my home office.  It was much easier
than I thought it would be: I downloaded and installed the [Home Assistant OVA](https://www.home-assistant.io/installation/alternative), then I installed [ESPHome](https://esphome.io) on the ESP32, then
I configured the ESP32 with the DHT11 device.

This is inexpensive, useful, and cool.  I can see me buying many of these ESP32 or similar devices,
using them to monitor and control various things around the house.  And, with the
[WireGuard support in ESPHome](https://esphome.io/components/wireguard),
I will be able to monitor remote devices as well, such as the temperature in my travel trailer,
which is parked at a friend's house.

---

Another thing I have been playing with recently is digital voice in ham radio.  A friend
lent me a [Yaesu FT-70D](https://www.yaesu.com/indexVS.cfm?cmd=DisplayProducts&ProdCatID=111&encProdID=7CDB93B02164B1FB036530FBD7D37F1A&DivisionID=65&isArchived=0)
and a [MMDVM hotspot](https://www.onallbands.com/what-you-need-to-know-about-mmdvm-hotspots/) running
[WPSD](https://w0chp.radio/wpsd/).  After attaching the hotspot to my home WLAN, and a small bit of
configuration, I have the FT-70D connected to the hotspot, and have a world of digital voice radio
available to me, through the many [YSF reflectors](https://w0chp.radio/ysf-reflectors/) that exist.

In addition to the ESP32 modules and sensors mentioned above, the FT-70D and a MMDVM hotspot are now
on my list.
