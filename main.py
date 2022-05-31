from utils.main_menu import *
from utils.display import print_color    

if __name__ == "__main__":
    flag, opt = True, None
    while flag:
        # functions from utils.main_menu
        clear_screen()
        print_main_menu()
        opt = input("Enter Choice: ")
        flag = check_main_opt(opt)

    print_color("credit", "green")
    print_color("debit", "red")
    print_color("some text", "normal")

