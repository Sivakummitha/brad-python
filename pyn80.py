ip = input("Enter IP address: ")
parts = ip.split(".")
new_ip = ".".join(str(int(p)) for p in parts)
print("IP address without leading zeros:", new_ip)
