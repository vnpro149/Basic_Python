# Devnet
![bannergiangdayPython-01](https://user-images.githubusercontent.com/129259654/230593624-41fdd224-f834-48ad-bd2f-247cef11868a.jpg)

Link đăng kí tham gia: [tại đây](https://docs.google.com/forms/d/e/1FAIpQLSeJPTaFc8x4RqA6Kwc2-AUMopM1hJetPzlswxABluLZi-_bug/viewform?usp=share_link)

# Sơ đồ mạng

![image](https://user-images.githubusercontent.com/129259654/231654866-dbef501a-df78-4ff6-b94d-1c2aa52e8386.png)

# Cài đặt thư viện Netmiko

pip3 install netmiko

# Import thư viện và khai báo biến thuộc tính thiết bị

```
from netmiko import ConnectHandler # Import phương thức ConnectHandler trong thư viện Netmiko

  sw={

     "device_type":"cisco_ios", # Loại thiết bị
    
     "ip":"10.215.27.32", # IP của thiết bị
    
     "username":"vnpro", # Username truy cập SSH vào thiết bị
    
     "password":"vnpro#123", # Password truy cập SSH vào thiết bị
    
     "secret":"vnpro#321" # Secret cấu hình trên thiết 
      
  } 
```

# Kết nối và ngắt kết nối
```

net_connect=ConnectHandler(**sw) # Tạo kết nối đến thiết bị

net_connect.enable() # giữ kết nối ở mode Privileged

net_connect.disconnect() # Ngắt kết nối đến  thiết bị
```

# Phương thức gửi câu lệnh đến thiết bị
```

data= net_connect.send_command("show int") # Gửi câu lệnh ở mode Privileged

output=net_connect.send_config_set("vlan 10") #gửi câu lệnh ở mode Config
```

# Lab: Sử dụng Python quản lý, cấu hình Vlan10-30
```

for n in range (10,31):

    CreateVlan=['vlan '+str(n)] # tạo VLan
    
    ipVlan=['int vlan '+str(n),'ip add 172.16.'+str(n)+'.1 255.255.255.0','no shutdown'] # cấu hình địa chỉ ip cho interface VLan
    
    output= net_connect.send_config_set(CreateVlan) 
    
    output= net_connect.send_config_set(ipVlan)
    
    
output= net_connect.send_command('show ip interface brief | i Vlan') #in ra tất cả các vlan đã tạo

print(output)
```
![image](https://user-images.githubusercontent.com/129259654/231666121-9e4b48cb-2e85-4501-bbaa-1a951b808c49.png)


Thực thi file:

```
python3 demo_netmiko.py
```

# Lab:Sử dụng Python in các bảng định tuyến trên router
- In trạng thái hiện tại của tất cả các interface chỉ định trong VRF
```

data= net_connect.send_command('show ip vrf int ')

print(data)
```
Kết quả:

![image](https://user-images.githubusercontent.com/129259654/231663865-a67f1e09-3e64-4d7c-93e5-4a986efc3e3e.png)

- In trạng thái hiện tại của tất cả VRF
```
data = net_connect.send_command('show vrf brief | i ipv')

print(data)
```
Kết quả:
![image](https://user-images.githubusercontent.com/129259654/231664023-d7d216f5-4d13-4cbd-bfb2-c741858a2e23.png)

- In ra chi tiết từng bảng định tuyết trong VRF

```
for vrflines in data.splitlines(): # cắt chuỗi trả về theo dòng và lấy lần lượt từng giá trị

    vrfsplit=vrflines.split() # cắt chuỗi theo ký tự trống
    
    vrfipv4= net_connect.send_command("show ip route vrf "+ vrfsplit[0]) # gửi câu lệnh in ra bảng định tuyến với tên bảng ở index 0
    
    print(vrfipv4)
```  
Kết quả:

 ![image](https://user-images.githubusercontent.com/129259654/231664697-2e0e2afb-cfa9-48cc-8eff-8512644b9971.png)

Thực thi file:
```
python3 showrouting.py
```
