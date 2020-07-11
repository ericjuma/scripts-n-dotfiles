from libqtile.config import Key, Screen, Group, Drag, Click, Match, ScratchPad, DropDown
from os import system
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
import json

from typing import List  # noqa: F401

mod = "mod4"
ctrl = "control"
shft = "shift"

keys = [

    # hjkl
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "l", lazy.layout.shuffle_down()),
    Key([mod], "h", lazy.layout.shuffle_up()),

    Key([mod, ctrl], "j", lazy.layout.grow()),
    Key([mod, ctrl], "k", lazy.layout.shrink()),

    # control
    Key([mod, ctrl], "q", lazy.shutdown()),
    Key([mod], "w", lazy.layout.next()),
    Key([mod], "e", lazy.next_layout()),
    Key([mod], "r", lazy.spawncmd()),
    Key([mod], "t", lazy.layout.toggle_split()),

    Key([mod, ctrl], "l", lazy.window.kill()),
    Key([mod, ctrl], "r", lazy.restart()),
    Key([mod, shft], "r", lazy.layout.rotate()),

    # program launchers
    Key([mod], "Return", lazy.spawn("kitty")),
    Key([mod], "n", lazy.spawn("firefox")),
    Key([mod], "m", lazy.spawn("qutebrowser")),
    Key([mod], "comma", lazy.spawn("startup")),
    Key([mod], "period", lazy.spawn("scrt-select")),
    Key([mod, ctrl], "period", lazy.spawn("scrt")),

]

groups = [Group(i) for i in "asdfzxcv"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

with open('/home/mimi/.cache/wal/colors.json') as f:
    colorscheme = json.load(f)

backgr = colorscheme['special']['background']
foregr = colorscheme['special']['foreground']
#color1 = colorscheme['colors']['color5']
color1 = colorscheme['colors']['color1']
color2 = colorscheme['colors']['color6']
color3 = colorscheme['colors']['color2']

layouts = [
    layout.MonadTall( border_width=10, margin=80, ratio=.56, border_focus=foregr, border_normal=backgr ),
    layout.Max(),
    # layout.Columns(), layout.Matrix(), layout.MonadWide(), layout.RatioTile(), layout.Tile(), layout.VerticalTile(),
]

widget_defaults = dict(
    font='monospace',
    fontsize=24,
    padding=9,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(foreground=foregr),
                widget.GroupBox(active=foregr, disable_drag=True, this_current_screen_border=color1, other_screen_border=backgr, borderwidth=2),
                widget.Prompt(foreground=foregr),
                widget.WindowName(foreground=backgr),
                widget.Systray(foreground=foregr),
                widget.Clock(foreground=foregr, format='%a the %d  |  %I:%M'),
            ],
            50,
            background=backgr,
            foreground=foregr
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


dgroups_app_rules = [] # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
#system("startup")
