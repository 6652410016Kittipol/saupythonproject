money = input("insert number of money : ")
amount_of_people = input("insert amount of people : ")
product_value = int(money)/int(amount_of_people)
product_value_t = format(product_value, ".2f")
print("You would get", product_value_t, "Baht per peron")
print("You would get" + product_value_t + "Baht per peron")
print("You would get {} Baht per peron".format (product_value_t))
print(f"You would get {product_value_t} Baht per person")