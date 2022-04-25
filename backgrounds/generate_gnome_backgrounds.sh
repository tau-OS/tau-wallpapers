#!/bin/sh

for i in *.jpg; do
    [ -f "$i" ] || break
    echo "Found wallpaper $i"

    Y=$(echo ${i%.*} | sed 's/\-/\ /')

    echo """
    <wallpaper deleted="false">
        <name>${Y^}</name>
        <filename>@BACKGROUNDDIR@/$i</filename>
        <options>zoom</options>
        <shade_type>solid</shade_type>
        <pcolor>#3c6eb4</pcolor>
        <scolor>#294172</scolor>
    </wallpaper>
    """ >> tau-backgrounds.xml.in
done
