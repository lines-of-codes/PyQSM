# This Python file uses the following encoding: utf-8

"""
Minecraft Server Properties files are in a key=value format with # as the comment sign
For example:

# The following property changes the difficulty level of the game
difficulty=easy
"""

import re

class ServerProperties:
    def __init__(self):
        self.values = {}

    def parse(self, string):
        for line in string.split("\n"):
            self.parseLine(line)

    def parseLine(self, line):
        result = re.search("#", line)

        if result is not None:
            line = line[:result.span()[0]]
            # If the string is empty (the whole line is a comment), return.
            if not line.strip():
                return

        result = re.search(".+=.+", line)

        # If the line does not match the key=value pattern, return.
        if result is None:
            return

        key, *value = line.split("=")

        if isinstance(value, list):
            value = "=".join(value)

        if value.lower() == "true":
            value = True
        elif value.lower() == "false":
            value = False

        self.values[key] = value

    def __str__(self):
        result = ""

        for k, v in self.values.items():
            result += f"{k}={v}"

        return result
