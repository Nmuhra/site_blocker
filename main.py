from datetime import datetime

year = int(input("Year:\n"))
month = int(input("Month(number):\n"))
day = int(input("day:\n"))
hour = int(input("until when do you want your site to be blocked (24hr time):\n"))
end_time = datetime({year}, {month}, {day}, {hour})
site = str(input("Site to block: "))
sites_to_block = [f"{site}"]

hosts_path = str(input("host path: "))
path = hosts_path
redirect = "127.0.0.1"

def block_sites():
  if  datetime.now() < end_time:
    print("block sites")
    with open(path, "r") as hostsfile:
      hosts_content = hostsfile.read()
      for site in sites_to_block:
        if site not in hosts_content:
          hostsfile.write(redirect + "" + site + "n")
  else:
    print("unblock sites")
    with open(path, "r") as hostsfile:
      lines = hostsfile.readlines()
      hostsfile.seek(0)
      for line in lines:
        if not any(site in line for site in sites_to_block):
          hostsfile.write(line)
      hostsfile.truncate()
