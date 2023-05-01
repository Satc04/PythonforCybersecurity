#!/usr/bin/env python3
# Sample script that reads from a file
# By satveer 4/25

# open file for reading
test_file = open("hackme.txt", "r")

# Read contents and print
file_contents = test_file.read()
print(file_contents)

# Close file
test_file.close()