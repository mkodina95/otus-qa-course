import re
import time
import paramiko


host = '192.168.1.24'
user = 'marina'
secret = 'qwerty'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)

channel = client.invoke_shell()
channel.recv(9999)

# restart opencart server
channel.send('sudo reboot\n')
channel.send('qwerty\n')
channel.recv(9999)
time.sleep(60)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)

channel = client.invoke_shell()
channel.recv(9999)
time.sleep(2)

# restart mysql service
channel.send('sudo service mysql restart\n')
channel.send('qwerty\n')
channel.recv(9999)
time.sleep(2)

# check service status
channel.send("sudo service mysql status | grep ' active '\n")
time.sleep(2)
output = channel.recv(9999).decode("utf-8")

match = re.search(r'\(running\)', output)

if match is None:
    print("Not active")
else:
    res = match.group(0)
    if res is None or len(res) == 0:
        print("Not active")
    else:
        print("Active")


# restart apache2 service
channel.send('sudo service apache2 restart\n')
channel.recv(9999)
time.sleep(2)

# check service status
channel.send("sudo service apache2 status | grep ' active '\n")
time.sleep(2)
output = channel.recv(9999).decode("utf-8")

match = re.search(r'\(running\)', output)

if match is None:
    print("Not active")
else:
    res = match.group(0)
    if res is None or len(res) == 0:
        print("Not active")
    else:
        print("Active")


channel.close()
client.close()
