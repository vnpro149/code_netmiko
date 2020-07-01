from netmiko import ConnectHandler
from multiprocessing import Process
from device_list import device_list as devices
from ntc_templates.parse import parse_output
from pprint import pprint
def show_vlan(device):
    ssh=ConnectHandler(**device)
    ssh.enable()
    data=ssh.send_command("show vlan")
    data_parse=parse_output(platform="cisco_ios",command="show vlan",data=data)
    vlan={}
    ###vlan={"vlan_ID":"Interfaces"}
    for i in data_parse:
        vlan[i["vlan_id"]]=i["interfaces"]
    if "Et0/2" and "Et0/1" in vlan["1"]:
        print("vlan 1 da duoc gan cac cong tren")
    else:
        print("Vlan 1 chua duoc gan cac cong tren")
    #print("Day la du lieu duoi dang JSON")
    pprint(vlan)
    '''
    list_vlan=[]
    for i in data_parse:
        list_vlan.append(i["vlan_id"])
    if "1" in list_vlan:
       print("Da co vlan 10")
    else:
       print("chua co Vlan 10 , Dang tao vlan 10")
    '''      
    #pprint(data_parse)
    ssh.disconnect()
def main():
    #command=input("Nhap command muon chay: ")
    for device in devices:
        my_proc=Process(target=show_vlan,args=(device,))
        my_proc.start()
if __name__ == "__main__":
    main()
