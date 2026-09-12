# scanner/wifi_scanner.py

import pywifi
from pywifi import const
import time

def scan_networks():
    wifi = pywifi.PyWiFi()              # Create Wi-Fi object
    iface = wifi.interfaces()[0]        # Select the first Wi-Fi adapter

    iface.scan()                        # Trigger scan
    time.sleep(3)                       # Wait for scan to complete

    results = iface.scan_results()      # Get results

    networks = []
    for network in results:
        networks.append({
            "SSID": network.ssid,
            "BSSID": network.bssid,
            "Signal": network.signal,    # Signal strength (higher is better)
            "Channel": network.freq,     # Frequency of the channel
            "Security": get_auth_type(network.akm)
        })

    return networks

def get_auth_type(akm_list):
    """Determine the type of security protocol used by the network."""
    if not akm_list:
        return "Open"
    if const.AKM_TYPE_WPA2PSK in akm_list:
        return "WPA2-PSK"
    if const.AKM_TYPE_WPAPSK in akm_list:
        return "WPA-PSK"
    return "Other"
