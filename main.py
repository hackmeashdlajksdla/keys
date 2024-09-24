import os
import requests

# Configuration
REPO_URL = "https://raw.githubusercontent.com/yourusername/yourrepo/main/main.py"  # URL to the latest version of the script
LOCAL_FILE = "main.py"

def get_latest_version():
    try:
        response = requests.get(REPO_URL)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the latest version: {e}")
        return None

def check_for_update():
    latest_version = get_latest_version()
    if latest_version is None:
        return False

    # Compare local and latest version
    with open(LOCAL_FILE, 'r') as local_file:
        local_version = local_file.read()

    if latest_version != local_version:
        print("Update available!")
        return True
    else:
        print("You are using the latest version.")
        return False

def update_script():
    latest_version = get_latest_version()
    if latest_version:
        with open(LOCAL_FILE, 'w') as local_file:
            local_file.write(latest_version)
        print("Update completed successfully.")

def main():
    if check_for_update():
        update_script()

    # Continue with the rest of your main program logic
    print("Running the main application...")

if __name__ == "__main__":
    main()
