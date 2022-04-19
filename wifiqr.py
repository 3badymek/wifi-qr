import pyqrcode
import sys

### requirement packages ##
# pip install pyqrcode
# pip install pypng
###########################

#if no output provided
if len(sys.argv) < 2:
    print ("Usage: pyton3 wifiqr.py [network SSID] [password]")
    quit()

#set network SSID name
network = sys.argv[1]

#set the value of WIFI network
if len(sys.argv) > 2:
    protocol = "WPA/WPA2"
    pwd = sys.argv[2]
else:
    protocol = "nopass"
    pwd = ""

qr = pyqrcode.create(f"WIFI:S:{network};T:{protocol};P:{pwd};;")

png = qr.png(f"{network}.png", scale=5)
