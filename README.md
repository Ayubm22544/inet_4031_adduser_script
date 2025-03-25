# Automated User Creation Script

## Overview
This Python script automates the process of adding multiple users and assigning them to groups on a Linux system. It reads user information from an input file and executes the necessary system commands to create accounts, set passwords, and assign groups.

## Features
- Reads user details from an input file (`create-users.input`)
- Automatically creates user accounts
- Assigns users to specified groups
- Skips commented or improperly formatted lines
- Supports dry-run mode for testing

## Prerequisites
- A Linux-based system with `adduser` and `passwd` commands available
- Python 3 installed

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/Ayubm22544/inet_4031_adduser_script.git
cd inet_4031_adduser_script
