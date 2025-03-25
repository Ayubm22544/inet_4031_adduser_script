#!/usr/bin/python3

# INET4031 - Automating User Creation Script
# Author: Ayubm22544
# Date Created: (Insert Date)
# Last Modified: (Insert Date)

# Import required libraries
import os   # Used to execute system commands like adding users and setting passwords
import re   # Used for regular expressions to filter input lines
import sys  # Used to read input from standard input (sys.stdin)

def main():
    """
    Reads user information from an input file (stdin), processes each line,
    and executes system commands to add users and assign them to groups.
    """

    for line in sys.stdin:

        # Check if the line is a comment (starts with '#') and skip it
        match = re.match("^#", line)

        # Strip newline characters and split the input line into fields using ':'
        # Expected format: username:password:last_name:first_name:groups
        fields = line.strip().split(':')

        # Skip processing if the line is a comment or doesn't have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user details from the input fields
        username = fields[0]  # Username for the new account
        password = fields[1]  # User's password
        # The gecos field stores the full name and additional information
        gecos = "%s %s,,," % (fields[3], fields[2])  # First Name, Last Name

        # Extract groups from the fifth field (comma-separated list of groups)
        groups = fields[4].split(',')

        # Informing the admin that a new user is being created
        print("==> Creating account for %s..." % (username))

        # Construct the system command to create a new user with disabled password login
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Uncomment the line below to execute the user creation command

        # Informing the admin that the user's password is being set
        print("==> Setting the password for %s..." % (username))

        # Construct the system command to set the user's password using `passwd` command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Uncomment the line below to execute the password setting command

        # Assign user to groups if applicable
        for group in groups:
            # Skip if the user does not need to be assigned to any group (indicated by '-')
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # Uncomment the line below to execute the group assignment command


# Run the script when executed directly
if __name__ == '__main__':
    main()
