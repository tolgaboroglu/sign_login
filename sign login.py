print("""**************************  
Sing Login
**************************  
 """ )

sys_user_name = "tolga"

sys_password = "122334455"

user_name =  input("Enter User Name:")

password  =  input("Enter Password:")

if(user_name !=sys_user_name and password ==sys_password):
    print("Wrong Username,Try Again...")

elif(user_name ==sys_user_name and password !=password):
    print("wrong password,Try Again...")

elif(user_name !=sys_user_name and password !=sys_password):
    print("Wrong Username and Password,Try Again...")

else:
    print("loging in...")

