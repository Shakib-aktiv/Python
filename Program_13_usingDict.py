#  Store  system....
# this is second comments ...
store = {
    'shelf1': {
        'product1': {
            'january': {
                'Price': [[10, 30, 45, 50],20]
            },
            'february': {
                'Price': [[60, 64, 68],30]
            }


        },
        'product2': {
            'january': {
                'Price': [[66, 67, 81, 75],20]
            },
            'february': {
                'Price': [[78, 81, 85],30]
            }
        },
        'product3': {
            'january': {
                'Price': [[18, 20],35]
            },
            'february': {
                'Price': [[21, 22],40]
            },
            'march': {
                'Price': [[22, 23, 24],45]
            }
        }
    },
    'shelf2': {
        'product1': {
            'january': {
                'Price': [[206, 220, 225],10]
            },
            'march': {
                'Price': [[180, 170, 165],10]
            },
            'april': {
                'Price': [[160, 150, 136],15]
            }
        },
        'product4': {
            'january': {
                'Price': [[300],10]
            },
            'february': {
                'Price': [[280, 300, 385],10]
            },
            'march': {
                'Price': [[280, 300, 385],15]
            },
            'april': {
                'Price': [[360, 376],10]
            }
        }
    },
    'shelf3': {
        'product2': {
            'march': {
                'Price': [[55, 59, 61]]
            },
            'april': {
                'Price': [[53, 54, 55]]
            }
        }
    }
}



def createself():
    firstName = input("enter a shelf name : ")
    store[firstName] = {}
    first = input("create Product ENter Y   : ")
    if first == "Y":
        second = store[firstName]
        third = int(input("enter a Product number you want to add it ... (ex 1): "))
        for i in range(third):
            qw = input("enter a name a products : ")
            second[qw] = {}
            fourth = input("create a months  Y : ")
            if fourth == "Y":

                fifth = second[qw]
                fifth1 = int(input("enter a months number you want to add it ... (ex-2): "))
                for j in range(fifth1):
                    fifth2 = input("enter a Months name : ")
                    fifth[fifth2] = {}
                    sixth = input("create a Price   Y : ")
                    if sixth == "Y":
                        seventh = fifth[fifth2]
                        seventh['price'] = []
                        eight = seventh['price']
                        eight1 = int(input("how many price  number you want to add it ... : "))
                        for l in range(eight1):
                            eight2 = int(input("Enter the Price "))
                            eight.append(eight2)

    else:
        print("okay..")

 def update():
 	print("given list that vaslue can enter otherwise give a error ..")
 	totalshelf = store.keys()
 	print(totalshelf)
 	first = input("enter a self name ... : ")
 	totalProduct = store[first].keys()
 	print(totalProduct)
 	second = input("enter a produc name ... : ")
 	totalmonths = store[first][second].keys()
 	print(totalmonths)
 	third = input("Enter a moths name ..")
 	data=store[first][second][third]['Price']
 	print(data)


print("welcome to the store...")
totalshelf =store.keys()
print(list(totalshelf))
first =input("enter a shelf name... : ")
if first in totalshelf:
    totalProduct =store[first].keys()
    print(list(totalProduct))
    second = input("enter a product name ... : ")
    if second in totalProduct:
        totalmonths =store[first][second].keys()
        print(list(totalmonths))
        third = input("enter a months ... : ")
        if third in totalmonths:
            Price = store[first][second][third]['Price']
            print("This is cost Price : ", Price[0])
            decision = input("to make a by default calculeate to press y oither wise n ")
            if decision =='y':
                salesPrice = map(lambda value: ((Price[1]/100) * value) + value, Price[0])
                print("This is sales Price : ", list(salesPrice))
                 last  = input("do you need a create user Enter Y"):
                 if last =="y":
                 	createself()
                 	print(store)

            elif decision =="n":
                percentage= int(input("enter Percentage : "))
                salesPrice = map(lambda value: ((percentage/100) * value) + value, Price[0])
                print("This is sales Price : ",list(salesPrice))
                 last  = input("do you need a create user Enter Y"):
                 if last =="y":
                 	createself()
                 	print(store)
               
            else:
                print("wrong")
        else:
            print("wrong input ..")
    else:
        print("wrong input")
else:
    print("wrong choice...")
