import json
import getpass
import datetime
import string
import subprocess
import os 
import hashlib
import secrets
username = input("Enter your cloud username: ")
password = getpass.getpass("Enter your cloud password: ")
pass_hash = hashlib.sha256(password.encode()).hexdigest()  
new = datetime.datetime.now()

def cloud ():
    print("Your fingerprint is being scanned...")
    a = input("You want to proceed or not (y/n): ")
    if a == 'y':
        print("Fingerprint scan successful.")
        with open ("db.json", "r+") as file:
            data = json.load(file)
            
        if username in data["users"] and pass_hash == data["users"][username]["password"] and data["users"][username]["role"] == "admin":         #HACKER
            
             print("Access granted.")
             if "key_rotation_days" not in data["config"]:
                    z = int(input("Enter number of days after which you want to rotate keys: "))
                    data["config"]["key_rotation_days"] = z
                    if z not in range (15,91):
                       print("Invalid input. Please enter a number between 15 and 90.")
                    
            
             if (new - datetime.datetime.fromisoformat(data["users"][username]["key_created"])).days > data["config"]["key_rotation_days"]:
               alert()
             log = True
             while log == True:
              print("Welcome to the cloud configuration, admin user.")      
              print("1.Do you want to make an EC2 instance? : ")
              print("2. Do you want to make an S3 instance? : ")
              print("3.Do you want to delete an S3 instance? : ")
              print("4.Do you want to delete an EC2 instance? : ")
              print("5.Do you want to view the logs? : ")
              print("6.Make a new user in VPC.")
              print("7.Delete a user from VPC.")
              print("8.You can move to folder. ")
              print("9.Exit.")
              EC = input("Enter your choice: ")
              
              match EC: 
                case '1':
                     folder = input('Enter the  name of EC2 : ')
                    
                     with open("polcy.json" ,"r")as file :
                         data = json.load(file)
                     if folder in data["Folder"]["EC2"] :
                         print(f"{folder} is already exist")
                     else:
                            os.mkdir(folder)
                            print("Creatring EC2 instance....")
                            print(f"Folder '{folder}' created successfully.")
                            
                            data["Folder"]["EC2"][folder] = {
                             "permission": [".pdf",".png",".jpg",".jpeg",".txt",".py",".cpp"]
              
                         }
                            with open("polcy.json" ,"w")as file :
                             json.dump(data , file , indent =4 )
                case '2':
                    folder = input('Enter the  name of S3 : ')
                    
                    with open("polcy.json" ,"r")as file :
                         data = json.load(file)
                    if folder in data["Folder"]["S3"] :
                         print(f"{folder} is already exist")
                    else:
                            os.mkdir(folder)
                            print("Creatring S3 instance....")
                            print(f"Folder '{folder}' created successfully.")
                            
                            data["Folder"]["S3"][folder] = {
                             "permission": [".pdf" , ".png",".jpg",".jpeg" , ".txt"]   
                         }
                            with open("polcy.json" ,"w")as file :
                             json.dump(data , file , indent =4 )
                         
                   
                    
                case '3':
                    folder = input('Enter the name of S3 to delete :')
                    try:
                        os.rmdir(folder)
                        print(f"Folder '{folder}' deleted successfully.")
                    except FileNotFoundError:
                        print(f"Folder '{folder}' not found.")
                    except OSError:
                        print(f"Folder '{folder}' is not empty or cannot be deleted.")
                        
                case '4':
                    folder = input('Enter the name of EC2 to delete :')
                    try:
                        os.rmdir(folder)
                        print(f"Folder '{folder}' deleted successfully.")
                    except FileNotFoundError:
                        print(f"Folder '{folder}' not found.")
                    except OSError:
                        print(f"Folder '{folder}' is not empty or cannot be deleted.")
                
                case '5':
                    logs()
                    
                case '6':
                    newuser = input("Enter new username: ")
                    newpassword = getpass.getpass("Enter new password: ")
                    has = hashlib.sha256(newpassword.encode()).hexdigest()  
                    newrole = input("Enter role (developer/tester): ")
                    if newrole  not in ["developer" , "tester"]:
                        print("Invalid role. Please enter 'developer' or 'tester'.")
                        return
                    if newuser in data["users"]:
                        print("User already exists.")
                    else:
                        data["users"][newuser]={
                        "password": has,
                        "role": newrole,
                        "key_created": str (datetime.datetime.now())
                        
                        }
                        with open ("db.json", "w")as file :
                            json.dump(data, file , indent = 4 )
                            print("New user added successfully.") 
                        
                case '7':
                    deluser = input("Enter username to delete: ")
                    if deluser in data["users"]:
                        del data["users"][deluser]
                        with open("db.json", "w")as file :
                            json.dump(data, file , indent = 4 )
                        print("User deleted successfully.")
                    else : 
                        print("User not found.")
                case '8':
                    policy()
                case '9' :
                    return         
                case _:
                    print("Invalid choice.")
                    
        elif username in data["users"] and pass_hash == data["users"][username]["password"] and data["users"][username]["role"] == "developer":        #password123
            print("Access granted.")
            print("Welcome to the cloud configuration, developer.")
            logs_save()
          
            if (new - datetime.datetime.fromisoformat(data["users"][username]["key_created"])).days > data["config"]["key_rotation_days"] :
             alert()
            log = True
            while log == True:
                
             print("1.Do you want to make an EC2 instance? : ")
             print("2.Do you want to make an S3 instance? : ")
             print("3.Do you want to make a file in EC2? : ")
             print("4.Do you want to run a test scripts ? : ")
             print("5.You make file in S3 bucket.")
             print("6.Exit")
             choice  = int(input("Enter your choice : "))         
             match choice :
                case 1:
                 folder = input('Enter the name of EC2 instance: ')
                 with open("polcy.json" ,"r")as file :
                         data = json.load(file)
                 if folder in data["Folder"]["EC2"] :
                         print(f"{folder} is already exist")
                 else:
                            os.mkdir(folder)
                            print("Creatring EC2 instance....")
                            print(f"Folder '{folder}' created successfully.")
                            
                            data["Folder"]["S3"][folder] = {
                             "permission": [".pdf",".png",".jpg",".jpeg",".txt",".py",".cpp"]
              
                         }
                            with open("polcy.json" ,"w")as file :
                             json.dump(data , file , indent =4 )
                  
                case 2:
                 folder = input('Enter the name of S3 instance: ')
                 with open("polcy.json" ,"r")as file :
                         data = json.load(file)
                 if folder in data["Folder"]["S3"] :
                         print(f"{folder} is already exist")
                 else:
                            os.mkdir(folder)
                            print("Creatring S3 instance....")
                            print(f"Folder '{folder}' created successfully.")
                            
                            data["Folder"]["S3"][folder] = {
                             "permission": [".pdf" , ".png",".jpg",".jpeg" , ".txt"]   
                         }
                            with open("polcy.json" ,"w")as file :
                             json.dump(data , file , indent =4 )
                 
                case 3:
                 policy()
                 
                 with open("polcy.json" ,"r")as file :
                       data = json.load(file)     
                 folder = os.getcwd()
                 
                 folder = os.path.relpath(folder, r"D:\new")
                 print(folder)
                 if folder in data["Folder"]["EC2"] :
                     file = input("Enter the file name to write code with format (like cpp): ")
                 
                     print("Enter your code (type EOF for break): ")
                     lines = []
                     while True:
                        line = input()
                        if line == "EOF":
                         break
                        lines.append(line)
                     code = "\n".join(lines)
                     with open(file, "w") as f:
                      f.write(code)
                      print(f"Code written to {file} successfully.")
                      log = False
                case 4:
                    policy()
                    with open("polcy.json" ,"r")as file :
                       data = json.load(file)     
                    folder = os.getcwd()
                 
                    folder = os.path.relpath(folder, r"D:\new")
                    print(folder)
                    if folder in data["Folder"]["EC2"] :
                            file = input("Enter the file name to read code with format (like py or cpp): ")
                    if "cpp" in file : 
                         try:
                            exe = file.replace(".cpp","")
                            result_compile = subprocess.run(["g++", file, "-o",exe],stdout = subprocess.PIPE ,text = True)
                            print(f"Executed {file} sucessfully")
                            print("Output: \n ")
                         except FileNotFoundError:
                           print(f"File {file} not found.")
                           log = False
                         if result_compile.returncode != 0 :
                            print("Compile error")
                            log = False
                         else :
                            result = subprocess.run([f"{exe}.exe"],stdout = subprocess.PIPE ,text = True)
                            print(result.stdout)
                            log = False 
                    else :
                         try :
                           result = subprocess.run(["python", file], stdout = subprocess.PIPE , text =True)
                           print(f"Executed {file} successfully.")
                           print("Output:\n", result.stdout)
                         except FileNotFoundError :
                            print(f"File {file} not found.")  
                         log = False        
                case 5: 
                    policy()
                    with open("polcy.json" ,"r")as file :
                       data = json.load(file)     
                    BASE_DIR = os.path.abspath(os.getcwd())
                    current_dir = os.path.abspath(os.getcwd())
                    folder = os.path.relpath(current_dir, BASE_DIR)
                    print(folder)
                    if folder in data["Folder"]["S3"] :
                     file = input("Enter the file name to write file with format : ")
                     name , ext = os.path.splitext(file)
                     print(ext)
                     if ext in data["Folder"]["S3"][folder]["permission"] :
                        print("Enter your code (type EOF for break): ")
                        lines = []
                        while True:
                            line = input()
                            if line == "EOF":
                                break
                            lines.append(line)
                        code = "\n".join(lines)
                        with open(file, "w") as f:
                            f.write(code)
                            print(f"Code written to {file} successfully.")
                        log = False
                     else: 
                         print("You are in S3 Bucket. You haven't permission to make Executable file. ")
                         log = False
                case 6:
                    return
                case _:
                 print("Invalid choice.")                    
        elif  username in data["users"] and pass_hash == data["users"][username]["password"] and data["users"][username]["role"] == "tester":            #pass456
            print("Access granted.")
            print("Welcome to the cloud configuration, tester.")
            logs_save() 
            
            if (new - datetime.datetime.fromisoformat(data["users"][username]["key_created"])).days > data["config"]["key_rotation_days"] :
             alert()
            log = True
            while log == True:    
             print("1.Do you want to see logs?:")
             print("2.Do you want to read a test scripts ? : ")
             print("3.You can move to folder. ")
             print("4.Exit")
            
             choice  = int(input("Enter your choice ?"))         
             match choice :
                case 1:
                 logs()
                
                case 2:
                  file = input("Enter the file name to read code with format (like py or cpp): ") 
                  try:
                   with open(file, "r") as f:
                        content = f.read()
                        print(f"Content of {file}:\n{content}")
                  except FileNotFoundError:
                      print("File not found ")
                case 3:
                    policy()
                    log = False
                case 4:
                    return
                case _:
                    print("Invalid choice.")
                   
        else :
           print("Access denied. Using default configuration.")
           logs_save()
           return 0 
    else :
        print ("Fingerprint scan failed. Using default configuration.")
