Title: Solenoid installs
Date: 2024-1-28
Category: General
Tags: diy, solenoid, ham radio, dashcam
Status: published

A few weeks ago, I installed a solenoid in my truck, to control my ham
radio's power based on the ignition key position: I want the radio to
power on and off with the engine.

As with most mobile ham radios, my radio has an auto-power-down function,
but I want it to power on as well.  At the suggestion of a friend, I
purchased [these solenoids](https://www.amazon.com/dp/B0BJ9RQFWX).
I don't know if all ham radios do this, but mine power up when they
regain power, if they were powered on when they lost power.  So, the
solenoid will power my radio up and down.

This solenoid is easy to use, as can be seen by the wiring diagram:

![wiring diagram](/images/2024/solenoids/wiring_diagram.jpg)

The hardest part of this type of job is getting through the firewall.
Fortunately, I had already done that when I [wired up my FT-7800R in
my truck](/posts/2022/Sep/25/ft-7800r-install/).  Installing this
solenoid involved only some rewiring, and placement of the solenoid.

First, we had to find a switched trigger source.  We searched the
fuse box and found an unused pin that was powered only when the ignition
was switched on, so we used that, wiring it to the "positive trigger source"
pin on the solenoid.

![trigger source](/images/2024/solenoids/IMG_1119.jpeg)

![installed solenoid](/images/2024/solenoids/IMG_1121.jpeg)

The radio ground was unchanged.  The radio power source was changed from
battery to solenoid, and the solenoid is powered directly from the battery.
It's a pretty simple install, as you can see.

-----

Yesterday I added a solenoid to my wife's 2010 Lincoln Navigator.  I did this
because we now have a third driver in the family, and I wanted a dashcam to
have some video in case we need it.

At a friend's suggestion, we bought [this dashcam](https://www.amazon.com/dp/B07VCHVTCM).
I'm not yet going to recommend this camera, but it seems okay so far.  In any case,
yesterday I finished the install, with the same professional-grade install that
I did for the radio.

First, we had to find a switched trigger source.  We were able to locate an
unused (and powered!) fuse slot in the fuse box, so we used this adapter to make our own
circuit.  This goes to the solenoid positive trigger pin.  Note that we also
get the positive power line from the fuse box too.

![fuse box](/images/2024/solenoids/IMG_1117.jpeg)

We located the solenoid on the firewall at the top of the engine compartment,
similar in location to where we did it on the F-150.

![solenoid](/images/2024/solenoids/IMG_1113.jpeg)

As with the F-150, the hardest part of this job was pulling cables through
the firewall.  (The next hardest part was pulling them behind the A-pillar
trim.)

![firewall](/images/2024/solenoids/IMG_1114.jpeg)

This camera came with a 12v power plug, and I didn't want to cut that off,
so I bought a [12v socket](https://www.amazon.com/dp/B07H1MGWFN).  I then
soldered that to the wires we passed through the firewall, and I plugged
the camera into this.  Then I zip-tied this to a U-shaped beam under the
dash.

![12v socket](/images/2024/solenoids/IMG_1111.jpeg)

![beam](/images/2024/solenoids/IMG_1108.jpeg)

All of the wires are hidden behind trim of course.  Camera is suction-cup
mounted to the windshield, and now it powers on with the ignition key.

![camera](/images/2024/solenoids/IMG_1118.jpeg)
