import json

FILE_NAME = "contacts.json"

# ---------- Utility Functions ----------

def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# ---------- Contact Operations ----------

def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)


def display_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    for c in contacts:
        print(f"{c['name']} - {c['phone']}")


def update_contact(name, new_phone):
    contacts = load_contacts()
    for c in contacts:
        if c["name"].lower() == name.lower():
            c["phone"] = new_phone
            save_contacts(contacts)
            print("Contact updated successfully.")
            return
    print("Contact not found.")


# ---------- Example Usage ----------

add_contact("Ahmed Raza", "+923001234567")
add_contact("Maria Khan", "+923459876543")

display_contacts()

update_contact("Ahmed Raza", "+923000000000")
