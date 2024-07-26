def validate_args(args: list, expected_length: int) -> None:
    if len(args) != expected_length:
        raise ValueError(f"Exactly {expected_length} argument(s) are required.")

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact does not exist."
        except IndexError:
            return "Enter user name and phone."
        except Exception as e:
            return f"Error occurred: {type(e).__name__}, {e}"
    return inner

@input_error
def add_contact(args: list, contacts: dict) -> str:
    validate_args(args, 2)
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: list, contacts: dict) -> str:
    validate_args(args, 2)
    name, phone = args
    if name not in contacts:
        raise KeyError("Contact does not exist.")
    contacts[name] = phone
    return "Contact updated."

@input_error
def get_contact(args: list, contacts: dict) -> str:
    validate_args(args, 1)
    name = args[0]
    if name not in contacts:
        raise KeyError("Contact does not exist.")
    return contacts[name]

@input_error
def get_all_contacts(contacts: dict) -> str:
    if not contacts:
        return "Contacts are empty."
    contacts_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return f"Contacts:\n{contacts_list}"
