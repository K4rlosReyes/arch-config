from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import hook
import subprocess
import os

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("brave"), desc="Launch Brave"),
    Key([mod], "p", lazy.spawn("dmenu_run"), desc="Launch Dmenu"),
    Key([mod], "c", lazy.spawn("code"), desc="Launch VSCode"),
    Key([mod], "q", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Launch Emacs"),
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="Launch PcManfm"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
]

groups = [
    Group(i)
    for i in [
        "dev",
        "www",
        "term",
        "misc",
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

layout_conf = {
    "border_normal": "#282c34",
    "border_focus": "#bbc2cf",
    "border_width": 2,
    "margin": 6,
}
layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(**layout_conf),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

### BAR
from libqtile.bar import CALCULATED


bg = "#282c34"
fg = "#bbc2cf"
defaults = {
    "font": "mononoki Nerd Font Medium",
    "fontsize": 10,
    "padding": None,
}


def base(bg: str, fg: str) -> dict:
    return {
        "background": bg,
        "foreground": fg,
    }


def iconFont(size=15) -> dict:
    return {"font": "mononoki Nerd Font", "fontsize": size}


def logo(bg: str, fg: str) -> widget.TextBox:
    return widget.TextBox(
        **base(bg, fg),
        #        **decoration(),
        **iconFont(),
        mouse_callbacks={"Button1": lazy.restart()},
        offset=4,
        padding=5,
        text="",
    )


def group_box(bg: str) -> widget.GroupBox:
    return widget.GroupBox(
        **iconFont(),
        background=bg,
        borderwidth=1,
        highlight_color=bg,
        highlight_method="line",
        inactive="#5b6268",
        padding=7,
    )


def sep(bg: str, fg: str, offset=0, padding=8) -> widget.TextBox:
    return widget.TextBox(
        **base(bg, fg),
        **iconFont(),
        offset=offset,
        padding=padding,
        text="",
    )


def volume(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, fg),
            #            **decoration("left"),
            **iconFont(),
            text="",
            x=4,
            padding=5,
        ),
        widget.Volume(
            **base(bg, fg),
            # **powerline("arrow_right"),
            volume_down_command="pamixer --decrease 5",
            volume_up_command="pamixer --increase 5",
            mute_command="pamixer --toggle-mute",
            get_volume_command="pamixer --get-volume-human",
            update_interval=0.2,
        ),
    ]


def updates(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, fg),
            **iconFont(),
            # offset=-1,
            text="",
            x=-5,
            padding=8,
        ),
        widget.CheckUpdates(
            **base(bg, fg),
            #            **decoration("right"),
            colour_have_updates=fg,
            colour_no_updates=fg,
            display_format="{updates} updates  ",
            distro="Arch_checkupdates",
            initial_text="No updates  ",
            no_update_string="No updates  ",
            padding=5,
            update_interval=3600,
        ),
    ]


def window_name(bg: str, fg: str) -> object:
    return widget.WindowName(
        **base(bg, fg),
        format="{name}",
        max_chars=60,
        width=CALCULATED,
    )


def cpu(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, fg),
            #            **decoration("left"),
            **iconFont(),
            # offset=20,
            text="",
            # x=20,
            padding=5,
        ),
        widget.CPU(
            **base(bg, fg),
            # **powerline("arrow_right"),
            format="{load_percent:.0f}%",
        ),
    ]


def ram(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, fg),
            **iconFont(),
            # offset=-10,
            padding=5,
            text="﬙",
            # x=-10,
        ),
        widget.Memory(
            **base(bg, fg),
            # **powerline("arrow_right"),
            format="{MemUsed: .0f}{mm} ",
            padding=1,
        ),
    ]


def clock(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, fg),
            #            **decoration("left"),
            **iconFont(),
            # offset=2,
            text="",
            # x=4,
            padding=5,
        ),
        widget.Clock(
            **base(bg, fg),
            #            **decoration("right"),
            format="%A - %I:%M %p ",
            padding=6,
        ),
    ]


widget_defaults = dict(
    font="mononoki Nerd Font Bold",
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()

widgets: list = [
    # widget.Spacer(length=2),
    logo(bg, fg),
    sep(bg, fg, offset=-8),
    group_box(bg),
    sep(bg, fg, offset=4, padding=4),
    *volume(bg, fg),
    *updates(bg, fg),
    widget.Spacer(),
    window_name(bg, fg),
    widget.Spacer(),
    *cpu(bg, fg),
    *ram(bg, fg),
    sep(bg, fg),
    *clock(bg, fg),
    widget.Spacer(length=2),
    widget.Systray(),
]

barra: dict = {
    "background": bg,
    "border_color": bg,
    "border_width": 4,
    "opacity": 1,
    "size": 24,
    "widgets": widgets,
}
screens = [
    Screen(
        top=bar.Bar(**barra),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])


wmname = "LG3D"
