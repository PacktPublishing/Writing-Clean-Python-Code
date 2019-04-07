import access_check as check


def main():
    nested_check()
    flat_check()


def nested_check():
    print("This is the nested check ... ")
    if check.has_logged_in():
        if check.has_role():
            print("Yay you have access")
            if check.has_funds():
                print("Yay you can buy it")
            else:
                print("Please add more funds")
        elif check.is_root():
            print("Yay you have access")

        else:
            print("You do not have access to this area")
    else:
        print("You must be logged in")


def flat_check():
    print("This is the flat check ... ")

    if check.is_root():
        print("Yay you have access")
        return
    if not check.has_logged_in():
        print("You must be logged in")
        return
    if not check.has_role():
        print("You must have the correct role")
        return
    if not check.has_funds():
        print("Please add more funds")
        return

    print("You have access")


if __name__ == '__main__':
    main()
