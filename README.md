# Set up automatically changing wallpaper on linux
Personalize your desktop background (wallpaper) with a picture

A small python script that will set your wallpaper to something random from , made for linux window managers, 

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


### Automatic change background after unlock

1 - You must create new file on a folder: ~/.config/autostart

    File name : ~/.config/autostart/unlock_monitor.desktop



	[Desktop Entry]
		Type=Application
		Exec=/usr/local/bin/unlock_monitor
		Hidden=false
		NoDisplay=false
		X-GNOME-Autostart-enabled=true
		Name[en_US]=unlock_monitor
		Name=unlock_monitor
		Comment[en_US]=unlock_monitor
		Comment=unlock_monitor
	

2 - Create new bash file

    file: /usr/local/bin/unlock_monitor

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

	
	sudo chmode a+x /usr/local/bin/unlock_monitor
	sudo chmode a+x /var/lib/vlad/change_background.py
	










  


