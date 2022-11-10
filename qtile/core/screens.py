from libqtile.config import Screen
from libqtile import bar, widget
from libqtile.lazy import lazy
from libqtile.bar import CALCULATED

bg = "#282c34"
fg = "#bbc2cf"

defaults = {
    "font": "mononoki Nerd Font Medium",
    "fontsize": 15,
    "padding": 1,
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
        highlight_method="text",
        active=fg,
        this_current_screen_border="#51afef",
        inactive="#5b6268",
        padding=2,
    )


def sep(bg: str, fg: str, offset=0, padding=8) -> widget.TextBox:
    return widget.TextBox(
        **base(bg, fg),
        **iconFont(),
        offset=offset,
        padding=padding,
        text="",
    )


def wifi(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, fg),
            **iconFont(),
            # offset=-1,
            text="直",
            x=-5,
            padding=4,
        ),
        widget.Wlan(
            **base(bg, fg),
            format="{essid}",
            interface="wlp2s0",
            padding=4,
        ),
    ]


def window_name(bg: str, fg: str) -> object:
    return widget.WindowName(
        **base(bg, fg),
        format="{name}",
        font="mononoki Nerd Font Bold",
        max_chars=30,
        width=CALCULATED,
    )


def cpu(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, "#51afef"),
            **iconFont(),
            # offset=20,
            text="",
            # x=20,
            padding=5,
        ),
        widget.CPU(
            **base(bg, fg),
            format="{load_percent:.0f}%",
        ),
    ]


def ram(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, "#51afef"),
            **iconFont(),
            # offset=-10,
            padding=5,
            text="﬙",
            # x=-10,
        ),
        widget.Memory(
            **base(bg, fg),
            format="{MemUsed: .0f}{mm} ",
            padding=-7,
        ),
    ]


def clock(bg: str, fg: str) -> list:
    return [
        widget.TextBox(
            **base(bg, "#ff6c6b"),
            **iconFont(),
            # offset=2,
            text="",
            # x=4,
            padding=5,
        ),
        widget.Clock(
            **base(bg, fg),
            format="%A, %B %d - %I:%M %p ",
            padding=6,
        ),
    ]


widgets: list = [
    widget.Spacer(length=2),
    logo(bg, "#51afef"),
    sep(bg, fg, offset=-8),
    group_box(bg),
    sep(bg, fg, offset=4, padding=4),
    *wifi(bg, fg),
    sep(bg, fg, offset=4, padding=4),
    widget.CurrentLayoutIcon(scale=0.8),
    widget.Spacer(),
    window_name(bg, fg),
    widget.Spacer(),
    *cpu(bg, fg),
    widget.Spacer(length=8),
    *ram(bg, fg),
    sep(bg, fg),
    widget.Systray(),
    sep(bg, fg),
    *clock(bg, fg),
    widget.Spacer(length=2),
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