def logs_save():
    log = "log.txt"
    try : 
        with open("logs.txt", "a") as file:
            logs = (f'[{datetime.datetime.now()}] - User: {username}  accessed the cloud configuration.\n')
            file.write(logs)
            print("Logs updated successfully.")
    except FileNotFoundError:
        print("Log file not found. Creating a new log file.")
    finally:
        file.close()
        
def alert():
    print ("Alert! Please roatate the keys....")
    print ("You have two options to ratotate the passowrd : \n 1. Manually \n 2. Automatically")
    choice = int(input ("Enter your choice (1/2): "))
    with open ("db.json", "r+") as file:
            data = json.load(file)
    if choice == 1:
               newpassword = getpass.getpass("Enter the new password :")
               if len(newpassword) < 8:
                    print("Password must be at least 8 characters")
                    return
               ha = hashlib.sha256(newpassword.encode()).hexdigest() 
               data["users"][username]["key_created"] = str (new)
               data["users"][username]["password"] = ha
               with open("db.json","w")as file:
                json.dump(data,file,indent =4)
                print("Password rotated successfully and key_created is also updated.")
    elif choice == 2:
              alphabet = string.ascii_letters + string.digits + string.punctuation 
              autopassword = ''.join(secrets.choice(alphabet) for i in range(16))
              has = hashlib.sha256(autopassword.encode()).hexdigest() 
              print("Generated secure password:", autopassword)
              data["users"][username]["key_created"] = str (new)
              data["users"][username]["password"] = has
              with open("db.json","w")as file:
                json.dump(data,file,indent =4)
                print("Password rotated successfully and key_created is also updated.")
