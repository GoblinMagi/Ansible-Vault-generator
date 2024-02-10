# Ansible Vault Secret Generator
This simple script creates an Ansible Vault secret variable for use within Ansible playbooks and variable files.

The script will first prompt you for the string you wish to encrypt, then you will be prompted for the variable name for the encrypted data. Ansible will ask for Vault password for the encrypted string.

The output of this script can then be redirected into your YAML files.

## TODOS:
- [ ] Support for additional args
- [ ] Support for vault IDs
- [ ] Support for password files
