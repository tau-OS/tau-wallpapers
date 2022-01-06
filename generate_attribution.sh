#!/bin/sh

for i in default/*.jpg; do
    [ -f "$i" ] || break
    x=${i##*/}

    echo "Found wallpaper $x"

    Y=$(echo ${x%.*} | sed 's/\-/\ /')

    echo """
${Y^}
============
Files: /usr/share/backgrounds/tauos/default/$x
Authors: ${Y^}  

License: Unsplash (https://unsplash.com/license)
    """ >> Attribution
done
