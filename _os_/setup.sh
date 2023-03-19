#file for OS commands and operations

#add wpa_supplicant.confg + ssh file to bootfs
#POWER ON
#tty x.x.x.x:22
#login with default pi - raspberry #If you were putting this on the internet you should change this password first

#sudo passwd root
#vim /etc/ssh/sshd_config
##PermitRootLogin prohibit-password -> PermitRootLogin yes
#sudo service ssh restart 

#=====> !!!!!!REMEMBER TO UNDO PermitRootLogin CHANGES AFTER A PROPER USER ACCOUNT HAS BEEN CONFIGURED!!!!!! <======
#Alternatively if you don't wish to use root you can use pi's sudo privs to setup a user account

#login as root
#adduser <params>/useradd <username> #Useradd is a perl script which uses the native adduser binary
#usermod -aG sudo <username>
#vim /etc/ssh/sshd_config
##Port 22 -> Port 2222
##PermitRootLogin yes -> PermitRootLogin prohibit-password
#service ssh restart
#confirm changes by trying to login as root


#Removing traces of pi user from system
#tty x.x.x.x:2222
#login to new user account
#sudo deluser pi
#sudo deluser -remove-home pi
#try su pi to confirm changes, also check filesystem if so inclined
#POWER OFF - It's not "secure" but this deters opportunistic attacks (those from bots)
