#!/usr/bin/python

import threading
import os
import random
import sys
import os.path
import pwd

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ];

def getFile(path):

  files = os.listdir(path);
  index = random.randrange(0, len(files));
  return files[index];

  

def f():
   user = get_username();
   path = "/home/" + user + "/Wallpapers";
   fileName = getFile(path);
   fullpash = "file://" + path + "/" + fileName;
   command = 'gsettings set org.gnome.desktop.background picture-uri "' + fullpash + '"';
   os.system(command);   
   threading.Timer(600, f).start();


f()
  
