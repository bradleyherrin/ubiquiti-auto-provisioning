#!/usr/bin/env python

# welcome-message-input-begin.py
# This project is authored by Bradley Herrin and Josh Moore.
# It is covered under the GPL-3.0 license.
# The goal of this project is to use Python to
# auto-provision Ubiquiti EdgeRouters and EdgeSwitches.
# View the full project on GitHub
# https://github.com/bradleyherrin/ubiquiti-auto-provisioning

def welcome_message():
        print("-------------------------------------\n".center(40))
        print("Welcome to the Ubiquiti EdgeMax\n".center(40))
        print("Auto-Provisioning Application\n".center(40))
        print("by Bradley Herrin\n".center(40))
        print("-------------------------------------\n".center(40))
        input("Press Enter/Return to begin... ")

welcome_message()
