# Set up automatically changing wallpaper on linux
Personalize your desktop background (wallpaper) with a picture

A small python script that will set your desktop wallpaper and lock screen background to something random pictures from your wallpapers catalog


## Install using Git

If you are a git user, you can install the theme and keep up to date by cloning the repo:

		git clone https://github.com/Vladimir-Novick/wallpaper-changer

If you are a not git user:

  Download using the [GitHub .zip](https://github.com/Vladimir-Novick/wallpaper-changer/archive/master.zip) download option and unzip them.

## Activating: 

Install.py is a simple python script that installs the wallpapper-changer.
All images are stored in the "Home/Wallpappes" directory

1) Once it’s downloaded, open your file manager and go to the download destination folder.    
Then right-click the "install.py" and select properties in the context menu.
Next, select the Permissions tab and tick on Allow executing file as program.  

   ![check permissions](/img/permissions.png)
   
and close the "install.py" Properties window
 

2) Open up the terminal, and type ./install.py   
 OR   
 right-click the "install.py" and   
  select "Open With Outher Application" in the context menu.
  
 ![run installer](/img/run_install.png)

3) try run install.py again

4) For Ubuntu 19.04, 19.10 :  
 Press mouse right-click on the "mychange-wallpaper.desktop" and select "Allow Launching" in the context menu.
 
![run installer](/img/allow_launching.png)



## Install manually

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








  


