""" Install JDK 11 and Jenkins in Ubuntu Server """

import os

os.system('sudo apt update')
os.system('sudo apt-get install openjdk-11-jdk-headless')
os.system('wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key |sudo gpg --dearmor -o /usr/share/keyrings/jenkins.gpg')
os.system("sudo sh -c 'echo deb [signed-by=/usr/share/keyrings/jenkins.gpg] http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'")
os.system('sudo apt update')
os.system('sudo apt install jenkins')
os.system('sudo systemctl start jenkins.service')
os.system('sudo systemctl status jenkins')
os.system('echo "--------------------------------"')
os.system('echo "Default jenkins password"')
os.system('sudo cat /var/lib/jenkins/secrets/initialAdminPassword')
