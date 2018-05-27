from paramiko import SSHClient
from scp import SCPClient
import os, json


#в json указываем место на сервере, куда поместить файл -- место файла в локальной системе
data = 0
with SCPClient(ssh.get_transport()) as scp:
        try:
        	with open("data.json", "r") as external:
        		data = json.load(external)
        except FileNotFoundError:
        	    print("json does not exists")
        if data != 0:
        	while True:			
    			try:
        			file_config = data.popitem() #дает кортеж из файла и параметров сервера 
        			ssh = SSHClient() 			 #file : [server, user, pass, path]
					ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
					ssh.connect(file_config[1][0], username=file_config[1][1], password=file_config[1][2])
               		scp.put(file_config[0], file_config[1][3])
    			except KeyError:
        			print("json is empty")
        			break
        else:
        	print("the data has not been loaded")
        	
        	
        	
        	

