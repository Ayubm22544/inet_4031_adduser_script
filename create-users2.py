#!/usr/bin/python3

import os
import re
import sys

def main():
    """
    Reads user information from an input file (sys.stdin), processes each line,
    and executes system commands to add users and assign them to groups.
    """

    # Ask the user if they want to run in dry-run mode
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().lower() == 'y'

    for line in sys.stdin:

        # Check if the line is a comment (starts with '#') and skip it
        if re.match("^#", line):
            if dry_run:
                print(f"Skipping commented line: {line.strip()}")
            continue

        # Remove spaces/newlines and split by ':'
        fields = line.strip().split(':')

        # Ensure the line has exactly 5 fields; otherwise, skip
        if len(fields) != 5:
            if dry_run:
                print(f"Skipping invalid line (missing fields): {line.strip()}")
            continue

        # Extract user details
        username = fields[0]
        password = fields[1]
        last_name = fields[2]
        first_name = fields[3]
        gecos = f"{first_name} {last_name},,,"
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")

        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run:
            print(f"Would run: {cmd}")
        else:
            os.system(cmd)

        print(f"==> Setting the password for {username}...")

        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_run:
            print(f"Would run: {cmd}")
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                
                if dry_run:
                    print(f"Would run: {cmd}")
                else:
                    os.system(cmd)

if __name__ == '__main__':
    main()
