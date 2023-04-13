from netmiko import ConnectHandler

router={
    "device_type":"cisco_ios",
    "ip":"10.215.27.32",
    "username":"vnpro",
    "password":"vnpro#123",
    "secret":"vnpro#321"
}
net_connect= ConnectHandler(**router)
net_connect.enable()
"""data= net_connect.send_command('show ip vrf int ')
print(data)"""
data = net_connect.send_command('show vrf brief | i ipv')
for vrflines in data.splitlines():
    vrfsplit=vrflines.split()
    
    if "4" in vrfsplit[3]:
        vrfipv4= net_connect.send_command("show ip route vrf "+ vrfsplit[0])
        print(vrfipv4)

"""data = net_connect.send_command("show ip route vrf Customer_A")
print(data)"""
net_connect.disconnect()
