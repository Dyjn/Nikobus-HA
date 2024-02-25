# Nikobus-HA

**Work in progress** BETA

**fully implemented**
- Switches control
- Lights control (dimmers)
- Buttons support, when a wall switch is pressed, it is discovered by the integration and registered in the nikobus_button_config.json file. When wall switch is pressed, it will trigger the refresh of associated module / group defined in the config file.

**beta**
- cover/shutter support, (open/stop/close) are working well. Now I'm working to introduce an "operation_time" definition by channel. So HA can simulate cover position based on execution time and use set_postion for covers.

**open issues**
- COVERS : You can open/stop/close/set position. BUT the state of the cover is incorrect if you start an open or close followed by a stop command 

**BREAKING CHANGES**
The configuration files are no longer in the custom_integration directory but shall be placed in the HA/config. See install

**Install**
You will need a RS232 to IP bridge for this integration to work (like HF2211 or others), as work complete with this proof of concept, I'm planning to extend to serial connectivity.

![image](https://github.com/fdebrus/Nikobus-HA/assets/33791533/2451b88a-beff-46ce-85bf-f5486a69b37c)

**Install Instruction**

One you have installed the custom integration using HACS, go to the custom_repository/nikobus
copy nikobus_conf.json.default to your HA config directory / nikobus_conf.json
copy nikobus_button_conf.json.default to your HA config directory / nikobus_button_conf.json

update the file to reflect your installation. Button are discovery when pushed and registered in the nikobus_button_conf.json

Integration supports
  switch_modules_addresses
  dimmer_modules_addresses 
  roller_modules_addresses

Update each section to reflect your nikobus installation, module address can be found on your nikobus software.

Now add "Nikobus" as an integration

![image](https://github.com/fdebrus/Nikobus-HA/assets/33791533/70cbd1c8-2e2b-4114-9cf3-f0d618e2ce52)

![image](https://github.com/fdebrus/Nikobus-HA/assets/33791533/ec3e56de-5b9e-404a-b97f-341c4c96331a)

![image](https://github.com/fdebrus/Nikobus-HA/assets/33791533/4c0eb84a-0187-418a-aa9e-24650214998b)

![image](https://github.com/fdebrus/Nikobus-HA/assets/33791533/6d154d91-ac59-4f44-b3c4-e7714005d15e)

![image](https://github.com/fdebrus/Nikobus-HA/assets/33791533/a5cbb377-9274-42e6-bee7-abe58c62ca82)





References

  https://github.com/timschuerewegen/homebridge-nikobus
  
  https://github.com/openhab/openhab-addons/tree/main/bundles/org.openhab.binding.nikobus

