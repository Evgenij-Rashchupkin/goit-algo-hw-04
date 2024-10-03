def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    if len(args) < 2:
        return "Not enough informations. Use 'add username phone'"
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added successfully."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Not enough informations. Use 'add username phone'"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated successfully"
    else:
        return f"Contact {name} does not exist. Input another name"


def get_phone(args, contacts):
    if len(args) < 1:
        return "Not enough informations. Use 'phone username'"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        f"Contact {name} does not exist. Input another name"


def all(contacts):
    if contacts:
        return "\n".join([f"{name} >>> {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found"


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
