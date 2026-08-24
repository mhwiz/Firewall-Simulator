import os
import random
import time
import subprocess
import ipaddress

clsc = "cls" if os.name == "nt" else "clear"
subprocess.run(clsc, shell=True, check=True)


def generate_random_ip():
    networks = [
        ipaddress.ip_network("10.0.0.0/24"),
        ipaddress.ip_network("10.0.1.0/24"),
        ipaddress.ip_network("172.16.0.0/24"),
        ipaddress.ip_network("192.168.1.0/24")
    ]

    network = random.choice(networks)

    return str(random.choice(list(network.hosts())))


def check_firewall_rules(ip, rules):
    ip = ipaddress.ip_address(ip)

    for network, action in rules.items():
        if ip in network:
            return action

    return "allow"


def main():

    firewall_rules = {
        ipaddress.ip_network("10.0.0.0/24"): "allow",
        ipaddress.ip_network("10.0.1.0/24"): "block",
        ipaddress.ip_network("172.16.0.0/24"): "allow",
        ipaddress.ip_network("192.168.1.0/24"): "block"
    }

    for _ in range(100):

        ip_address = generate_random_ip()

        action = check_firewall_rules(
            ip_address,
            firewall_rules
        )

        random_number = random.randint(0, 9999)

        print(
            f"IP: {ip_address}, "
            f"Action: {action}, "
            f"OID: {random_number}"
        )

        time.sleep(1)


if __name__ == "__main__":
    main()