"""install and configure consul service discovery"""

import os
import subprocess
import json

os.system('sudo apt-get update -y')
os.system('sudo apt-get install unzip gnupg2 curl wget -y')
os.system('wget https://releases.hashicorp.com/consul/1.13.2/consul_1.13.2_linux_amd64.zip')
os.system('unzip consul_1.13.2_linux_amd64.zip')
os.system('sudo mv consul /usr/local/bin')
os.system('echo "consul version: "')
os.system('consul --version')

os.system('sudo groupadd --system consul')
os.system('sudo useradd -s /sbin/nologin --system -g consul consul')
os.system('sudo mkdir -p /var/lib/consul')
os.system('sudo mkdir /etc/consul.d')

os.system('sudo chown -R consul:consul /var/lib/consul')
os.system('sudo chmod -R 775 /var/lib/consul')
os.system('sudo chown -R consul:consul /etc/consul.d')

with open('/etc/systemd/system/consul.service','w') as f:
    lines = ["[Unit]\n","Description=Consul Service Discovery Agent\n","After=network-online.target\n","Wants=network-online.target\n",
    "[Service]\n","Type=simple\n","User=consul\n","Group=consul\n","ExecStart=/usr/local/bin/consul agent -server -ui -advertise=127.0.0.1 -bind=127.0.0.1 -data-dir=/var/lib/consul -node=consul-01 -config-dir=/etc/consul.d\n", "ExecReload=/bin/kill -HUP $MAINPID\n","KillSignal=SIGINT\n","TimeoutStopSec=5\n","Restart=on-failure\n","SyslogIdentifier=consul\n","[Install]\n","WantedBy=multi-user.target"]
    f.writelines(lines)
    f.close()

os.system('sudo systemctl daemon-reload')

keygen = subprocess.check_output("consul keygen", shell=True)

config = {
    "bootstrap": True,
    "server": True,
    "log_level": "DEBUG",
    "enable_syslog": True,
    "datacenter": "server1",
    "addresses" : {
    "http": "0.0.0.0"
    },
    "bind_addr": "127.0.0.1",
    "node_name": "ubuntu2004",
    "data_dir": "/var/lib/consul",
    "acl_datacenter": "server1",
    "acl_default_policy": "allow",
    "encrypt": keygen
}

jsonString = json.dumps(config)
jsonFile = open("/etc/consul.d/config.json","w")
jsonFile.write(jsonString)
jsonFile.close()


os.system('systemctl start consul')
os.system('systemctl enable consul')

os.system('echo "consul status: "')
os.system('systemctl status consul')
os.system('echo "consul run at http://127.0.0.1:8500/ui"')