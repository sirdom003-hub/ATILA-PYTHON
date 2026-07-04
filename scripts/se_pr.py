print("------catalog of electronics------")

electronics_catalog = {
    # Laptops (LPT)
    "LPT-001": {"name": "Apple MacBook Pro 16-inch", "price": 2499.00},
    "LPT-002": {"name": "Dell XPS 15", "price": 1899.99},
    "LPT-003": {"name": "Lenovo ThinkPad X1 Carbon", "price": 1499.50},
    "LPT-004": {"name": "HP Spectre x360", "price": 1399.00},
    "LPT-005": {"name": "Asus ROG Zephyrus G14", "price": 1599.99},
    "LPT-006": {"name": "Acer Swift 3", "price": 799.00},
    "LPT-007": {"name": "Microsoft Surface Laptop 5", "price": 1299.00},
    "LPT-008": {"name": "Razer Blade 15", "price": 2299.99},
    
    # Smartphones (SMP)
    "SMP-001": {"name": "Apple iPhone 15 Pro Max", "price": 1199.00},
    "SMP-002": {"name": "Samsung Galaxy S24 Ultra", "price": 1299.99},
    "SMP-003": {"name": "Google Pixel 8 Pro", "price": 999.00},
    "SMP-004": {"name": "OnePlus 12", "price": 799.99},
    "SMP-005": {"name": "Sony Xperia 1 V", "price": 1198.00},
    "SMP-006": {"name": "Motorola Edge Plus", "price": 799.00},
    "SMP-007": {"name": "Asus ROG Phone 8", "price": 1099.99},
    
    # Tablets (TBL)
    "TBL-001": {"name": "Apple iPad Pro 12.9", "price": 1099.00},
    "TBL-002": {"name": "Samsung Galaxy Tab S9 Ultra", "price": 1199.99},
    "TBL-003": {"name": "Microsoft Surface Pro 9", "price": 999.00},
    "TBL-004": {"name": "Lenovo Tab P12 Pro", "price": 699.99},
    "TBL-005": {"name": "Amazon Fire HD 10", "price": 149.99},
    
    # Wearables & Smartwatches (WTC)
    "WTC-001": {"name": "Apple Watch Series 9", "price": 399.00},
    "WTC-002": {"name": "Apple Watch Ultra 2", "price": 799.00},
    "WTC-003": {"name": "Samsung Galaxy Watch 6 Classic", "price": 399.99},
    "WTC-004": {"name": "Garmin Fenix 7 Pro", "price": 799.99},
    "WTC-005": {"name": "Fitbit Charge 6", "price": 159.95},
    "WTC-006": {"name": "Amazfit GTR 4", "price": 199.00},
    
    # Audio & Headphones (AUD)
    "AUD-001": {"name": "Apple AirPods Pro 2", "price": 249.00},
    "AUD-002": {"name": "Sony WH-1000XM5", "price": 398.00},
    "AUD-003": {"name": "Bose QuietComfort Ultra", "price": 429.00},
    "AUD-004": {"name": "Sennheiser Momentum 4", "price": 349.95},
    "AUD-005": {"name": "Beats Studio Pro", "price": 349.99},
    "AUD-006": {"name": "JBL Flip 6 Portable Speaker", "price": 129.95},
    "AUD-007": {"name": "Sonos Roam Smart Speaker", "price": 179.00},
    "AUD-008": {"name": "Ultimate Ears Megaboom 3", "price": 199.99},
    
    # Cameras (CAM)
    "CAM-001": {"name": "Sony Alpha A7 IV", "price": 2498.00},
    "CAM-002": {"name": "Canon EOS R6 Mark II", "price": 2499.00},
    "CAM-003": {"name": "Nikon Z6 II", "price": 1996.95},
    "CAM-004": {"name": "Fujifilm X-T5", "price": 1699.00},
    "CAM-005": {"name": "GoPro HERO12 Black", "price": 399.99},
    "CAM-006": {"name": "DJI Osmo Action 4", "price": 299.00},
    
    # Televisions (TV)
    "TV-001": {"name": "LG C3 OLED 65-inch", "price": 1699.99},
    "TV-002": {"name": "Samsung S90C OLED 65-inch", "price": 1599.99},
    "TV-003": {"name": "Sony A80L OLED 65-inch", "price": 1799.99},
    "TV-004": {"name": "TCL 6-Series Mini-LED 65-inch", "price": 799.00},
    "TV-005": {"name": "Hisense U8K Mini-LED 65-inch", "price": 899.99},
    
    # Gaming Consoles (CON)
    "CON-001": {"name": "Sony PlayStation 5", "price": 499.99},
    "CON-002": {"name": "Microsoft Xbox Series X", "price": 499.99},
    "CON-003": {"name": "Nintendo Switch OLED", "price": 349.99},
    "CON-004": {"name": "Valve Steam Deck OLED", "price": 549.00},
    "CON-005": {"name": "Asus ROG Ally", "price": 699.99},
    "CON-006": {"name": "Meta Quest 3 VR Headset", "price": 499.99},
    
    # Networking & Routers (NET)
    "NET-001": {"name": "Netgear Orbi AX6000 Mesh", "price": 699.99},
    "NET-002": {"name": "Amazon eero Pro 6E", "price": 549.00},
    "NET-003": {"name": "TP-Link Deco XE75", "price": 399.99},
    "NET-004": {"name": "Asus ROG Rapture GT-AX11000", "price": 449.00},
    
    # Smart Home (SMH)
    "SMH-001": {"name": "Amazon Echo Dot (5th Gen)", "price": 49.99},
    "SMH-002": {"name": "Google Nest Hub Max", "price": 229.00},
    "SMH-003": {"name": "Philips Hue White and Color Starter Kit", "price": 199.99},
    "SMH-004": {"name": "Ring Video Doorbell Pro 2", "price": 249.99},
    "SMH-005": {"name": "Ecobee Smart Thermostat Premium", "price": 249.99}
}

print()



# --- Exemplo de como acessar e iterar sobre os dados ---

# Acessar um produto específico pelo código
print("Produto específico:")
print(electronics_catalog["LPT-001"]["name"])  # Saída: Apple MacBook Pro 16-inch
print(f"${electronics_catalog['LPT-001']['price']}\n") # Saída: $2499.0

# Iterar sobre todos os produtos e imprimir formatado
print("Catálogo Completo:")
for code, details in electronics_catalog.items():
    print(f"Code: {code} | Product: {details['name']} | Price: ${details['price']:.2f}")