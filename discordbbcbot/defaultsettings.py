"""
initial state for discordbbc settings file (settings.json)
"""
from __future__ import annotations

from typing import TypedDict


class SettingsDict(TypedDict):
    discord: DiscordSettingsDict


class DiscordSettingsDict(TypedDict):
    token: str


DEFAULT_SETTINGS: SettingsDict = {
    "discord": {
        "token": "[Enter your token]"
    }
}
