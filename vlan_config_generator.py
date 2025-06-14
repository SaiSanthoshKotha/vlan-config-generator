# VLAN Config Generator for Cisco Devices

def generate_vlan_config(vlans):
    config_lines = []
    for vlan_id, vlan_name in vlans.items():
        config_lines.append(f"vlan {vlan_id}")
        config_lines.append(f" name {vlan_name}")
        config_lines.append("!")
    return "\n".join(config_lines)

if __name__ == "__main__":
    # Sample VLAN input
    vlan_data = {
        10: "Users",
        20: "Voice",
        30: "Management",
        40: "Guests"
    }

    config = generate_vlan_config(vlan_data)

    # Save to file
    with open("vlan_config.txt", "w") as f:
        f.write(config)

    print("✅ VLAN config generated and saved to vlan_config.txt")
