import time

def Add_Order():
    with open("orders.txt", "a", encoding="utf-8") as file:
        try:
            order_num = int(input("Enter your orders num you want to add: "))
            order_name = input("Enter your orders name: ")
            order_quantity = int(input("Enter your orders quantity: "))
            order_price = int(input("Enter your orders price: "))
            
            file.write(f"{order_num},{order_name},{order_quantity},{order_price}\n")

            return True
        except:
            return False


while True:
    
    print("---------- Web store controller panel! ----------")
    
    try:
        menu_choice = int(input("1. Add a new order\n2. Review all orders\n3. Search for an order by a number\n4. Update order\n5. Delete order\n6. Exit\n"))

    except TypeError:
        print("You must enter a number, not an text!")
        continue

    match menu_choice:
        case 6:
            break

        case 1:
            result = Add_Order()
            if result == True:
                print("Your order was added in the file!")
                time.sleep(1.5)

            elif result == False:
                print("Your order wasn't added correctly. Make sure you've entered all correctly.")
                time.sleep(1)

        case 2:
            with open("orders.txt", "r", encoding="utf-8") as file:
                for index, value in enumerate(file, start=1):
                    value = value.strip("\n").split(",")

                    print(f"{index}: {value[1]}")
            time.sleep(1)
        case 3:
            order_num_search = str(int(input("Enter your order num you want to find: ")))

            with open("orders.txt", "r", encoding="utf-8") as file:
                for value in file:
                    value = value.strip("\n").split(",")

                    if value[0] == order_num_search:
                        print(f"Name of the order: {value[1]}\nQuantity: {value[2]}\nPrice: {value[3]}\n")

                    else:
                        print("There's no order by this tracking number.")

                time.sleep(1)

        case 4:
            order_to_update = input("Enter your orders number: ")

            with open("orders.txt", "r") as file:
                for tracking_num in file:
                    tracking_num = tracking_num.strip("\n").split(",")

                    if tracking_num[0] == order_to_update:
                        update_info = int(input("Enter what do you want to update:\n1. Quantity of the order\n2. Price of the order\n"))

            match update_info:
                case 1:
                    quantity = int(input("Enter quantity: "))

                    with open("orders.txt", "r", encoding="utf-8") as file:
                        file_text = file.readlines()

                        file_text_clean = []
                        for line in file_text:
                            line = line.strip("\n").split(",")

                            if line[0] == order_to_update:
                                line[2] = str(quantity)

                            file_text_clean.append(",".join(line) + "\n")

                        with open("orders.txt", "w", encoding="utf-8") as file:
                            file.writelines(file_text_clean)

                    print("Quantity changed succesfully!")


                case 2:

                    price = int(input("Enter a price you want change to: "))

                    with open("orders.txt", "r", encoding="utf-8") as file:
                        file_text = file.readlines()

                        file_text_clean = []
                        for line in file_text:
                            line = line.strip("\n").split(",")

                            if line[0] == order_to_update:
                                line[3] = str(price)

                            file_text_clean.append(",".join(line) + "\n")

                    with open("orders.txt", "w", encoding="utf-8") as file:
                        file.writelines(file_text_clean)

                    print("Price updated succesfully!")


                case 5:
                    order_to_delete = int(input("Enter your orders tracking num you want to delete: "))

                    with open("orders.txt", "r", encoding="utf-8") as file:
                        text_source = file.readlines()
                        text_clean = []

                        for line in text_source:

                            line = line.strip("\n").split(",")
                            if line[0] == str(order_to_delete):
                                continue

                            text_clean.append(",".join(line) + "\n")

                    with open("orders.txt", "w", encoding="utf-8") as file:
                        file.writelines(text_clean)
