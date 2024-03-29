from core.groups import groups
from core.keys import keys
from core.layouts import layouts, floating_layout
from core.mouse import mouse
from core.screens import screens, defaults

from core import hooks

widget_defaults = defaults.copy()
extension_defaults = defaults.copy()

__all__ = [
    "extension_defaults",
    "floating_layout",
    "groups",
    "hooks",
    "keys",
    "layouts",
    "mouse",
    "screens",
    "widget_defaults",
]
