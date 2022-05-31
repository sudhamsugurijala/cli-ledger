from os import name, system

def clear_screen():
    _ = system("clear") if name == "posix" else system("cls")
    return None


def print_main_menu():
    print("System Active. Please specify your choice from options below\n")
    print("1. Record Expense (Debit) \n2. Record Income (Credit)")
    print("(press any other key to save and exit)\n")
    return None


def check_main_opt(option):
    safe_opts = ['1', '2']
    if option in safe_opts:
        return True
    
    return False
