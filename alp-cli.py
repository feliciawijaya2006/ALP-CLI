import os
import shutil

# Function for ls
def list_files():
    for item in os.listdir():
        print(item)

# Function for pwd
def print_working_directory():
    print(os.getcwd())

# Function for cd
def change_directory(path):
    try:
        os.chdir(path)
        print(f"Changed directory to {os.getcwd()}")
    except FileNotFoundError:
        print("Directory not found!")

# Function for mkdir
def make_directory(name):
    try:
        os.mkdir(name)
        print(f"Directory '{name}' created.")
    except FileExistsError:
        print("Directory already exists.")

# Function for rmdir
def remove_directory(name):
    try:
        os.rmdir(name)
        print(f"Directory '{name}' removed.")
    except FileNotFoundError:
        print("Directory not found!")
    except OSError:
        print("Directory not empty or cannot be removed.")

# Function for touch
def create_file(name):
    try:
        with open(name, 'w') as f:
            pass
        print(f"File '{name}' created.")
    except Exception as e:
        print(f"Error: {e}")

# Function for rm
def remove_file(name):
    try:
        os.remove(name)
        print(f"File '{name}' removed.")
    except FileNotFoundError:
        print("File not found!")

# Function for cp
def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print(f"Copied '{src}' to '{dest}'.")
    except FileNotFoundError:
        print("Source file not found!")

# Function for mv
def move_file(src, dest):
    try:
        shutil.move(src, dest)
        print(f"Moved/Renamed '{src}' to '{dest}'.")
    except FileNotFoundError:
        print("Source file not found!")

# Function for help
def display_help():
    print("""
Available commands:
  ls          - List files and directories.
  pwd         - Print working directory.
  cd <path>   - Change directory.
  mkdir <name> - Create a new directory.
  rmdir <name> - Remove a directory (if empty).
  touch <name> - Create a new file.
  rm <name>    - Remove a file.
  cp <src> <dest> - Copy a file.
  mv <src> <dest> - Move or rename a file.
  clear       - Clear the terminal screen.
  exit        - Exit the CLI.
Additional commands:
  search <pattern> - Search for files or directories matching the pattern.
  tree        - Display directory structure in tree form.
  log <command> - Log command history to a file.
    """)

# Function for clear
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for exit
def exit_cli():
    print("Exiting CLI. Goodbye!")
    exit()

# Function for search
def search_files(pattern):
    for root, dirs, files in os.walk('.'):
        for name in dirs + files:
            if pattern in name:
                print(os.path.join(root, name))

# Function for tree
def display_tree(path='.'):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")

# Function for log
def log_command(command):
    with open("command_log.txt", "a") as log_file:
        log_file.write(command + "\n")
    print(f"Command '{command}' logged.")

# Main loop
def main():
    while True:
        command = input("cli> ").strip()
        log_command(command)
        parts = command.split()
        cmd = parts[0]

        if cmd == 'ls':
            list_files()
        elif cmd == 'pwd':
            print_working_directory()
        elif cmd == 'cd' and len(parts) > 1:
            change_directory(parts[1])
        elif cmd == 'mkdir' and len(parts) > 1:
            make_directory(parts[1])
        elif cmd == 'rmdir' and len(parts) > 1:
            remove_directory(parts[1])
        elif cmd == 'touch' and len(parts) > 1:
            create_file(parts[1])
        elif cmd == 'rm' and len(parts) > 1:
            remove_file(parts[1])
        elif cmd == 'cp' and len(parts) > 2:
            copy_file(parts[1], parts[2])
        elif cmd == 'mv' and len(parts) > 2:
            move_file(parts[1], parts[2])
        elif cmd == 'help':
            display_help()
        elif cmd == 'clear':
            clear_screen()
        elif cmd == 'exit':
            exit_cli()
        elif cmd == 'search' and len(parts) > 1:
            search_files(parts[1])
        elif cmd == 'tree':
            display_tree()
        elif cmd == 'log':
            print("Command logging enabled.")
        else:
            print("Invalid command. Type 'help' for the list of commands.")

if __name__ == "__main__":
    main()
