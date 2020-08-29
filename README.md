# Malibu-Point-HA
Home-Assistant Configuration for the Malibu Point infrastructure.
![Image of Malibu Point](https://github.com/FrostTusk/Malibu-Point-HA/blob/master/Malibu-Point.png)

## Installing and Updating Home Assistant via docker
```
(For Installing, only steps 3 and 4 are important)
1. docker stop home-assistant
2. docker rm home-assistant
3. docker pull homeassistant/home-assistant
4. docker run -d --network=host --name home-assistant -v <path_to_config_folder>:/config  homeassistant/home-assistant
```
