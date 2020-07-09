#!/usr/bin/env python
import os
import sys
def check_reboot():
    """returns if the computer needs a reboot"""
    return os.path.exists("/run/reboot-required") 

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everythings ok.")
    print("faith.")
    sys.exit(0)


main()