# This Python file uses the following encoding: utf-8

import requests

PURPURMC_BASE_ENDPOINT = "https://api.purpurmc.org/v2"
PURPUR = "purpur"
_cache = {
    "minecraftVersions": {},
    "builds": {
        PURPUR: {}
    }
}

def getAvailableMinecraftVersions(project: str = PURPUR):
    if project in _cache["minecraftVersions"]:
        return _cache["minecraftVersions"][project]
    res = requests.get(f"{PURPURMC_BASE_ENDPOINT}/{project}").json()["versions"]
    _cache["minecraftVersions"][project] = res
    return res

def getAvailableBuilds(minecraftVersion: str, project: str = PURPUR):
    if project in _cache["builds"]:
        return _cache["builds"][project]
    res = requests.get(f"{PURPURMC_BASE_ENDPOINT}/{project}/{minecraftVersion}").json()["builds"]
    _cache["builds"][project][minecraftVersion] = res
    return res
