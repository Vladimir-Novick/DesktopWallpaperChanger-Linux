#!/usr/bin/env python3

# Author: Vladimir Novick , <vlad.novick@gmail.com>
#
#                          https://www.linkedin.com/in/vladimirnovick
#
# Purpose: automatic changing wallpaper options
#
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
import pathlib

def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ];

userName = get_username();
path = "/home/"+ userName + "/Wallpapers";

command = 'mkdir -p ' + path ;
os.system(command);

command = 'cp -a ./Wallpapers/. ' + path + '/';
os.system(command);

pathAutoStart = "/home/"+ userName + "/.config/autostart";
command= 'mkdir -p ' + pathAutoStart ;
os.system(command);


currendDir =  os.path.dirname(os.path.realpath(__file__));

command = "chmod +x " + currendDir + "/change_background.py";
os.system(command);


fileName = pathAutoStart + "/mychange-wallpaper-autostart.desktop";
File = open(fileName,'w');
File.write("[Desktop Entry]\n");
File.write("Type=Application\n");
line = "Exec=" + currendDir + "/change_background.py\n";
File.write(line);
line = "Icon=" + currendDir + "/change_background_icon.png\n";
File.write(line);
File.write("Hidden=false\n");
File.write("NoDisplay=false\n");
File.write("X-GNOME-Autostart-enabled=true\n");
File.write("Name[en_US]=change background\n");
File.write("Name=change background - system start \n");
File.write("Comment[en_US]=change background - system start\n");
File.write("Comment=\n");
File.flush();
File.close();

command = "chmod +x " + fileName;
os.system(command);

command = 'gio set ' + fileName + ' "metadata::trusted" yes';
os.system(command);

fileName = "/home/"+ userName + "/Desktop/mychange-wallpaper.desktop";
File = open(fileName,'w');
File.write("[Desktop Entry]\n");
File.write("Type=Application\n");
line = "Exec=" + currendDir + "/change_background.py\n";
File.write(line);
line = "Icon=" + currendDir + "/change_background_icon.png\n";
File.write(line);
File.write("Hidden=false\n");
File.write("NoDisplay=false\n");
File.write("Name[en_US]=change background\n");
File.write("Name=change background \n");
File.write("Comment[en_US]=change background\n");
File.write("Comment=\n");
File.flush();
File.close();

command = "chmod +x " + fileName;
os.system(command);

command = 'gio set ' + fileName + ' "metadata::trusted" yes';
os.system(command);

fileName =  currendDir + "/myUnlock_monitor";
File = open(fileName,'w');

File.write('#!/bin/bash\n');
File.write('\n');
File.write('dbus-monitor --session "type=signal,interface=com.canonical.Unity.Session" --profile \\\n');
File.write('| while read dbusmsg; do\n');
File.write('    if [[ "$dbusmsg" =~ Unlocked$ || "$dbusmsg" =~ NameAcquired$ ]] ; then\n');
File.write('        sleep 5\n');
File.write('         ' + currendDir + '/change_background.py\n');
File.write('    fi\n');
File.write('done\n');
File.flush();
File.close();
command = "chmod +x " + fileName;
os.system(command);

command = 'gio set ' + fileName + ' "metadata::trusted" yes';
os.system(command);

fileName = pathAutoStart + "/mychange-wallpaper_unlock_manitor.desktop";
File = open(fileName,'w');
File.write("[Desktop Entry]\n");
File.write("Type=Application\n");
line = "Exec="+  currendDir + "/myUnlock_monitor\n";
File.write(line);
line = "Icon=" + currendDir + "/change_background_icon.png\n";
File.write(line);
File.write("Hidden=false\n");
File.write("NoDisplay=false\n");
File.write("Name[en_US]=change background unlock monitor\n");
File.write("Name=change background unlock monitor\n");
File.write("Comment[en_US]=change background unlock monitor\n");
File.write("Comment=\n");
File.flush();
File.close();
command = "chmod +x " + fileName;
os.system(command);

command = 'gio set ' + fileName + ' "metadata::trusted" yes';
os.system(command);
        

