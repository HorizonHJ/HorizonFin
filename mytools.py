import os

card_list = []


def main_function():
    print('*' * 50)
    print('【Welcome to use oliver system】 V1.0')
    print('1. Create ID Card')
    print('2. Show all ID Cards')
    print('3. Find the ID Card' + "\n")
    print('0. exit the system')
    print('*' * 50)


def action_user():
    action_str = input("please chose the action you want to do: ")
    print("you have chosen 【%s】" % action_str)
    if action_str in ["1", "2", "3", "0"]:
        if action_str == "1":
            add_user()
        elif action_str == "2":
            show_all()
        elif action_str == "3":
            find_user()
        elif action_str == "0":
            print("Thanks for using this system")
            exit()
    else:
        print("your choice is undefined, please re-try")
        action_user()


def add_user():
    name = input("please input the user name: ")
    id_card = input("please input the user id card: ")
    qq_number = input("please input the qq number: ")

    user_dic = {'username': name, 'userid': id_card, 'userqq': qq_number}
    card_list.append(user_dic)
    print("the user %s has been added successfully" % name)


def show_all():
    if not card_list:
        print("there is no user in system")
    else:
        print("Name\t\tID_Card\t\tQQ")
        print("=" * 50)
        for card_dict in card_list:
            print("%s\t\t\t%s\t\t\t%s" % (card_dict['username'],
                                          card_dict['userid'],
                                          card_dict['userqq'],))


def find_user():
    print("-" * 50)
    print("*" * 20 + "Find User" + "*" * 20)
    uname = input("please input the user name that you want to check: ")
    if not card_list:
        print("there is no user in system")
    else:
        print("Name\t\tPhone\t\tQQ")
        for card_dict in card_list:
            if card_dict['username'] == uname:
                print("=" * 50)
                print("%s\t\t\t%s\t\t\t%s" % (card_dict['username'],
                                              card_dict['userid'],
                                              card_dict['userqq'],))
                deal_card(card_dict)
            else:
                print("the user : %s can not be found" % uname)
                find_user()


def deal_card(choice):
    action = input("please input the action you want to do for the [%s] " % choice["username"] + '\n'
                                                                                                 "<1> Modify <2> delete <3> go back to former menu: ")
    if action == "1":
        pass
    elif action == "2":
        card_list.remove(choice)
    elif action == "3":
        main_function()
        action_user()
    else:
        print("Choice %s is un-defined, please re-try" % action)
        exit(0)
