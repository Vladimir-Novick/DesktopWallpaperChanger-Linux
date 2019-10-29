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
import sys
import pathlib
import stat
import pwd

def get_umask():
    umask = os.umask(0)
    os.umask(umask)
    return umask

def chmod_x(path):
    os.chmod(
        path,
        os.stat(path).st_mode |
        (
            (
                stat.S_IXUSR |
                stat.S_IXGRP |
                stat.S_IXOTH
            )
            & ~get_umask()
        )
    )



def get_username():
    return pwd.getpwuid( os.getuid() )[ 0 ]

userName = get_username()
path = "/home/"+ userName + "/Wallpapers"

command = 'mkdir -p ' + path 
os.system(command)

command = 'cp -a ./Wallpapers/. ' + path + '/'
os.system(command)

pathAutoStart = "/home/"+ userName + "/.config/autostart"
command= 'mkdir -p ' + pathAutoStart 
os.system(command)


currendDir =  os.path.dirname(os.path.realpath(__file__))

fileNameBackground =  currendDir + "/change_background.py"


fileNameAutostart = pathAutoStart + "/mychange-wallpaper-autostart.desktop"

if os.path.exists(fileNameAutostart) :
    command = 'sudo rm ' + fileNameAutostart
    os.system(command)


with open(fileNameAutostart,'w') as File :
    File.write("[Desktop Entry]\n")
    File.write("Type=Application\n")
    line = "Exec=" + currendDir + "/change_background.py\n"
    File.write(line)
    line = "Icon=" + currendDir + "/change_background_icon.png\n"
    File.write(line)
    File.write("Hidden=false\n")
    File.write("NoDisplay=false\n")
    File.write("X-GNOME-Autostart-enabled=true\n")
    File.write("Name[en_US]=change background\n")
    File.write("Name=change background - system start \n")
    File.write("Comment[en_US]=change background - system start\n")
    File.write("Comment=\n")
    File.flush()
    File.close()


fileNameDesktopFile = "/home/"+ userName + "/Desktop/mychange-wallpaper.desktop"

if os.path.exists(fileNameDesktopFile) :
    command = 'sudo rm ' + fileNameDesktopFile
    os.system(command)


with open(fileNameDesktopFile, 'w') as File:
    File.write("[Desktop Entry]\n")
    File.write("Type=Application\n")
    line = "Exec=" + currendDir + "/change_background.py\n"
    File.write(line)
    line = "Icon=" + currendDir + "/change_background_icon.png\n"
    File.write(line)
    File.write("Hidden=false\n")
    File.write("NoDisplay=false\n")
    File.write("Name[en_US]=change background\n")
    File.write("Name=change background \n")
    File.write("Comment[en_US]=change background\n")
    File.write("Comment=\n")
    File.close()
    File.flush



batchUnlock_monitorSleep =  pathAutoStart + "/myUnlock_monitor"

if os.path.exists(batchUnlock_monitorSleep) :
    command = 'sudo rm ' + batchUnlock_monitorSleep
    os.system(command)


with open(batchUnlock_monitorSleep,'w') as File:
    File.write('#!/bin/bash\n')
    File.write('\n')
    File.write("    dbus-monitor --session \"type='signal',interface='org.gnome.ScreenSaver'\" | \\\n")
    File.write('(\n')
    File.write('  locked=0\n')
    File.write('  while true; do\n')
    File.write('    read X\n')
    File.write('        if echo "$X" | grep "member=ActiveChanged" &> /dev/null; then\n')
    File.write('            if [ $locked -eq 0 ]; then\n')
    File.write('              locked=1\n')
    File.write('            elif [ $locked -eq 1 ]; then\n')
    File.write('         sleep 5\n')
    File.write('        '+ currendDir + '/change_background.py\n')
    File.write('               locked=0\n')
    File.write('            fi\n')
    File.write('         fi\n')
    File.write('  done\n')
    File.write(')\n')
    File.flush()
    File.close()


chmod_x(fileNameBackground)

chmod_x(fileNameAutostart)

chmod_x(fileNameDesktopFile)

chmod_x(batchUnlock_monitorSleep )


command = 'gio set ' + fileNameDesktopFile + ' "metadata::trusted" yes'
os.system(command)


command = 'gio set ' + batchUnlock_monitorSleep + ' "metadata::trusted" yes'
os.system(command)

command = 'gio set ' + fileNameAutostart + ' "metadata::trusted" yes'
os.system(command)

        

