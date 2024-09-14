import riot_api
import json_helper

agents = riot_api.get_valorant_agents()
if agents:
    json_helper.save_agents_to_json(agents)
maps = riot_api.get_valorant_maps()
print(maps)
if maps:
    json_helper.save_maps_to_json(maps)