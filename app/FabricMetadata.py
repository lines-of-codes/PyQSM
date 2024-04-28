# This Python file uses the following encoding: utf-8

import requests

FABRIC_BASE_ENDPOINT = "https://meta.fabricmc.net/v2"
_cache = {
    "minecraftVersions": [],
    "builds": {}
}

def getAvailableMinecraftVersions():
    if len(_cache["minecraftVersions"]) > 0:
        return _cache["minecraftVersions"]
    res = requests.get(f"{FABRIC_BASE_ENDPOINT}/versions/game")
    if res.status_code != 200:
        raise Exception(f"Fabric supported game version listing returned {res.status_code} status.")
    res = res.json()
    res = [x["version"] for x in res]
    _cache["minecraftVersions"] = res
    return res

def getAvailableLoaderVersion(minecraftVersion: str):
    if minecraftVersion in _cache["builds"]:
        return _cache["builds"][minecraftVersion]
    res = requests.get(f"{FABRIC_BASE_ENDPOINT}/versions/loader/{minecraftVersion}")
    if res.status_code != 200:
        raise Exception(f"Fabric {minecraftVersion} build listing returned {res.status_code} status.")
    res = res.json()
    res = [x["loader"]["version"] for x in res]
    _cache["builds"][minecraftVersion] = res

    return res

def downloadBuild(minecraftVersion: str, loaderVersion: str, location: str):
    res = requests.get(f"{FABRIC_BASE_ENDPOINT}/versions/loader/{minecraftVersion}/{loaderVersion}/1.0.0/server/jar")

    if res.status_code != 200:
        raise Exception(f"Fabric {minecraftVersion} Loader {loaderVersion} Installer 1.0.0 failed to download. Returning {res.status_code} code.")

    with open(location, "wb") as f:
        f.write(res.content)

