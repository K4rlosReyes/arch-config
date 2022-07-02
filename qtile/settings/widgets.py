from libqtile import widget
from .theme import colors

def base(fg='text', bg='crust'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='crust', fontsize=16, text="?"):
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
            **base(fg='flamingo'),
            font='UbuntuMono Nerd Font Medium',
            fontsize=15,
            margin_y=2,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['green'],
            inactive=colors['overlay1'],
            rounded=False,
            highlight_method='text',
            urgent_alert_method='block',
            urgent_border=colors['red'],
            this_current_screen_border=colors['blue'],
            this_screen_border=colors['base'],
            other_current_screen_border=colors['base'],
            other_screen_border=colors['base'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='blue'), fontsize=15, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),

    separator(),

    icon(bg="crust", text=' '), # Icon: nf-fa-download

    widget.CheckUpdates(
        background=colors['crust'],
        colour_have_updates=colors['text'],
        colour_no_updates=colors['text'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    icon(bg="crust", text=''),

    widget.Memory(
        background=colors['crust'],
        foreground=colors['text'],

    ),

    widget.CurrentLayoutIcon(**base(bg='crust'), scale=0.65),

    widget.Clock(**base(bg='crust'), format='%d/%m/%Y - %H:%M '),

    widget.Systray(background=colors['crust'], padding=5),
]

secondary_widgets = [
    *workspaces(),

    separator(),

    widget.CurrentLayoutIcon(**base(bg='flamingo'), scale=0.65),

    widget.CurrentLayout(**base(bg='crust'), padding=5),

    widget.Clock(**base(bg='crust'), format='%d/%m/%Y - %H:%M '),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Medium',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
