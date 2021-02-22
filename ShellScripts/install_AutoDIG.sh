# Saves the directory for compatability with Auto-DIG application.
cd ../
temp_dir=$PWD
DIR="${temp_dir:1}"
# Copy Auto-DIG.desktop to /home/${USER}/Desktop
cd ./ShellScripts
sudo cp Auto-DIG.desktop /home/${USER}/Desktop
# Make executable and trusted
chmod +x Auto-DIG.desktop
# Dialog may appear to ask if trusted. Allow user to say yes. The below could be used to bypass if desired.
gio set /home/$USER/Desktop/Auto-DIG.desktop "metadata::trusted" yes
# Copy image to /usr/share/pixmaps
sudo cp /${DIR}/ImagesForApp/autoDIG.png /usr/share/pixmaps
# Send DIR to startAutoDIG.sh
sed -i "s|home/${USER}/git-repos/Auto-DIG|${DIR}|g" startAutoDIG.sh
# Copy startAutoDIG.sh to bin
sudo cp /home/${USER}/git-repos/Auto-DIG/ShellScripts/startAutoDIG.sh /bin
