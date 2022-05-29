from colorama import Fore, init

init()

def print_color(txt, color):
    """
    txt - text to print
    color - red, green, normal
    """
    
    color_dict = {"red":Fore.RED, "green":Fore.GREEN, "normal":Fore.RESET}
    print(color_dict[color] + txt)
    return None
