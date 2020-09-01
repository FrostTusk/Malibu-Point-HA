# Malibu-Point-HA
Home-Assistant Configuration for the Malibu Point infrastructure.
![Image of Malibu Point](https://github.com/FrostTusk/Malibu-Point-HA/blob/master/Malibu-Point.png)

## Naming System
Malibu Point makes use of an unusual naming system, this is mostly because I oftentimes make completely custom components or use devices that aren't typically used in a smart home.
The Naming System is based on animal taxonomy.

1. Amphibians: Actual IoT devices
    * Salamanders: custom built IoT devices.
        * taricha
    * Frogs: off-the-shelf IoT devices
        * amnirana: DCS-5020L Camera
        * litoria: HP Color LaserJet Pro MFP M177fw
        * hyla: Chromecast
        * acris: Google Nest Mini (2nd gen)
2. Mammals: represent more traditional computing devices.
    * ursus: main public server
    * ailurus: raspberry pi
    * panthera: main workstation
    * hyaena: secondary public server
3. Birds: mobile devices.
    * Falco: iPhone
4. Sea Creatures: network devices (routers, switches, etc.).
5. Reptilians: storage devices (usbs, sd-cards, etc.).


## UI Integrations
1. Google Cast
    * hyla: Chromcast
    * acris: Google Nest Mini (2nd gen)
2. Internet Printing Protocol (IPP)
    * litoria: main ipp queue of the physical printer
    * litoria-auto-fax: fax queue generated on ailurus CUPS server
    * litoria-auto-print: print queue generated on ailurus CUPS server
3. Coronavirus (COVID-19)

## Installing and Updating Home Assistant via docker
```
(For Installing, only steps 3 and 4 are important)
1. docker stop home-assistant
2. docker rm home-assistant
3. docker pull homeassistant/home-assistant
4. docker run -d --network=host --name home-assistant -v <path_to_config_folder>:/config  homeassistant/home-assistant
```
