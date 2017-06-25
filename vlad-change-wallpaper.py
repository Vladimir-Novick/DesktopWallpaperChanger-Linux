#!/usr/bin/env python3

# Author: Vladimir Novick , <vlad.novick@gmail.com>
#
#                          https://www.linkedin.com/in/vladimirnovick
#                      
# Date: 24.01.2015
# Purpose: script for automatic changing wallpaper

#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import locale
import os
import re

try:  # try python 3 import
    from urllib.request import urlopen
    from urllib.request import urlretrieve
    from configparser import ConfigParser
except ImportError:  # fall back to python2
    from urllib import urlretrieve
    from urllib2 import urlopen
    from ConfigParser import ConfigParser

import xml.etree.ElementTree as ET

import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Notify

import random
import sys


def getFile(path):

  files = os.listdir(path);
  index = random.randrange(0, len(files));
  return files[index];

def change_background(filename):
    set_gsetting('org.gnome.desktop.background', 'picture-uri',
                 filename)
    
def set_gsetting(schema, key, value):
    gsettings = Gio.Settings.new(schema)
    gsettings.set_string(key, value)
    gsettings.apply()    

# replace with the actual path to the active  folder
path = "/home/vlad/Wallpapers"

fileName = getFile(path);

fullpash = "file://" + path + "/" + fileName;

change_background(fullpash);




        

