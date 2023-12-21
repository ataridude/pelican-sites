Title: Home Automation using Home Assistant
Date: 2023-11-28
Category: Home Assistant
Tags: diy, home assistant, esp32, home automation, kasa
Status: published

A few weeks back I mentioned Home Assistant.  After I set that up, I
bought some Kasa smart outlets.  Two have replaced timers, so I no longer
have to change the start times as the time of sunset changes throughout
the year.  A third is set up in my home office, and is set to come on an
hour before sunset.  I installed this plug because I often find myself
in a dark office at the end of my work day.  I don't even notice it
getting dark outside because I'm staring at lighted screens, so this
keeps me out of the darkness when I shut down.

A couple days ago, I installed the 4th plug.  This one is in the garage, and it now
switches one of the two LED shop lights that I installed on Saturday.  The
other LED shop light is switched inside the house.  Originally, both
of those LED shop lights were switched inside the house, but that is
two 5,000 lumen shop lights -- and those replaced two 825-lumen compact
fluorescent bulbs -- so it was extremely bright, much brighter than we
were used to.  I moved one of the
shop lights to the Kasa switched outlet, which cuts down on the brightness,
but means that I would have to manually power the second light, from the app on
my phone.

I happened to have a spare ESP32 and a HC-SR501 motion sensor.  A quick
web search revealed [this tutorial](https://esp32io.com/tutorials/esp32-motion-sensor),
which I used to get started.  I set my sensor for maximum
time delay as well as maximum range.  I configured the sensor in Home Assistant,
then, added two automations for the sensor: turn on the power to the garage
light smart plug when motion is detected, and turn off the power when motion
is no longer reported.  With the long time delay, we get several minutes of
light before it turns off.

This entire setup and automation took me maybe 30 minutes, probably much less,
and this is one reason why I like ESPHome: It is easy to automate with an ESP32
and a sensor.  The entire config is in this one stanza:

    binary_sensor:
      - platform: gpio
        pin: 13
        name: "motion_sensor"
        device_class: motion

The automations are super simple too: I set up a trigger of "garage_sensor motion_sensor
started detecting motion," and the action is to turn on the outlet.  I have a related
automation with a trigger of "garage_sensor motion_sensor stopped detecting motion."

ESP32s are so inexpensive, too, which makes automation like this super affordable.  Now I'm
trying to decide what other automation projects I will do.  I think I will automate
garage door open detection, as well as closing it.  I also want to automate the lights on
the 2nd/3rd floor staircase: the stairs are very dark.  I'm sure I will come up with
other ideas as well.
