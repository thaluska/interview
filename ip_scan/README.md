# IP scanner

This script can be used for scanning one IP address or range of IP addresses for open ports.
Script is limited only for scanning these ports 20 21 22 25 53 80 443

For running scan for one IP you need to run the script as followed:
```bash
./ip_scanner 10.10.10.10
```
where you change the IP address to IP you want to scan.

Scanning IP range is limited to only one subnet and need to be defined as starting IP space ending IP ( 10.10.10.1 10.10.10.110 )
For running scan on IP address range, run script as followed:
```bash
./ip_scanner 10.10.10.1 10.10.10.100
```

Script will dislpay only ports which are open on scanned IP.
When you run script again on the same IP it will show result only if new ports where open or close on scanned IP.
