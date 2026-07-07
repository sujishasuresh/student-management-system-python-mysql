from admin.menu import display_admin_menu

def authenticate_admin(username,password):
    ADMIN_USERNAME='admin123'
    ADMIN_PASSWORD='password123'
    if ADMIN_USERNAME==username:
        if ADMIN_PASSWORD==password:
            return 'SUCCESS'
        else:
            return 'WRONG PASSWORD'

    else:
        if ADMIN_PASSWORD==password:
            return 'WRONG USERNAME'
        else:
            return 'BOTH INCORRECT'
    

def get_admin_credentials():
    print("====Admin=====")
    while True:
        username=input("Username: ")
        password=input("Password: ")
        status=authenticate_admin(username,password)
        if status=='SUCCESS':
            print("Login successfully")
            display_admin_menu()
            break
        elif status=='WRONG USERNAME':
            print("Incorrect user name")
            continue
        elif status=='WRONG PASSWORD':
            print("Incorrect password")
            continue
        elif status=='BOTH INCORRECT':
            print("Incorrect username and password ")
            continue





