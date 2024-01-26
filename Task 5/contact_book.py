print("----------------Contact Book App---------------------")
contact = {}


def display_contact():
    print("\nContact Details")
    for key in contact.keys():
        print("---------------------------------------")
        print("Name: ",key)
        for i in range(len(contact[key])):
            if i==0:
                print("Contact number: " + contact[key][i])
            elif i==1:
                print("Email id: " + contact[key][i])
            elif i==2:
                print("Address: " + contact[key][i])
            else:
                break
        print("---------------------------------------")


while True:
    choice = int(input(" 1. Add new contact \n 2. Search contact \n 3. Display contact \n 4. Edit contact \n 5. Delete contact \n 6. Exit \nEnter your choice: "))
    if choice == 1:
        name = input("Enter the contact name: ")
        phone = input("Enter the mobile number: ")
        email = input("Enter an email id of contact: ")
        address = input("Enter an address: ")
        contact[name] = [phone,email,address]
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name,"'s details are ")
            for i in range(len(contact[search_name])):
                if i==0:
                   print("Contact number: " + contact[search_name][i])
                elif i==1:
                   print("Email id: " + contact[search_name][i])
                elif i==2:
                   print("Address: " + contact[search_name][i])
                else:
                    break
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact to be edited:  ")
        if edit_contact in contact:
            phone = input("Enter mobile number: ")
            email = input("Enter an email id of contact: ")
            address = input("Enter an address: ")
            contact[edit_contact]=[phone,email,address]
            print("Contact updated")
            display_contact()
        else:
            print("Name is not found in contact book")
    elif choice == 5:
        del_contact = input("Enter the contact to be deleted: ")
        if del_contact in contact:
            confirm = input("Do you want to delete this contact y/n?:  ")
            if confirm =='y' or confirm =='Y':
                contact.pop(del_contact)
            display_contact()
        else:
            print("Name is not found in contact book")

    elif choice==6:
        break
    else:
        print("Wrong Choice")