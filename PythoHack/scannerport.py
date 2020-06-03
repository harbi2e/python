import socket

host = input("please enter the ip address: ")
#hostIP = socket.gethostbyname(host) تحويل رابط الموقع الى اي بي
try:
    for port in range(1,1000) :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host,port))
        if result == 0:
            print("[+] Port {}: Open.".format(port))
        else:
            print("[-]" Port {}: Closed.".format(port))
except:
    print("Pass")