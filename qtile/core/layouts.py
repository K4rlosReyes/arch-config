from libqtile import layout
from libqtile.config import Match

# ---- Tiling ---------------------------- #
config = {
    "border_focus": "#bbc2cf",
    "border_normal": "#282c34",
    "border_width": 2,
    "margin": 6,
    "single_border_width": 0,
    "single_margin": 10,
}

layouts = [
    layout.MonadTall(
        **config,
        change_ratio=0.02,
        min_ratio=0.30,
        max_ratio=0.70,
    ),
    layout.Max(**config),
    layout.MonadThreeCol(**config),
]

# ---- Floating -------------------------- #
floating_layout = layout.Floating(
    border_focus="#dfdfdf",
    border_normal="#282c34",
    border_width=0,
    fullscreen_border_width=0,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(
            wm_class=[
                "confirmreset",
                "floating",
                "gnome-screenshot",
                "lxappearance",
                "makebranch",
                "maketag",
                "psterm",
                "ssh-askpass",
                "pcmanfm",
                "xfce4-about",
            ]
        ),  # type: ignore
        Match(
            title=[
                "branchdialog",
                "File Operation Progress",
                "Open File",
                "pinentry",
            ]
        ),  # type: ignore
    ],
)
