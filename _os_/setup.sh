#Will consist of any major chages to base OS
#For example disabling Wireless and using other bare metal RF for communication

#add wpa_supplicant.confg + ssh file to bootfs
#POWER ON
#tty x.x.x.x:22

#sudo passwd root
#vim /etc/ssh/sshd_config
##PermitRootLogin prohibit-password -> PermitRootLogin yes
#sudo service ssh restart 

#=====> !!!!!!REMEMBER TO UNDO PermitRootLogin CHANGES AFTER A PROPER USER ACCOUNT HAS BEEN CONFIGURED!!!!!! <======
#Alternaitvely if you don't wish to use root you can use raspberry's sudo privs to setup a user account

#adduser <params>/useradd <username> #Useradd is a perl script which uses the native adduser binary
#usermod -aG sudo <username>
#vim /etc/ssh/sshd_config
##Port 22 -> Port 2222
##PermitRootLogin yes -> PermitRootLogin prohibit-password
#service ssh restart
