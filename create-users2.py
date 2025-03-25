#!/usr/bin/python3

import os
import re
import sys

def main():
    """
    This script reads user details from an input file and creates Linux user accounts.
    It also assigns users to groups and sets their passwords.

    A dry-run mode is implemented to allow testing without making actual changes.
    """

    # Ask the user if they want to run in dry-run mode
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().lower() == 'y'

    for line in sys.stdin:
        # Skip lines that start with '#' (comments in the input file)
        if re.match("^#", line):
            if dry_run:
                print(f"Skipping commented line: {line.strip()}")  # Dry-run message
            continue

        # Split the line into fields (username, password, last_name, first_name, groups)
        fields = line.strip().split(':')

        # If the line does not have exactly 5 fields, skip it
        if len(fields) != 5:
            if dry_run:
                print(f"Skipping invalid line (missing fields): {line.strip()}")  # Dry-run message
            continue

        # Extract user details
        username = fields[0]
        password = fields[1]
        last_name = fields[2]
        first_name = fields[3]
        gecos = f"{first_name} {last_name},,,"
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")

        # Construct the command to create the user account
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run:
            print(f"Would run: {cmd}")  # Print the command instead of executing
        else:
            os.system(cmd)  # Execute the command

        print(f"==> Setting the password for {username}...")

        # Construct the command to set the password
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"

        if dry_run:
            print(f"Would run: {cmd}")  # Dry-run output
        else:
            os.system(cmd)  # Execute the command

        # Assign the user to groups if applicable
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"

                if dry_run:
                    print(f"Would run: {cmd}")  # Dry-run output
                else:
                    os.system(cmd)  # Execute the command

if __name__ == '__main__':
    main()

