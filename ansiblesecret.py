#! /usr/bin/env python3
import pyinputplus as pyip
import subprocess

print("Enter string to encrypt:",end=" ")
vault_pass = pyip.inputPassword()
print("Enter variable name:",end=" ")
var_name = input()

subprocess.run(['ansible-vault','encrypt_string',vault_pass,'--name',var_name])

#TODO: Support for additional args
#TODO: Support for vault IDs
#TODO: Support for password files
