#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program finds out if grand child is dateable


def main():
    # funciton calculates grand child compatability

    # Welcome statement
    print("Let's find out if you can date my grandchild.")
    input("Press Enter to continue.")

    # input
    money = input("\nDo you posess large amounts of money? (y/n)")
    beauty = input("Do you possess beautiful? (y/n)")

    # process
    if money == "y" and beauty == "y":
        # output
        print("\nYou are eligible to date my grandchild.")
    else:
        print("\nYou are not eligible to date my grandchild.")


if __name__ == "__main__":
    main()