def logs():
    try :
        with open ("logs.txt" , "r") as file:
            print("Here are the logs : \n", file.read())
    except FileNotFoundError :
        print ("Log file not found.")    
def policy ():
    with open("polcy.json", "r") as file :
       ls = json.load(file)
    print("\nEC2 Instances:")
    for vm_name in ls["Folder"]["EC2"]:
        print("-", vm_name)
    print("\nS3 Instances:")
    for vm_name in ls["Folder"]["S3"]:
        print("-", vm_name)
    folder = input("To move in folder and Enter the folder name : ")
    
    if folder in ls["Folder"]["EC2"] or folder in ls["Folder"]["S3"]:
     os.chdir(folder)
    
     if folder in ls["Folder"]["EC2"] :
        print("You are in EC2 folder : ")
        print("1.To see file ")
        print("2.Exit")
        d = int(input("Enter your choice :"))
        if d ==1 :
            for f in os.listdir():
              print(f) 
        elif d ==2 :
            return 0
        else: 
            print("Invalid choice")
     else:
        print("You are in S3 buckets")
        print("To see file in presss 1")
        print("2.Exit")
        d = int(input("Enter your choice :"))
        if d ==1 :
            for f in os.listdir():
              print(f)
        elif d ==2 :
            return
        else: 
            print("Invalid choice")
    else:
        print("folder is not exit in current dir ")   
cloud()



        
    
