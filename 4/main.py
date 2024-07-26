from contacts_handler import (
    add_contact,
    change_contact,
    get_contact,
    get_all_contacts,
)

COMMANDS = {
    "close": "Goodbye!",
    "exit": "Goodbye!",
    "hello": "How can I help you?",
    "all": get_all_contacts,
    "add": add_contact,
    "change": change_contact,
    "phone": get_contact,
}

def parse_input(user_input: str) -> tuple:
    try:
        cmd, *args = user_input.strip().lower().split(maxsplit=1)
        return cmd, args[0].split() if args else []
    except ValueError:
        return "", []

def handle_command(command: str, args: list, contacts: dict) -> None:
    if command in COMMANDS:
        if command in {"close", "exit", "hello"}:
            print(COMMANDS[command])
        elif command == "all":
            print(COMMANDS[command](contacts))
        else:
            print(COMMANDS[command](args, contacts))
    else:
        print("Invalid command.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        handle_command(command, args, contacts)
        if command in {"close", "exit"}:
            break

if __name__ == "__main__":
    main()
