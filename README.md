# 📡 Wi-Fi Network Scanner (Python)

A simple and customizable Wi-Fi Network Scanner built with Python that detects nearby wireless networks, displays their details like signal strength, security type, and allows user-defined filtering.

---

## 🚀 Features

- 🔍 Scan nearby Wi-Fi networks
- 📶 Display signal strength with labels: Excellent, Strong, Moderate, Weak, Very Weak
- 🛡️ Show network security type (Open, WPA2, etc.)
- 📡 Show/hide hidden SSIDs
- 🎯 Filter by signal strength category
- ❌ Remove duplicate SSID entries
- 🧠 Beginner-friendly and industry-ready code structure

---

## 🛠️ Requirements

- Python 3.7+
- Platform: Linux / Windows

### 📦 Python Libraries
Install dependencies using:

```bash
pip install pywifi tabulate


📁 Folder Structure
---------------------------
wifi-scanner/
│
├── main.py                      # Main program (entry point)
├── scanner/
│   └── wifi_scanner.py          # Scans and returns Wi-Fi network data
├── utils/
│   └── display_formatter.py     # Signal strength labels, formatting, filtering
├── README.md                    # Project documentation


⚙️ How to Run
--------------------
python main.py

Follow the on-screen prompts to:
Filter by signal strength category (Excellent to Very Weak)
Choose to display or hide hidden networks

🖼️ Sample Output

📡 Wi-Fi Network Scanner

🔍 Filter Options:
1. Excellent
2. Strong
3. Moderate
4. Weak
5. Very Weak
6. No Filter
Choose signal strength filter (1-6): 2
Show hidden networks? (y/n): n

🔄 Scanning nearby Wi-Fi networks...

✅ Showing 2 network(s) matching your filter:

╒════╤═════════════╤══════════════════════╤════════════════════════════╤══════════╤════════════╕
│ No │ SSID        │ BSSID               │ Signal Strength             │ Channel  │ Security   │
╞════╪═════════════╪══════════════════════╪════════════════════════════╪══════════╪════════════╡
│ 1  │ HomeNet     │ 00:11:22:33:44:55   │ -48 dBm (Excellent)         │ 2412     │ WPA2-PSK   │
│ 2  │ MyWiFi      │ AA:BB:CC:DD:EE:FF   │ -62 dBm (Moderate)          │ 2437     │ Open       │
╘════╧═════════════╧══════════════════════╧════════════════════════════╧══════════╧════════════╛


🧠 Concepts Used
---------------------
pywifi: Cross-platform Wi-Fi interface for Python
tabulate: Pretty-printing tabular data in terminal
subprocess: Interface with OS tools (optional fallback)
Signal strength interpretation (dBm → categories)
Clean code structure with modular design



🧑‍💻 Author
Name: MSH

Internship Project: Wi-Fi Scanner using Python
Task 8 at Tamizham Skills Internship



