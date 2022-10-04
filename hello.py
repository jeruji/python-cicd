""" Hello world python """
import json

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
    "encrypt": "keygen"
}

jsonString = json.dumps(config)
jsonFile = open("config.json","w")
jsonFile.write(jsonString)
jsonFile.close()
