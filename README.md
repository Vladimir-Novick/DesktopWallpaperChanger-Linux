# Set up automatically changing wallpaper on linux
Personalize your desktop background (wallpaper) with a picture

A small python script that will set your wallpaper to something random pictures from your wallpapers catalog

[More details please look WIKI](https://github.com/Vladimir-Novick/wallpaper-changer/wiki)

### Automatic installation

Install.py is a simple python script that installs the wallpapper-changer.
All images are stored in the "Home/Wallpappes" directory

1) Make sure the script is executable by running : chmod +x install.py
2) Run :  ./install.py 

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

1 - You must create new file on a folder: ~/.config/autostart
     
    File name : ~/.config/autostart/unlock_monitor.desktop


		
		[Desktop Entry]
		  Type=Application
		  Exec=/var/lib/vlad/unlock_monitor
		  Hidden=false
		  NoDisplay=false
		  X-GNOME-Autostart-enabled=true
		  Name[en_US]=unlock_monitor
		  Name=unlock_monitor
		  Comment[en_US]=unlock_monitor
		  Comment=unlock_monitor
			
			please change "/var/lib/vlad" to your current folder name.

2 - Create new bash file

    file: /var/lib/vlad/unlock_monitor

		#!/bin/bash
		dbus-monitor --session "type=signal,interface=com.canonical.Unity.Session" --pr$
		| while read dbusmsg; do
  		  if [[ "$dbusmsg" =~ Unlocked$ || "$dbusmsg" =~ NameAcquired$ ]] ; then
     		   sleep 5
     		    /var/lib/vlad/change_background.py
     		   # ...
  		  fi
		done
3  - set files as executable:

			
		 chmod a+x /var/lib/vlad/bin/unlock_monitor
		 chmod a+x /var/lib/vlad/change_background.py
			

please change "/var/lib/vlad" to your current folder name.








  


