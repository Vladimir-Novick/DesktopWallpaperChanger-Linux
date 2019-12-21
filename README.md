# Set up automatically changing wallpaper on linux
Personalize your desktop background (wallpaper) with a picture

A small python script that will set your desktop wallpaper and lock screen background to something random pictures from your wallpapers catalog


### Automatic installation

Install.py is a simple python script that installs the wallpapper-changer.
All images are stored in the "Home/Wallpappes" directory

1) Make sure the script is executable by running : chmod +x install.py
  or check "Allow executing file as program"
   ![check permissions](https://github.com/Vladimir-Novick/wallpaper-changer/img/permissions.png)

2) Run :  ./install.py 
  or
 - select istall.py from file browser and "Open With Outher Application" :
 ![run installer](https://github.com/Vladimir-Novick/wallpaper-changer/img/run_install.png)

3) try run istall.py again

enjoy

## Manual installation

### Automatic change background after login

you must create new file on a folder : ~/.config/autostart

File name :
    
	~/.config/autostart/change-wallpaper-autostart.desktop


	[Desktop Entry]
		Type=Application
		Exec=/var/lib/vlad/change_background.py
		Hidden=true
		NoDisplay=true
		X-GNOME-Autostart-enabled=true
		Name[en_US]=change background
		Name=change background
		Comment[en_US]=
		Comment=change background after login

please change "/var/lib/vlad" to your current folder name.

### Automatic change background after unlock

1 - Create new file on a folder: ~/.config/autostart
     

    file: ~/.config/autostart/unlock_monitor

        #!/bin/bash

        dbus-monitor --session "type='signal',interface='org.gnome.ScreenSaver'" | \
        (
          locked=0
          while true; do
            read X
                echo "$X"
                if echo "$X" | grep "member=ActiveChanged" &> /dev/null; then
                    if [ $locked -eq 0 ]; then
                      echo "************* Screen locked"
                      locked=1
                    elif [ $locked -eq 1 ]; then
                        echo "********* Screen unlocked"
                sleep 5
                /home/vlad/mygithub/wallpaper-changer/source/change_background.py
                      locked=0
                    fi
                fi

          done
        )

2  - set files as executable:

			
		 chmod a+x ~/.config/autostart//unlock_monitor
			

please change "/var/lib/vlad" to your current folder name.








  


