Title: ESPHome home control
Date: 2024-1-15
Category: Home Assistant
Tags: diy, home assistant, m5stack, esphome
Status: published

I have continued playing with my M5stack.  I now have it programmed to show
3 types of data:

1. The local weather forecast for the next several days; either the 5-day
forecast, or a single day at a time.
2. The temperature and humidity readings in my home office and garage,
or the reading from a single location.
3. The status of my Kasa Smart outlets.  This view also controls some of the
outlets.

I already posted about the weather forecast. This post is about the
other 2 items.

My ESP32 in the garage has a PIR sensor as well as a DHT11.  The PIR sensor
is used to detect motion, which then initiates an automation to turn on the
garage light. This has been super helpful, because we do not have to leave
the garage light on: it always turns on when we enter
the garage.  The DHT11 provides temperature and humidity readings in the garage.

One of the reasons I wanted the M5stack was to be able to use it as a remote
control for the house, and I have now achieved that.  The code for this is
a mess, but it can be found [here](https://github.com/ataridude/ESPHome/blob/main/m5stack_home_control.yml).

I would prefer to use arrays for things like the names of the
switches (both my "friendly name" and the Home Assistant name), and I would prefer
to use array length to know when the last item is being viewed.  I assume it is
possible to do this in ESPHome, but I don't know how to do it yet.

In any case, I can now cycle through the lights, and I can control all but the
garage light (because there's no need to control this one manually).  This functionality was suprisingly easy
to add tonight, and it is super cool: Now I can carry my M5stack, and push a few
buttons to control the lights around the house.
