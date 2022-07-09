from libqtile import widget
from .theme import colors

def base(fg='fg', bg='bg'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='fg', bg='bg', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )
def workspaces():
    return [
        separator(),
        widget.GroupBox(
            **base(fg='fg'),
            font='UbuntuMono Nerd Font Medium',
            fontsize=15,
            margin_y=2,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['dark-blue'],
            inactive=colors['gray'],
            rounded=False,
            highlight_method='text',
            urgent_alert_method='block',
            urgent_border=colors['red'],
            this_current_screen_border=colors['dark-blue'],
            this_screen_border=colors['bg'],
            other_current_screen_border=colors['bg'],
            other_screen_border=colors['bg'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='fg'), fontsize=15, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    icon(bg="bg", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['bg'],
        colour_have_updates=colors['fg'],
        colour_no_updates=colors['fg'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    widget.Memory(
        background=colors['bg'],
        foreground=colors['fg'],

    ),

    widget.CurrentLayoutIcon(**base(bg='bg', fg='red'), scale=0.65),

    widget.Clock(**base(bg='bg'), format='%d/%m/%Y - %H:%M '),

    widget.Systray(background=colors['bg'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    widget.CurrentLayoutIcon(**base(bg='bg'), scale=0.65),

    widget.CurrentLayout(**base(bg='bg'), padding=5),

    widget.Clock(**base(bg='bg'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Medium',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
