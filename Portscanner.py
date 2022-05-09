import nmap

target = input("Enter your target : ")

scanvar = nmap.PortScanner()

for ports in range(0,100):
    result  = scanvar.scan(target , str(ports))
    result  = result['scan'][target]['tcp'][ports]['state']
    print(f'Port {ports} is {result}')
