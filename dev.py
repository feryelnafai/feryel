from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22,
}

def main():
    connexion = ConnectHandler(**device)

    # 1) show clock
    print("=== DATE DU ROUTEUR ===")
    print(connexion.send_command("show clock"))

    # 2) Save interfaces
    print("\n=== SAUVEGARDE DES INTERFACES ===")
    interfaces = connexion.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)
    print("Interfaces enregistrées dans interfaces.txt")

    # 3) Configure loopback
    print("\n=== CONFIGURATION DE LOOPBACK ===")
    config_commands = [
        #"config t"
        "interface Loopback10",
        "ip address 10.10.10.10 255.255.255.240",
        "commit",
    ]
    conn = connexion.send_config_set(config_commands)
    print(conn)
    print("Loopback configurée avec succès.")
  
connexion.disconnect()

if __name__ == "__main__":
    main()
