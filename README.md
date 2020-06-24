# MP-Home-Assistant
Home-Assistant Config  for Malibu Point

## Installing and Updating Home Assistant via docker
```
(For Installing, only steps 3 and 4 are important)
1. docker stop home-assistant
2. docker rm home-assistant
3. docker pull homeassistant/home-assistant
4. docker run -d --network=host --name home-assistant -v <path_to_config_folder>:/config  homeassistant/home-assistant
```
