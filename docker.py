"""Install docker"""

import os

os.system('sudo apt-get remove docker docker-engine docker.io')
os.system('sudo apt-get update')
os.system('sudo apt install docker.io -y')
os.system('sudo snap install docker')
os.system('docker --version')
os.system('sudo docker run hello-world')
os.system('sudo docker images')
os.system('sudo docker ps -a')
os.system('sudo docker ps')
os.system('sudo usermod -a -G docker jenkins')
