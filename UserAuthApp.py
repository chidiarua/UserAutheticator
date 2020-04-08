import random
import string


def get_user_info():
    # collect details
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    email = input("Enter Email Address: ")

    details_container = {"First Name:": first_name, "Last Name:": last_name, "Email:": email}

    return details_container


def password_generator(details_container):
    # generate random password

    random_string = "".join([random.choice(string.ascii_letters) for i in range(5)])
    password = str(details_container['First Name:'][0:2] + random_string + details_container['Last Name:'][-2:0])

    return password


general_container = []  # empty list to store details
user_id = 0    # user serial count

# while everything remains, start a loop
while True:
    # getting user details
    details_container = get_user_info()

    # printing password
    password = password_generator(details_container)
    print(f"Your generated password is {password}.")

    # ask user if they are satisfied by password
    choice = input("Do you like your generated password(Y/N)?: ").upper()
    while True:
        if choice == "Y":
            # collect password and add to user details
            user_id += 1
            details_container.update({"Password:": password, 'S/N:': user_id})
            general_container.append(details_container)
            break
        else:
            new_password = input("Enter your preferred password: ")
            while True:
                if len(new_password) >= 7:
                    user_id += 1
                    details_container.update({"Password:": new_password, 'S/N:': user_id})
                    general_container.append(details_container)
                    break
                else:
                    print("Please, enter a password equal or longer than 7 characters.")
                    new_password = input("Enter your preferred password: ")
                continue
            break
    # make room for another user
    another_user = input("Is there another user(Y/N)?: ").upper()
    if another_user == "N":
        break
    # print all the details collected so far
for i in range(len(general_container)):
    print_pattern = (f'''
    First Name: {general_container[i]['First Name:']}
    Last Name: {general_container[i]['Last Name:']}
    Email: {general_container[i]['Email:']}
    Password: {general_container[i]['Password:']}
    S/N: {general_container[i]['S/N:']}
''')
    print(print_pattern)