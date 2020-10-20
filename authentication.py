def fun():
    print("Thats all your data")
    print("Penetration Start")
    print("....0%")
    print("....40%")
    print("....60%")
    print("....90%")
    print("Penetration Succesfull")






















users={
    "nitish":"password",
    "prateek":"codingblocks"
}
def show(username,password):
    if username in users :
        if users[username]=="password":
            print("You could logon in to your system: ",username)
            fun()
        elif users[username]=="codingblocks":

            print("You could logon in to your system: ",username)
            fun()
        else:
            print("Enter the Valid Password")
        
    else:
        print("Enter the Valid Username")


username=input("Enter ur Valid Username: ")
password=input("Enter ur Password:  ")

show(username,password)


        



