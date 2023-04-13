from netmiko import ConnectHandler

sw={
    "device_type":"cisco_ios",
    "ip":"10.215.27.31",
    "username":"vnpro",
    "password":"vnpro#123",
    "secret":"vnpro#321"
}
net_connect= ConnectHandler(**sw)
net_connect.enable()
"""data= net_connect.send_command('show int')
print(data)"""

for n in range(10,31):
        CreateVlan=['vlan '+str(n)]
        ipvlan= ['int vlan '+ str(n),'ip add 172.16.'+str(n)+".1 255.255.255.0","no shutdown"]
        output=net_connect.send_config_set(CreateVlan)
        output=net_connect.send_config_set(ipvlan)
data= net_connect.send_command("show ip int brief | i Vlan")
print(data)

net_connect.disconnect()
