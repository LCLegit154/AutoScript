import os

while True:
    print("[1] Desktop")
    print("[2] Documents")
    print("[0] Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        while True:
            print("[1] Run python script")
            print("[0] Exit")
            sub_choice = input("Enter your choice: ")
            
            if sub_choice == "1":
                script_name = input("Enter script name: ")
                script_path = os.path.join(os.path.expanduser("~"), "Desktop", script_name)
                
                if os.path.exists(script_path) and os.path.isfile(script_path):
                    exec(open(script_path).read())
                else:
                    print("Script does not exist.")
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
    elif choice == "2":
        while True:
            print("[1] Run python script")
            print("[0] Exit")
            sub_choice = input("Enter your choice: ")
            
            if sub_choice == "1":
                script_name = input("Enter script name: ")
                script_path = os.path.join(os.path.expanduser("~"), "Documents", script_name)
                
                if os.path.exists(script_path) and os.path.isfile(script_path):
                    exec(open(script_path).read())
                else:
                    print("Script does not exist.")
            elif sub_choice == "0":
                break
            else:
                print("Invalid choice. Try again.")
    elif choice == "0":
        break
    else:
        print("Invalid choice. Try again.")
