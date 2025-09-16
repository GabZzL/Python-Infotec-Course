def hotel():
    rooms = {"single": 3, "double": 2}
    
    while True:
        option = input("book, release, or exit? ")
        
        match option:
            case "book":
                type = input("Select your room type(single or double): ")
                if type in rooms and rooms[type] > 0:
                    rooms[type] -= 1
                    print(f"Room has been booked: {type}")
                else :
                    print(f"Room {type} is not available")
            case "release":
                type = input("Select your room type(single or double)")
                
                if type == "single" and rooms[type] < 3:
                    rooms[type] += 1
                    print(f"Room has been released: {type}")
                elif type == "double" and rooms[type] < 2:
                    rooms[type] += 1
                    print(f"Room has been released: {type}")
                else:
                    print(f"There is no more {type} available rooms")
            case "exit":
                break
            case _:
                print("Invalid option")
        
        print("Room status")
        print(rooms)

hotel()