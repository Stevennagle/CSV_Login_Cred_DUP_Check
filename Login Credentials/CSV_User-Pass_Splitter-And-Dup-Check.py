#!/usr/bin/env python
# Nagls@' CSV Splitter and Dup Check

# This program 
# 0) takes a file of comma delimited usernames on the left and passwords on the right
# 1) Writes the usernames and passwords to 2 seperate files
# 2) Removes duplicates 

# Example run: User@deviceName> cd ~/Desktop/Main/holdMyCode/NewSplit
# > python ./CSV_User-Pass_Splitter-And-Dup-Check.py UserNamePasswordList.csv

import sys


def read_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    return lines


def split_lines(lines):
    left_side_username = []
    right_side_password = []
    for line in lines:
        parts = line.strip().split(',')
        left_side_username.append(parts[0])
        right_side_password.append(parts[1])
    return left_side_username, right_side_password


def write_user_file(output_user_file, left_side_username):
    with open(output_user_file, 'w') as file:
        for element in left_side_username:
            file.write(element + '\n')

def write_password_file(output_password_file, right_side_password):
    with open(output_password_file, 'w') as file:
        for element in right_side_password:
            file.write(element + '\n')


def remove_duplicates(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    unique_lines = sorted(set(lines))

    with open(output_file, 'w') as outfile:
        outfile.writelines(unique_lines)


def main():
    #get
    argumentsList = sys.argv
    input_file = sys.argv[1]
    output_user_file = 'split_users.txt'
    output_password_file = 'split_passwords.txt'

    #print
    lines = read_file(input_file)
    left_side_username, right_side_password = split_lines(lines)
    write_user_file(output_user_file, left_side_username)

    # comment this out to leave duplicates 
    remove_duplicates(output_user_file, output_user_file)

    write_password_file(output_password_file, right_side_password)
 
    # comment this out to leave duplicates 
    remove_duplicates(output_password_file, output_password_file)

if __name__ == '__main__':
    main()
