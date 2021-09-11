import requests
import json
import sys
import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-u", "--username", help="Enter the username you want to search")
group.add_argument("-f", "--file", help="Enter the file with usernames")
args = parser.parse_args()

BASE_URL = "https://ws2.kik.com/user/"


def do_print_banner():
    print("""
    ,_,_,_,_,_,_,_,_,_,_|______________________________________________________
    |#|#|#|#|#|#|#|#|#|#|_____________________________________________________/
    '-'-'-'-'-'-'-'-'-'-|----------------------------------------------------'
    """)
    print("\033[1mDeveloped by SakuraSamurai\033[0m\n")


def process_input():
    if args.file:
        with open(args.file, "r") as handle:
            usernames = handle.readlines()
        usernames = list(map(str.strip, usernames))
    else:
        usernames = [args.username]
    return usernames


def check_user(uid):
    target = f"{BASE_URL}{uid}"
    res = requests.get(target)
    if res.status_code == 200:
        return res.json()


def do_generate_output(usernames):
    valid_users = []

    for username in usernames:
        info = check_user(username)
        if info is not None:
            print(info)
            valid_users.append(f"Username: {username} Info: {info}")
        else:
            print(f"[-] {username} not found")

    with open("valid.txt", "a") as handle:
        handle.write('\n'.join(valid_users))


def main():
    do_print_banner()
    usernames = process_input()
    do_generate_output(usernames)
    print("\nValid users written to valid.txt")


if __name__ == "__main__":
    main()
