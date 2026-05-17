import json

with open("cops.json","r") as f:
    cops = json.load(f)

def show_all_cops():
    for cop in cops:
        print(f"Name: {cop['name']} | Type: {cop['type']} | Region: {cop['region']}")

def filter_by_type(cop_type):
    for cop in cops:
        if cop['type'].lower() == cop_type.lower():
            print(f"Name: {cop['name']} | Type: {cop['type']} | Region: {cop['region']}")

def filter_by_region(region):
    for cop in cops:
        if cop['region'].lower() == region.lower():
            print(f"Name: {cop['name']} | Type: {cop['type']} | Region: {cop['region']}")

def show_crates(cop_name):
    for cop in cops:
        if cop['name'] == cop_name:
            if len(cop['loot_crates']) == 0:
                print(f"No crates recoreded for {cop['name']}")
            else:
                print(f"\n---Crates at {cop['name']}---")
                for crate in cop['loot_crates']:
                    print(f" Location: {crate['location_note']} | Tier: {crate['tier']}")

def main():
    while True:
        print("\n--- GrayZone COP Tracker---")
        print("1. Show All COPs")
        print("2.Filter by Type")
        print("3.Filter by Region")
        print("4.Show crates for a COP")
        print("5.Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_all_cops()
        elif choice == "2":
            cop_type = input("Enter Type (Major or Minor): ").strip().lower()
            filter_by_type(cop_type)
        elif choice == "3":
            region = input(" Enter Region: ").strip().lower()
            filter_by_region(region)
        elif choice == "4":
            cop_name = input("Enter COP name: ")
            show_crates(cop_name)
        elif choice == "5":
            print("Exiting tracker.")
            break
        else:
            print("Invalid choice, try again.")

main()