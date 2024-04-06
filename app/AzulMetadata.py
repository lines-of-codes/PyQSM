# This Python file uses the following encoding: utf-8
import requests
import platform

cache = {}
versions = {
    "Java 22": 22,
    "Java 21 (LTS)": 21,
    "Java 17 (LTS)": 17,
    "Java 11 (LTS)": 11,
    "Java 8 (LTS)": 8
}
archive_type = {
    "windows": "zip",
    "macos": "tar.gz",
    "linux": "tar.gz"
}

# Trim out zeros at the end of a version array
def trimSemVerDisplay(ver: list):
    if len(ver) == 1:
        return listToString(ver)

    if ver[-1] == 0:
        ver.pop()
        return trimSemVerDisplay(ver)

    return listToString(ver)

def listToString(l: list):
    return [str(i) for i in l]

def jreDataToSummary(data):
    return f"Azul Zulu JRE {'.'.join(trimSemVerDisplay(data['java_version']))}+{data['openjdk_build_number']} (Zulu {'.'.join(trimSemVerDisplay(data['distro_version']))}, {data['name']})"

def getos():
    os = platform.system().lower()
    # Assume that this is macOS because this software is made for PCs
    if os == "darwin":
        os = "macos"
    return os

def getarch():
    arch = platform.machine()
    if arch == "x86_64":
        arch = "x64"

    return arch

def listJRE(versionChoice):
    os = getos()
    if cache.get(versionChoice) is not None:
        return [jreDataToSummary(x) for x in cache[versionChoice]]
    response = requests.get(f"https://api.azul.com/metadata/v1/zulu/packages/?java_version={versions[versionChoice]}&arch={getarch()}&os={getos()}&java_package_type=jre&archive_type={archive_type[os]}&javafx_bundled=false&crac_supported=false")

    if response.status_code != 200:
        raise Exception(f"Failed to list builds for Azul {versionChoice} Runtime")

    json = response.json()
    cache[versionChoice] = json
    return [jreDataToSummary(x) for x in json]

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
