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
    res = requests.get(f"{PURPURMC_BASE_ENDPOINT}/{project}")
    if res.status_code != 200:
        raise Exception(f"Project {project} returned {res.status_code} status.")
    res = res.json()["versions"]
    res.reverse()
    _cache["minecraftVersions"][project] = res
    return res

def getAvailableBuilds(minecraftVersion: str, project: str = PURPUR):
    if minecraftVersion in _cache["builds"][project]:
        return _cache["builds"][project][minecraftVersion]
    res = requests.get(f"{PURPURMC_BASE_ENDPOINT}/{project}/{minecraftVersion}")
    if res.status_code != 200:
        raise Exception(f"Project {project} Version {minecraftVersion} returned {res.status_code} status.")
    res = res.json()["builds"]["all"]
    res.reverse()
    _cache["builds"][project][minecraftVersion] = res
    return res

def downloadBuild(minecraftVersion: str, build: str, location: str, project: str = PURPUR):
    res = requests.get(f"{PURPURMC_BASE_ENDPOINT}/{project}/{minecraftVersion}/{build}/download")

    if res.status_code != 200:
        raise Exception(f"Project {project} {minecraftVersion} Build {build} failed to download. Returning {res.status_code} code.")

    with open(location, "wb") as f:
        f.write(res.content)
