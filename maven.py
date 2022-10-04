"""Install Maven"""

import os

os.system('sudo apt update')
os.system('sudo apt install maven -y')
os.system('echo "Maven Version:"')
os.system('mvn -version')