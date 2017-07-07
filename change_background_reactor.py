#!/usr/bin/python

import threading
import os
import random
import sys
import os.path

def getFile(path):

  files = os.listdir(path);
  index = random.randrange(0, len(files));
  return files[index];

def f():
   path = "/home/vlad/Wallpapers";
   fileName = getFile(path);
   fullpash = "file://" + path + "/" + fileName;
   command = 'gsettings set org.gnome.desktop.background picture-uri "' + fullpash + '"';
   os.system(command);    # do something here ...
   threading.Timer(600, f).start();

# start calling f now and every 60 sec thereafter
f()
  