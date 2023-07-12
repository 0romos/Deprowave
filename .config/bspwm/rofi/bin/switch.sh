

# Variables
param=$1

# Functions
switch_purpmal () {
    cd /home/gast/.local/share/local_themes/purpmal/ && cp -r * ~/.config/
    #cp -r /home/gast/.local/share/local_themes/purpmal/gtk.css /usr/share/gtk-3.0/
    cp -r /home/gast/.local/share/local_themes/purpmal/app.css /home/gast/Documents/Bento/
    bspc wm -r
}

switch_greenmal () {
    cd /home/gast/.local/share/local_themes/greenmal/ && cp -r * ~/.config/
    #cp -r /home/gast/.local/share/local_themes/greenmal/gtk.css /usr/share/gtk-3.0/
    cp -r /home/gast/.local/share/local_themes/greenmal/app.css /home/gast/Documents/Bento/
    bspc wm -r
}

move_files () {

    if [[ "$param" == "purpmal" ]]; then
        clear
        echo "[DEBUG] Switching to the PurpMal driver"
        switch_purpmal

    elif [[ "$param" == "greenmal" ]]; then
        clear
        echo "[DEBUG] Switching to the GreenMal driver"
        switch_greenmal

    else
        echo "[DEBUG] Unknown theme: $param"
    fi

}

move_files
