import sys
import vymgmt

def main(argv):
    firewalls = []
    blocked = []

    with open(argv[0]) as file:
        firewalls = file.readlines()

    with open(argv[1]) as file:
        blocked = file.readlines()
    
    for firewall in firewalls:
        vyos = vymgmt.Router(firewall, 'vyos', password='vyos', port=22)

        vyos.login()
        vyos.configure()

        for ip in blocked:
            vyos.set("firewall group address-group BLOCKED address " + ip)
        
        vyos.commit()
        vyos.save()
        vyos.exit()
        vyos.logout()

if __name__ == "__main__":
   main(sys.argv[1:])
