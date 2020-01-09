#!/bin/bash

#       Michael Himes
#       Jan 09 2020

#This script is used to populate ssh keys on the specified remote system with the current users name.

#Intended use:
#             Establish alias as sn
#             Example: sn 8.8.8.8 

#NOTE:
#       Current user must be present on the server that is being connected to.
#       This includes Centrify (AD)

#  Generate ssh key if none present
if [ ! -f  ~/.ssh/id_rsa ]; then
        ssh-keygen
fi


ssh-copy-id $USER@$1 >> ~/.ssh_copy_id_output 2>&1

#  Test if key has been established
if [[ `cat ~/.ssh_copy_id_output` == *"WARNING: All keys were skipped because they already exist on the remote system."* ]]; then

#  Key present on server with username
        rm ~/.ssh_copy_id_output
        ssh -o StrictHostKeyChecking=no $USER@$1; # Connect to remote system
else
#  Key not present on server with username
        ssh-copy-id $USER@$1 >> .ssh_copy_id_output 2>&1 # Copy key to remote system as current user
        rm ~/.ssh_copy_id_output
        ssh -o StrictHostKeyChecking=no $USER@$1; # Connect to remote system
fi
