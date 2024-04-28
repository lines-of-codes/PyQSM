# This Python file uses the following encoding: utf-8

# This Python file uses the following encoding: utf-8
import requests
import platform

base_endpoint = "https://api.adoptium.net/v3"
headers = {
    'User-Agent': 'PyQSM/1.0.0'
}
cache = {}
versions = {}
archive_type = {
    "windows": "zip",
    "macos": "tar.gz",
    "linux": "tar.gz"
}

def getAvailableReleases():
    availableReleases = requests.get(f"{base_endpoint}/info/available_releases", headers=headers)

    if availableReleases.status_code != 200:
        raise Exception(f"Failed to list available releases for Eclipse Temurin. {availableReleases.status_code} returned instead.")

    availableReleases = availableReleases.json()

    for release in availableReleases["available_releases"]:
        displayName = f"Java {release}"

        if release in availableReleases["available_lts_releases"]:
            displayName += " (LTS)"

        versions[displayName] = release

def getos():
    os = platform.system().lower()
    # Assume that this is macOS because this software is made for PCs
    if os == "darwin":
        os = "mac"
    return os

def getarch():
    arch = platform.machine()
    if arch == "x86_64":
        arch = "x64"

    return arch

def listJRE(versionChoice: str) -> list[str]:
    version = versions[versionChoice]
    os = getos()
    if cache.get(versionChoice) is not None:
        return cache[versionChoice]["releases"]
    response = requests.get(f"{base_endpoint}/info/release_names?architecture={getarch()}&heap_size=normal&image_type=jre&os={os}&page=0&page_size=10&project=jdk&release_type=ga&semver=false&sort_method=DEFAULT&sort_order=DESC&vendor=eclipse&version=%5B{version}%2C{version + 1}%5D", headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to list builds for Eclipse Temurin JRE {versionChoice} Runtime. {response.status_code} returned instead.")

    json = response.json()
    cache[versionChoice] = json
    return json["releases"]

def downloadJRE(versionChoice, selectedIndex, location):
    """
    versionChoice is the major java version display name
    selectedIndex is the index of the user's selection in the list of JREs
    location is a folder which the JRE should be placed in. This folder must already exist.
    """

    if cache.get(versionChoice) is None:
        listJRE(versionChoice)

    response = requests.get(cache[versionChoice][selectedIndex]["download_url"])

    if response.status_code != 200:
        raise Exception(f"Azul JRE ({versionChoice} index {selectedIndex}) download link returns {response.status_code}.")

    with open(location, "wb") as f:
        f.write(response.content)

