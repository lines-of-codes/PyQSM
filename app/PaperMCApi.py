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
    res = requests.get(f"{PAPERMC_BASE_ENDPOINT}/projects/{project}")
    if res.status_code != 200:
        raise Exception(f"Project {project} returned {res.status_code} status.")
    res = res.json()["versions"]
    res.reverse()
    _cache["minecraftVersions"][project] = res
    return res

def getAvailableBuilds(project: str, minecraftVersion: str):
    if minecraftVersion in _cache["builds"][project]:
        return _cache["builds"][project][minecraftVersion]
    res = requests.get(f"{PAPERMC_BASE_ENDPOINT}/projects/{project}/versions/{minecraftVersion}")
    if res.status_code != 200:
        raise Exception(f"Project {project} {minecraftVersion} returned {res.status_code} status.")
    res = res.json()["builds"]
    res.reverse()
    res = [str(x) for x in res]
    _cache["builds"][project][minecraftVersion] = res

    return res

def downloadBuild(project: str, minecraftVersion: str, build: str, location: str):
    res = requests.get(f"{PAPERMC_BASE_ENDPOINT}/projects/{project}/versions/{minecraftVersion}/builds/{build}")

    if res.status_code != 200:
        raise Exception(f"Project {project} {minecraftVersion} Build {build} returns {res.status_code} status.")

    fileName = res.json()["downloads"]["application"]["name"]
    res = requests.get(f"{PAPERMC_BASE_ENDPOINT}/projects/{project}/versions/{minecraftVersion}/builds/{build}/downloads/{fileName}")

    if res.status_code != 200:
        raise Exception(f"Project {project} {minecraftVersion} Build {build} failed to download. Returning {res.status_code} code.")

    with open(location, "wb") as f:
        f.write(res.content)
