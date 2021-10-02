import num_db
import os

app_name = '''
___ ____ _    ____ ___  _  _ ____ _  _ ____    ___  ____ ____ _  _ 
 |  |___ |    |___ |__] |__| |  | |\ | |___    |__] |  | |  | |_/  
 |  |___ |___ |___ |    |  | |__| | \| |___    |__] |__| |__| | \_ 
'''
menu = '''                                                                   

Options:
1. Add a new number
2. Edit a number(require number's id)
3. Delete a number(require number's id)
4. Veiw a contact
5. View contact list

0. Quit


'''

edit_menu='''

1. Edit a number's name
2. Edit a number's phone number
3. Edit a number's email address
4. Edit all of a number's info

0. Back to main menu


'''
search_menu='''

1. Open by name
2. Open by email address
3. Open by id

0. Back to main menu


'''
def clears():
    if os.name == "nt":
        clears()
    elif os.name == "posix":
        os.system("clear")
while True:
    clears()
    print(app_name)
    print(menu)
    choice = input("Enter your choice: ")


    if choice == '1':
        #? add a new number
        clears()
        print(app_name)
        name=input("Enter the name: ")
        
        if len(name) > 3:
            numt=True
        else:
            print("Name is too short")
            input("Press enter to return to the main menu...")
            continue
        email=input("Enter the email(Optional): ")


        if email == '' or len(email) > 5:
            namet=True
        else:
            print("Email is too short")
            input("Press enter to return to the main menu...")
            continue
        number=input("Enter the number: ")


        if len(number) > 8:
            emailt=True
        else:
            print("Phone number is too short")
            input("Press enter to return to the main menu...")
            continue

        if numt and namet and emailt:
            try:
                num_db.add_number(name, email, number)
                print("Number added successfully!")
                input("Press enter to return to the main menu...")
            except:
                print("Error: Number not added")
                input("Press enter to return to the main menu...")
        

        




    elif choice == '2':
        #? edit a number
        clears()
        print(app_name)
        print(edit_menu)
        option = input("Enter your choice: ")
        if option == '0':
            continue
        else:
            clears()
            print(app_name)
            num_id = input("Enter the number's id: ")
            editable=num_db.Editor(num_id)
            clears()
            print(app_name+'\n')
            print(f'ID: {num_id}\n\n')
            if option == '1':
                
                name = input("Enter the new name: ")
                if len(name) > 3:
                    editable.edit_name(name)
                else:
                    print("Name too short")
                
                print("Name changed to: " + name)
                input("Press enter to return to the main menu...")

            elif option == '2':
                
                number = input("Enter the new number: ")
                try:
                    if len(number) > 8:
                        editable.edit_number(number)
                        print("Number changed to: " + number)
                        input("Press enter to return to the main menu...")
                    else:
                        print("Number too short")
                except:
                    print("Unknown error! Number not changed")


            elif option == '3':
                
                email = input("Enter the new email: ")
                try:
                    if len(email) > 5:
                        editable.edit_email(email)
                        print("Email changed to: " + email)
                        input("Press enter to return to the main menu...")
                    else:
                        print("Email too short")
                except:
                    print("Unknown error! Number not changed")

            elif option == '4':
                name = input("Enter the new name: ")
                number = input("Enter the new number: ")
                email = input("Enter the new email: ")
                if len(number) > 8:
                    if len(name) > 3:
                        if len(email) > 5:
                            try:
                                editable.edit_all(name, email, number)
                                print("All info changed!")
                                input("Press enter to return to the main menu...")
                            except:
                                print("Unknown error! Number not changed")
                                input("Press enter to return to the main menu...")
                        else:
                            try:
                                editable.edit_all(name, "", number)
                                print("All info changed!")
                                input("Press enter to return to the main menu...")
                            except:
                                print("Error! All info not changed")
                                input("Press enter to return to the main menu...")
            
                    else:
                        print("Name too short")
                else:
                    print("Number too short")
                input("Press enter to return to the main menu...")
            
            else:
                print("Invalid input")
                input("Press enter to return to the main menu...")


    elif choice == '3':
        clears))
        print(app_name)
        deleteid=input("Enter the ID to delete: ")
        try:
            clears()
            print(app_name)
            num_db.delete(deleteid)
            print(f"Number {deleteid} was deleted!")
            input("Press enter to return to the main menu...")

        except:
            print("Error! Number not deleted")
            input("Press enter to return to the main menu...")



    elif choice == '4':
        #? search for a number
        clears()
        print(app_name)
        print(search_menu)
        option = input("Enter your choice: ")
        if option == '1':
            clears()
            print(app_name)
            name = input("Enter the name: ")
            try:
                clears()
                print(app_name)
                rows = num_db.search_by_name(name=name)
                if len(rows) == 0:
                    print("No results found")
                else:
                    for row in rows:
                        print(f'''
ID:     {row[0]}
Name:   {row[1]}
Email:  {row[2]}
Number: {row[3]}
==============''')
                input("Press enter to return to the main menu...")
            except:
                print("Can't search")
                input("Press enter to return to the main menu...")



        elif option == '2':
            clears()
            print(app_name)
            email = input("Enter the email: ")
            try:
                clears()
                print(app_name)
                rows = num_db.search_by_email(email=email)
                if len(rows) == 0:
                    print("No contact found")
                else:
                    for row in rows:
                        print(f'''
ID:     {row[0]}
Name:   {row[1]}
Email:  {row[2]}
Number: {row[3]}
==============''')
                input("Press enter to return to the main menu...")
            except:
                print("Can't search")
                input("Press enter to return to the main menu...")
        
        elif option == '3':
            clears()
            print(app_name)
            id = input("Enter the id: ")
            try:
                clears()
                print(app_name)
                rows = num_db.search_by_id(id=int(id))
                if len(rows) == 0:
                    print("No contact found")
                else:
                    for row in rows:
                        print(f'''
ID:     {row[0]}
Name:   {row[1]}
Email:  {row[2]}
Number: {row[3]}
==============''')
                input("Press enter to return to the main menu...")
            except:
                print("Can't search")
                input("Press enter to return to the main menu...")
        else:
            print("Invalid input")
            input("Press enter to return to the main menu...")
            



    elif choice == '5':
        try:
            clears()
            print(app_name)
            rows = num_db.view()
            if len(rows) == 0:
                    print("No contact found")
            else:
                for row in rows:
                    print(f'''
ID:     {row[0]}
Name:   {row[1]}
Email:  {row[2]}
Number: {row[3]}
==============''')
        
        except:
            print("Can't search")
        
        
        input("Press enter to return to the main menu...")


    elif choice == '0':
        break
