# utils/display_formatter.py

from tabulate import tabulate

def get_signal_label(signal):
    """Convert dBm to a readable label with number and text."""
    label = get_signal_label_category(signal)
    return f"{signal} dBm ({label})"

def get_signal_label_category(signal):
    """Return only the category (used for filtering)."""
    if signal >= -50:
        return "Excellent"
    elif -60 <= signal < -50:
        return "Strong"
    elif -70 <= signal < -60:
        return "Moderate"
    elif -80 <= signal < -70:
        return "Weak"
    else:
        return "Very Weak"

def format_networks_as_table(networks):
    headers = ["No.", "SSID", "BSSID", "Signal Strength", "Channel", "Security"]
    table_data = []

    for idx, net in enumerate(networks, 1):
        table_data.append([
            idx,
            net["SSID"] if net["SSID"] else "<Hidden>",
            net["BSSID"],
            get_signal_label(net["Signal"]),
            net["Channel"],
            net["Security"]
        ])

    return tabulate(table_data, headers=headers, tablefmt="fancy_grid")
