"""Create SSH Key for Github private repository"""

import os

os.system('su - jenkins')
os.system('ssh-keygen')