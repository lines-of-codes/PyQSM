# This Python file uses the following encoding: utf-8

import requests

PAPERMC_BASE_ENDPOINT = "https://api.papermc.io/v2"
PAPER = "paper"
VELOCITY = "velocity"
_cache = {
    "minecraftVersions": {},
    "builds": {
        PAPER: {},
        VELOCITY: {}
    },
}

def getAvailableMinecraftVersions(project: str):
    if project in _cache["minecraftVersions"]:
        return _cache["minecraftVersions"][project]
    res = requests.get(f"{PAPERMC_BASE_ENDPOINT}/projects/{project}").json()["versions"]
    res.reverse()
    _cache["minecraftVersions"][project] = res
    return res

def getAvailableBuilds(project: str, minecraftVersion: str):
    if project in _cache["builds"] and minecraftVersion in _cache["builds"][project]:
        return _cache["builds"][project][minecraftVersion]
    res = requests.get(f"{PAPERMC_BASE_ENDPOINT}/projects/{project}/versions/{minecraftVersion}")
    if res.status_code != 200:
        raise Exception(f"Project {project} Version {minecraftVersion} returned {res.status_code} status.")
    res = res.json()["builds"]
    res.reverse()
    res = [str(x) for x in res]
    _cache["builds"][project][minecraftVersion] = res

    return res
