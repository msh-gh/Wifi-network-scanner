# main.py

from scanner.wifi_scanner import scan_networks
from utils.display_formatter import format_networks_as_table, get_signal_label_category

def main():
    print("📡 Wi-Fi Network Scanner\n")

    # Ask for signal strength filter
    print("🔍 Filter Options:")
    print("1. Excellent")
    print("2. Strong")
    print("3. Moderate")
    print("4. Weak")
    print("5. Very Weak")
    print("6. No Filter")
    choice = input("Choose signal strength filter (1-6): ")

    signal_category = {
        "1": "Excellent",
        "2": "Strong",
        "3": "Moderate",
        "4": "Weak",
        "5": "Very Weak",
        "6": None
    }.get(choice.strip(), None)

    # Ask whether to show hidden SSIDs
    show_hidden_input = input("Show hidden networks? (y/n): ").strip().lower()
    show_hidden = show_hidden_input == "y"

    print("\n🔄 Scanning nearby Wi-Fi networks...\n")
    networks = scan_networks()

    # Apply filters
    filtered = []
    for net in networks:
        strength_label = get_signal_label_category(net["Signal"])
        is_hidden = not bool(net["SSID"])

        if signal_category and strength_label != signal_category:
            continue
        if not show_hidden and is_hidden:
            continue
        filtered.append(net)

    if filtered:
        print(f"✅ Showing {len(filtered)} network(s) matching your filter:\n")
        print(format_networks_as_table(filtered))
    else:
        print("❌ No networks found matching the criteria.")

if __name__ == "__main__":
    main()
