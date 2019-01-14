
l=$(cvt 1280 1024 60 | grep Modeline)
mode=$(echo $l|cut -d ' ' -f 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)
modname=$(echo $l|cut -d ' ' -f 2|cut -d '"' -f 2)
dev=$(xrandr | grep primary | cut -d ' ' -f 1)

xrandr --newmode $mode
xrandr --addmode $dev $modname
xrandr -s $modname

