#!/bin/bash

setxkbmap -option caps:swapescape
setxkbmap -option altwin:swap_lalt_lwin
setxkbmap -option ctrl:ralt_rctrl
xinput set-prop 12 323 1
