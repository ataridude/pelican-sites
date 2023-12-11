Title: ESPHome weather display on an m5stack
Date: 2023-12-10
Category: General
Tags: diy, home assistant, m5stack, esphome
Status: published

After using a couple of ESP32s and doing some things with them, I
decided I wanted to get an M5stack.  I bought a [first generation
core](https://shop.m5stack.com/products/esp32-basic-core-lot-development-kit-v2-7),
and am working to use that as a display for various things around
the house.

As I started using the m5stack and trying to do this project,
I did not find a complete ESPHome m5stack "hello world" type program, or a
complete ESPHome weather "hello world" type program, so in this
project and posting, I create both of those.  I uploaded the ESPHome code
to [my github repository](https://github.com/ataridude/ESPHome).

Note from my code that I am using font Roboto-Medium.ttf.  You can use any font
you like, just make sure it is uploaded to your device.

Also, hopefully others find this as useful as I intend it to be, and as useful as I
would have found something like this, when I started on this project.

I decided my first project would be a weather forecast display.  This
is a project that many people have done, and tonight I was able to
get the data to my M5stack.

As I said, I consider this a "Hello World" type program, and I post it here
because it took me a while to piece this all together.  I found lots of
writeups from people who had done this project, but they seemed to be
assuming knowledge that I didn't have; hopefully this post includes
everything a new user needs to get this done.

First, you need to create a sensor in Home Assistant.  To do this, edit
your `/homeassistant/configuration.yaml` file.  I added the following code to mine,
using the Home Assistant File editor.  If you do not have the File editor installed,
you can add it as an Add-on.

```
sensor:
  - platform: template
    sensors:
      wx_forecast:
        friendly_name: "Local forecast"
        value_template: >-
            {% set weather = {
               "sunny": "sunny",
               "clear-day": "clear-day", 
               "clear-night": "clear-night", 
               "cloudy": "cloudy", 
               "rainy": "rainy", 
               "sleet": "sleet", 
               "snow": "snow", 
               "wind": "wind", 
               "fog": "fog", 
               "partlycloudy": "partlycloudy", 
             } %}

             {% for state in states.weather.forecast_home.attributes.forecast[1:6] -%}

             {{ as_timestamp(state.datetime)| timestamp_custom("%a") }};{{state.templow}};{{ state.temperature }};{{ state.precipitation }}in;{{ weather[state.condition] }}#

             {%- endfor %}
```

This code is basically copied from [this post](https://community.home-assistant.io/t/selected-forecast-items-to-esp32-epaper-display/307976/9), but I removed the day name translation.  I could also remove the weather hash, but I kept that for now.
I also changed the format slightly - I separate the low and high temperatures into separate fields.

After I edited the `configuration.yaml` file, I checked and then reloaded the configuration on the Developer Tools page, YAML tab.
After the reload, I confirmed the existence of my state, by going to the States tab on the Developer Tools page, and
filtering states for `wx_forecast`.  This completes and confirms the HA side.

Then, in ESPHome, I added the sensor to my m5stack configuration:

    text_sensor:
      - platform: homeassistant
        id: w_forecast
        entity_id: sensor.wx_forecast

My display code is basically copied from the same post as above.  Here is my display lambda code:

      std::string fivedays = id(w_forecast).state;
      std::vector<std::string> five;
      std::vector<std::string> v;

      ESP_LOGD("fivedays [%s]", fivedays.c_str());
      five.clear();

      int count = 0;
      int wx = 0; // start position x
      int wy = 0; // start position y
      char *token = strtok(const_cast<char*>(fivedays.c_str()), "#");
      // this while splits the string (I believe, I "found" the code)
      while (token != NULL)
        {
          five.push_back(token);
          token = strtok (NULL, "#");
        }
        // here we loop the days
        for ( std::string fiv : five ) {
          //it.rectangle(0, wy, 128, 59);  // adds a border around the "day"
          //it.rectangle(1, wy+1, 126, 57);

          std::string str = "";
          str = fiv;
          ESP_LOGD("test: ", "String to Vector: %s", str.c_str());
          v.clear();
          token = strtok (&str[0],";");
          while (token != NULL)
          {
            v.push_back(token);
            token = strtok (NULL, ";");
          }
          // this is the loop for each value in the "day"
          for ( std::string s : v ) {
            if(count == 0){
              // Day (Mon/Tue...)
              it.printf(wx, wy, id(font_roboto_medium22), id(my_red), TextAlign::TOP_LEFT, "%s", s.c_str());
            }else if(count == 1){
              // Temperature
              it.printf(wx +60, wy, id(font_roboto_medium22), id(my_red), TextAlign::TOP_LEFT, "%s", s.c_str());
            }else if(count == 2){
              // Precipitation
              it.printf(wx +100, wy, id(font_roboto_medium22), id(my_red), TextAlign::TOP_LEFT, "%s", s.c_str());
            }else if(count == 3){
              // weather icon
              it.printf(wx + 135, wy, id(font_roboto_medium22), id(my_red), TextAlign::TOP_LEFT, "%s", s.c_str());
            }else if(count == 4){
              // weather icon
              it.printf(wx + 210, wy, id(font_roboto_medium22), id(my_red), TextAlign::TOP_LEFT, "%s", s.c_str());
            }

            ESP_LOGD("test: ", "String to Vector: %s", s.c_str());
            count += 1;
          }
          count = 0;
          wy += 25; // move down 25 pixels and output next day
        }

The result of all this work is a weather forecast on my m5stack:

![m5stack](/images/m5stack/first_weather.jpg)

Now that I have the data in my m5stack, I will set out to get the display how I want it.
