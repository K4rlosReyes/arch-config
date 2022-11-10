from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from core.keys import keys, mod

groups = [
    Group(i)
    for i in [
        "dev",
        "www",
        "term",
        "misc",
        "prod",
        "xtra",
    ]
]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend(
        [
            # Switch to workspace N
            Key([mod], actual_key, lazy.group[group.name].toscreen()),
            # Send window to workspace N
            Key([mod, "shift"], actual_key, lazy.window.togroup(group.name)),
        ]
    )
