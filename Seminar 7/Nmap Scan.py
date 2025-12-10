import nmap

def nmap_scan(host, port_range='1-10'):
    nm = nmap.PortScanner()
    try:
        nm.scan(host, port_range, arguments='-sV')

        for host in nm.all_hosts():
            print(f"Host: {host} ({nm[host].hostname()})")
            print(f"State: {nm[host].state()}")

            for proto in nm[host].all_protocols():
                print(f"Protocol: {proto}")
                for port in sorted(nm[host][proto].keys()):
                    service = nm[host][proto][port]
                    print(
                        f"Port: {port}\tState: {service['state']}\t"
                        f"Service: {service.get('name', 'unknown')} "
                        f"{service.get('version', '')}"
                    )
    except Exception as e:
        print(f"Error: {e}")

# Localhost scan only
nmap_scan('127.0.0.1', '1-10')
