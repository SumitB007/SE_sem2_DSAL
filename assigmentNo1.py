list = []
semihash = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
print("empty dictionary:")
print(dict)
cust = int(input("enter number of customers"))
for i in range(cust):
    print(i)
    x = str(input("enter name of customer:"))
    y = int(input("telephone number:"))
    z = str(input("enter address:"))
    xyz = {"name": x, "telephone": y, "adress": z}
    list.append(xyz)
print(list)


def add():
    x = str(input("enter name of customer:"))
    y = int(input("telephone number:"))
    z = str(input("enter address:"))
    xyz = {"name": x, "telephone": y, "adress": z}
    list.append(xyz)


def display():
    print(list)


def look():
    k = int(input("enter key to search"))
    found = []
    for dictionary in list:
        if(dictionary["telephone"] == k):
            found.append(dictionary)
            print(found)
        else:
            print("not found")


def delete():
    y = int(input("enter the entry number to delete:"))
    del(list[y])


def hashing():
    telephone_numbers = []
    for dictionary in list:
        rem = dictionary["telephone"] % 10
        if semihash[rem] == " ":
            semihash[rem] = dictionary["telephone"]
        else:
            semihash[rem] = "collison occured between", semihash[rem], dictionary["telephone"]
    print(semihash)


if __name__ == '__main__':
    print("**********give input first*******")
    while (True):
        print("1.add entry to register")
        print("2.delete entry from register")
        print("3.display register")
        print("4.search number")
        print("5.hashing")
        print("enter 0 ot exit")
        choice = int(input())
        if (choice == 1):
            add()
        if (choice == 2):
            delete()
        if (choice == 3):
            display()
        if (choice == 4):
            look()
        if (choice == 5):
            hashing()
        if (choice == 0):
            exit()
