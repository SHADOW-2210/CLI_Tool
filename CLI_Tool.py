import argparse
import os
import random
import datetime

def greet(name):
    """Greets the user."""
    print(f"Hello, {name}!")

def generate_password(length):
    """Generates a random password of a given length."""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

def list_files(directory):
    """Lists all files in a given directory."""
    try:
        files = os.listdir(directory)
        if not files:
            print(f"No files found in {directory}")
            return

        print(f"Files in {directory}:")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Error: Directory '{directory}' not found.")
    except NotADirectoryError:
        print(f"Error: '{directory}' is not a directory.")


def display_date_time():
    """Displays the current date and time."""
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def main():
    parser = argparse.ArgumentParser(description="A simple CLI tool.")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for greet
    greet_parser = subparsers.add_parser("greet", help="Greets the user")
    greet_parser.add_argument("name", help="Your name")

    # Subparser for generate_password
    password_parser = subparsers.add_parser("generate_password", help="Generates a random password")
    password_parser.add_argument("length", type=int, help="Length of the password")

    # Subparser for list_files
    list_files_parser = subparsers.add_parser("list_files", help="Lists files in a directory")
    list_files_parser.add_argument("directory", help="The directory to list")

     # Subparser for display_date_time
    date_time_parser = subparsers.add_parser("date_time", help="Displays the current date and time")


    args = parser.parse_args()

    if args.command == "greet":
        greet(args.name)
    elif args.command == "generate_password":
        password = generate_password(args.length)
        print(f"Generated password: {password}")
    elif args.command == "list_files":
        list_files(args.directory)
    elif args.command == "date_time":
        display_date_time()
    else:
        parser.print_help()  # If no command is provided, print help


if __name__ == "__main__":
    main()