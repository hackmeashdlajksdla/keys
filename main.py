import sys
import os
import platform
import requests

UTIL_FOLDER = "util"
GITHUB_KEY_URL = "https://raw.githubusercontent.com/hackmeashdlajksdla/keys/refs/heads/main/README.md"  # Replace with actual URL

def clear():
    if platform.system() == 'Windows':
        os.system('cls & title gdk nuker')
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('clear')

def open_info_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "info.py"))

def open_login_py():
    os.system(sys.executable + " " + os.path.join(UTIL_FOLDER, "login.py"))


def get_valid_keys():
    try:
        response = requests.get(GITHUB_KEY_URL)
        response.raise_for_status()
        # Split by lines and strip whitespace
        return [line.strip() for line in response.text.splitlines() if line.strip()]
    except Exception as e:
        print(f"Error fetching keys: {e}")
        return []

def check_key(key):
    valid_keys = get_valid_keys()
    return key in valid_keys

def input_key():
    key = input("Please input your key: ")
    if check_key(key):
        print_banner()  # Print banner if the key is valid
        return True
    else:
        print("Invalid key. Exiting.")
        sys.exit()

def print_banner():
    print("""                              
██╗███╗   ██╗████████╗███████╗██╗     ██╗     
██║████╗  ██║╚══██╔══╝██╔════╝██║     ██║     
██║██╔██╗ ██║   ██║   █████╗  ██║     ██║     
██║██║╚██╗██║   ██║   ██╔══╝  ██║     ██║     
██║██║ ╚████║   ██║   ███████╗███████╗███████╗
╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝╚══════╝""")
    print("<:intell is made bye jack:>")
    print(""" 
1:login
2:info
""")
    choice = input("Enter choice here: ")

    clear()

    if choice == '1':
        open_login_py()
    elif choice == '2':
        open_info_py()

# Clear the console and prompt for the key
clear()
input_key()
