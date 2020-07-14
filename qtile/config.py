from libqtile.config import Key, Screen, Group, Drag, Click, Match, ScratchPad, DropDown
from os import system
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
import json

from typing import List  # noqa: F401

mod = "mod4"
alt = "mod1"
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

    Key([mod], "BackSpace", lazy.window.kill()),
    Key([mod, ctrl], "r", lazy.restart()),
    Key([mod, shft], "r", lazy.layout.rotate()),

    # program launchers
    Key([mod], "Return", lazy.spawn("kitty")),
    Key([mod], "n", lazy.spawn("firefox")),
    Key([mod], "m", lazy.spawn("qutebrowser")),
    Key([mod], "comma", lazy.spawn("startup")),
    Key([mod], "period", lazy.spawn("scrt-select")),
    Key([mod, ctrl], "period", lazy.spawn("scrt")),

    Key([], "XF86AudioRaiseVolume", lazy.spawn("volume +10%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("volume -10%")),
    Key([], "XF86AudioMute", lazy.spawn("volume mute")),

    #Key([mod], "Down", lazy.spawn("theme set dark")),
    #Key([mod], "Up", lazy.spawn("theme set light")),
    Key([mod], "Right", lazy.spawn("theme wallcolor rand")),

]

groups = [Group(i) for i in "asdfzxcv"]

for i in groups:
    keys.extend([
        Key([mod], i.name, lazy.group[i.name].toscreen()),

        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True)),
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
    ])

groups.append(
    ScratchPad("scratchpad",
        [
           # DropDown("signal", "signal-desktop",
           #          x=0.2, y=0.05, width=0.65, height=0.9,
           #          opacity=0.95,
           #          on_focus_lost_hide=True),
            DropDown("py", "kitty python",
                     x=0.2, y=0.05, width=0.5, height=0.5,
                     opacity=0.80,
                     on_focus_lost_hide=True),
            DropDown("term", "kitty",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.80,
                     on_focus_lost_hide=True),
            DropDown("browser", "qutebrowser --config ~/.config/qutebrowser/no-daemon-config.py",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.95,
                     on_focus_lost_hide=True),
            DropDown("notes", "kitty nvim docs/karma.org",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.8,
                     on_focus_lost_hide=True),
            DropDown("vi", "kitty nvim",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.8,
                     on_focus_lost_hide=True),
            DropDown("torrent", "transmission-gtk",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.8,
                     on_focus_lost_hide=True),
            DropDown("audio", "pavucontrol",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.8,
                     on_focus_lost_hide=True),
            DropDown("music", "kitty zsh -c 'cd ~/music/songs; zsh'",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.8,
                     on_focus_lost_hide=True),
            DropDown("files", "kitty ranger",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=0.8,
                     on_focus_lost_hide=True),
            DropDown("msg", "signal",
                     x=0.2, y=0.05, width=0.65, height=0.9,
                     opacity=1,
                     on_focus_lost_hide=True),
        ])
)

numkey_dropdowns = [
    lazy.group['scratchpad'].dropdown_toggle('py'),
    lazy.group['scratchpad'].dropdown_toggle('vi'),
    lazy.group['scratchpad'].dropdown_toggle('notes'),
    lazy.group['scratchpad'].dropdown_toggle('term'),
    lazy.group['scratchpad'].dropdown_toggle('torrent'),
    lazy.group['scratchpad'].dropdown_toggle('audio'),
    lazy.group['scratchpad'].dropdown_toggle('music'),
    lazy.group['scratchpad'].dropdown_toggle('files'),
    lazy.group['scratchpad'].dropdown_toggle('msg'),
]

for number, dropdown in enumerate(numkey_dropdowns, start=1):
    keys.append(Key([mod], str(number), dropdown))

with open('/home/mimi/.cache/wal/colors.json') as f:
    colorscheme = json.load(f)

backgr = colorscheme['special']['background']
foregr = colorscheme['special']['foreground']
color1 = colorscheme['colors']['color1']
color2 = colorscheme['colors']['color6']
color3 = colorscheme['colors']['color8']

layouts = [
    layout.MonadTall( border_width=3, margin=80, ratio=.56, border_focus=color2, border_normal=backgr ),
    layout.Max(),
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
                widget.WindowName(markup=False, foreground=backgr),
                widget.Systray(foreground=foregr),
                widget.Clock(foreground=foregr, format='%a the %d  |  %I:%M'),
            ],
            50,
            background=backgr,
            foreground=foregr,
            #opacity=.7,

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


follow_mouse_focus = True
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': ' download'},
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
], border_focus=color1)
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "LG3D"
