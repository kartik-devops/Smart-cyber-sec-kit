import scapy.all as scapy
from scapy.all import Ether , ARP , srp , sniff , conf

def getMacOfSender(ip):
    p = Ether(dst = 'ff:ff:ff:ff:ff:ff')/ARP(pdst = ip)
    result = srp(p , timeout=2 , verbose=False)[0]
    return result[0][1].hwsrc
    
    
def processPackets(packet):
    if(packet.haslayer(scapy.ARP) and  packet[ARP].op==2):
       
        print("[*]Arp packets have been detected")
        print("[+] Details are\n ")
        print(packet.show())
        try:

            real_mac = getMacOfSender(packet[ARP].psrc)
            response_mac = packet[ARP].hwsrc
            if (real_mac != response_mac):
                print("[!}Somebody Trying to Using Arp attack")
                print("Real Mac of attacker is :" ,realmac.upper()) 
                print("FAKE MAC used by attacker is :" ,response_mac.upper())
        except IndexError:
            print("NOTE : Attacker could use Fake IP Also")
            pass

def sniffPackets(interface):
    scapy.sniff(iface = interface , store= False , prn = processPackets , count=40)




print("Enter your Interface eth0 , wlan0 , tun0")
interface = input()
sniffPackets(interface)


