from libqtile.config import Key
from libqtile.lazy import lazy

from libqtile.core.manager import Qtile


def float_to_front(qtile: Qtile) -> None:
    for window in qtile.current_group.windows:
        if window.floating:
            window.bring_to_front()


# from utils import config

keys, mod, alt = [], "mod4", "mod1"
# terminal = config['terminal'].copy()
terminal = "alacritty"

# if not terminal['main']:
#  terminal['main'] = guess_terminal()

for key in [
    # Switch/move between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),
    # Increase/decrease window size
    ([mod], "i", lazy.layout.grow()),
    ([mod], "m", lazy.layout.shrink()),
    # Window management
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod], "o", lazy.layout.maximize()),
    ([mod], "n", lazy.layout.normalize()),
    ([mod], "w", lazy.window.kill()),
    ([mod], "f", lazy.window.toggle_maximize()),
    ([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
    # Floating window management
    ([mod], "space", lazy.window.toggle_floating()),
    # Toggle between layouts
    ([mod], "Tab", lazy.next_layout()),
    # Qtile management
    ([mod, "control"], "b", lazy.hide_show_bar()),
    ([mod, "control"], "s", lazy.shutdown()),
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, alt], "r", lazy.restart()),
    # Kill xorg server
    ([mod, alt], "s", lazy.spawn("kill -9 -1")),
    # Terminal
    ([mod], "Return", lazy.spawn(terminal)),
    ([mod, "shift"], "Return", lazy.spawn(terminal)),
    # Application Launcher
    ([mod], "p", lazy.spawn("dmenu_run")),
    # Apps
    ([mod], "b", lazy.spawn("brave")),
    ([mod], "c", lazy.spawn("code")),
    ([mod], "q", lazy.spawn("emacsclient -c -a 'emacs'")),
    ([mod], "e", lazy.spawn("pcmanfm")),
    # Backlight
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # Volume
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    # Player
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
]:
    keys.append(Key(*key))  # type: ignore
