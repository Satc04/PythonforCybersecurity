#!/usr/bin/env python3
# Sample script that writes to a file
# By satveer 4/25

# Open file for writing
test_file = open("hackme.txt", "w")

# Ask user for name
user_name = input ("what is your name? ")
user_name = input ("what is your favorite color? ")
user_name = input ("what was your first pet's name? ")
user_name = input ("what is your mother's maiden name? ")
user_name = input ("what elementary school did you attend? ")
# write lines to the file
test_file.write(f"Hello {user_name}\n")
test_file.write("Hello {0}\n".format(user_name))
test_file.write("Hello " + user_name + "\n")

# Close teh file
test_file.close()



