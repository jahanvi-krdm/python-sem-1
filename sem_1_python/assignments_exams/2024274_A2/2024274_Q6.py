def insert_entry(address_book, name, address, phone, email):
    if name in address_book:
        if any(entry['address'] == address and entry['phone'] == phone and entry['email'] == email for entry in address_book[name]):
            print("Entry already exists!")
        else:
            address_book[name].append({"address": address, "phone": phone, "email": email})
    else:
        address_book[name] = [{"address": address, "phone": phone, "email": email}]
    return address_book

def delete_entry(address_book, name, phone=None, email=None):
    if name in address_book:
        address_book[name] = [entry for entry in address_book[name] if (phone and entry['phone'] != phone) and (email and entry['email'] != email)]
        if not address_book[name]:
            del address_book[name]
        print(f"Deleted entry for {name}")
    else:
        print(f"No entries found for {name}")
    return address_book

def find_entry_by_name(address_book, partial_name):
    return {name: entries for name, entries in address_book.items() if partial_name.lower() in name.lower()}

def find_entry_by_phone_or_email(address_book, phone=None, email=None):
    results = {}
    for name, entries in address_book.items():
        for entry in entries:
            if (phone and entry['phone'] == phone) or (email and entry['email'] == email):
                results.setdefault(name, []).append(entry)
    return results

def save_to_file(address_book, filename):
    with open(filename, 'w') as file:
        for name, entries in address_book.items():
            file.write(f"{name}:\n")
            for entry in entries:
                file.write(f"{entry['address']}, {entry['phone']}, {entry['email']}\n")

def load_from_file(filename):
    address_book = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        name, entries = None, []
        for line in lines:
            line = line.strip()
            if ':' in line:
                if name: address_book[name] = entries
                name, entries = line[:-1], []
            else:
                address, phone, email = line.split(', ')
                entries.append({"address": address, "phone": phone, "email": email})
        if name: address_book[name] = entries
    return address_book

address_book = load_from_file('/Users/jahanvikardam/Desktop/J/2024274_A2/addr_book.txt')

address_book = insert_entry(address_book, "Lucy", "japan", "8888888888", "Lucyl@iiitd.ac.in")
address_book = insert_entry(address_book, "Ryan", "america", "9810000000", "ryan@hotmail.com")
address_book = insert_entry(address_book, "Lucy", "russia", "8979797979", "Lucy@gmail.com")
address_book = insert_entry(address_book, "Locky", "india", "8979782929", "Locky@gmail.com")

print(find_entry_by_name(address_book, "Lucy"))
print(find_entry_by_phone_or_email(address_book, phone="8979797979"))

address_book = delete_entry(address_book, "Ryan", phone="9810000000")

save_to_file(address_book, '/Users/jahanvikardam/Desktop/J/2024274_A2/addr_book.txt')