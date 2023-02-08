'''
Copyright 2023 [Your Name or Company Name]

All rights reserved.

ZipCracker is a python script that brute-forces a password protected zip file by trying out passwords from a dictionary file. 
The dictionary file used in this script is 'rockyou.txt'. 
The name of the zipfile used in this script is 'enc.zip'.
The script will print the correct password once found, or inform that the password was not found in the list if all passwords have been tried.
'''

from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'rb') as f:
            for p in f:
                password = p.strip()
                if attempt_extract(zf, password):
                    print("[+] Correct password: %s" % password)
                    exit(0)
                else:
                    print("[-] Incorrect password: %s" % password)

    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
