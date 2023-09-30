import argparse
import os
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Run script and/or tests.')
    parser.add_argument('commands', nargs='*', help='Commands to run')

    args = parser.parse_args()

    valid_commands = ['script', 'test']

    if not args.commands or not all(command in valid_commands for command in args.commands):
        print("Please specify 'script' and/or 'test' as arguments to run the corresponding parts.")
        return

    if 'test' in args.commands:
        print("Running test.py...")
        subprocess.run(["python3", "-m", "unittest", "test.py"])

    if 'script' in args.commands:
        print("Running script.py...")
        subprocess.run(["python3", "script.py"])

if __name__ == "__main__":
    main()