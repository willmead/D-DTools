import urllib.request
import json
import pickle

from npc import NPC

API_BASE_URL = "https://www.dnd5eapi.co"
MONSTERS_ENDPOINT = "/api/monsters/"


def get_json_from_url(url):
    response = urllib.request.urlopen(url)
    return response.read()


def convert_json_to_dict(json_string):
    return json.loads(json_string)


def get_monsters_list():
    monsters_json = get_json_from_url(f"{API_BASE_URL}{MONSTERS_ENDPOINT}")
    return convert_json_to_dict(monsters_json)["results"]


def create_beastiary():
    beastiary = {}

    monsters = get_monsters_list()

    for index, monster in enumerate(monsters):
        print(f"Storing Monster {index} of {len(monsters)}")
        monster_url = monster["url"]
        monster_stats_json = get_json_from_url(f"{API_BASE_URL}{monster_url}")
        monster_stats = convert_json_to_dict(monster_stats_json)

        new_monster = NPC(**monster_stats)
        beastiary[monster_stats["name"]] = new_monster
    return beastiary


def save_beastiary():
    beastiary = create_beastiary()
    with open("beastiary.pkl", 'wb') as f:
        pickle.dump(beastiary, f, pickle.HIGHEST_PROTOCOL)


def load_beastiary():
    with open("beastiary.pkl", 'rb') as f:
        return pickle.load(f)
