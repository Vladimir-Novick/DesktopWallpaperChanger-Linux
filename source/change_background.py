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

import os
import random
import sys
import pwd

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ];

def getFile(path):

  files = os.listdir(path);
  index = random.randrange(0, len(files));
  return files[index];

userName = get_username();
path = "/home/"+ userName + "/Wallpapers";

fileName = getFile(path);

fullpash = "file://" + path + "/" + fileName;

command = 'gsettings set org.gnome.desktop.background picture-uri "' + fullpash + '"';
os.system(command);


        

