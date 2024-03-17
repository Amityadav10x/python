def process_input(choice):

    if choice == 'A':
        print("option a selected")
    elif choice =='B':
        print("option b is selected")
    elif choice == 'C':
        print("option c is selected")
    elif choice == 'D':
        print("option d is selected")
    elif choice == 'E':
        print("option e is  selected")
    else:
        print("selected choice is invalid")

choices = ['A','B','C','D','E']
for choice in choices:
        if choice == 'D':
            continue
        elif choice == 'E':
            break
        else:
            process_input(choice)