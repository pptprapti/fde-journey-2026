vendor_spend = {
    "TCS": 120000,
    "Infosys": 80000,
    "Accenture": 150000,
    "Wipro": 70000
}

final_vendor = []

for vendor in vendor_spend:
    potential_vendor = vendor_spend[vendor]
    if potential_vendor > 100000:
        final_vendor.append(vendor)

print(f"The vendors spending more than 100000 are : {final_vendor}")