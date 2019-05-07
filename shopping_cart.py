# shopping_cart.py

import datetime

def to_usd(price):
    return "${0:,.2f}".format(price)

def human_friendly_timestamp(d):
    timestamp = str(d.year) + "-" + str(d.month) + "-" + str(d.day) + " " + str(d.hour) + ":" + str(d.minute) + ":" + str(d.second)
    return timestamp


def find_product(products, product_id):
    matching_products = [p for p in products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    return matching_product

def calculate_total_price(products, selected_ids):
    running_total = 0
    for i in range(0, len(selected_ids)):
        item = find_product(products, selected_ids[i])
        #print("+ " + item["name"] + " (" + str(item["price"]) + ")")
        running_total = running_total + item["price"]
        i = i + 1
    return running_total

def receipt_print(selected_ids):
    print("-------------------------")
    print("Ryan's Grocery Store")
    print("-------------------------")
    print("Web: www.ryans.com")
    print("Phone: 1.908.555.5555")
    d = datetime.datetime.now()
    print("Checkout time: " + human_friendly_timestamp(d))
    print("-------------------------")
    print("Shopping Cart Items:")
    i = 0
    while ( i < len(selected_ids)):
        product = find_product(products, selected_ids[i])
        print("+ " + product["name"] + " (" + to_usd(product["price"]) + ")")
        running_total = calculate_total_price(products, selected_ids)
        i = i + 1
    print("-------------------------")
    print("Subtotal: " + str(to_usd(running_total)))
    tax = tax_calc(running_total)
    #print("Plus DC Sales Tax (6.0%): " + tax)))
    running_total = running_total + tax
    print("Total: " + str(to_usd(running_total)))
    print("-------------------------")
    print("Thank you for shopping with us!")
    print("-------------------------")

def product_lookup(selected_ids):
    i = 0
    running_total = 0
    print("Shopping cart identifiers include: [", end="")
    for s in shopping_cart: 
        print(str(s), end="")
        if s == shopping_cart[-2]:
            break
        else:
            print(", ", end="")
    print("]")
    
    for i in range(0, len(selected_ids)):
        matching_products = [p for p in products if p["id"] == selected_ids[i]]
        
        item = matching_products[0]
        print("+ " + item["name"] + " (" + str(item["price"]) + ")")
        running_total = running_total + item["price"]
        i = i + 1
    print( "Total Price: " + str(running_total))



if __name__ == "__main__":
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

    # TODO: write some Python code here to produce the desired functionality...
    #print(products)


    

    still_shopping = True

    #while still_shopping == True:
        #current_id = input("Please input a product id (if finished shopping, type 'DONE'): ")
        #if current_id == "DONE":
            #break
        #print(current_id)

    def tax_calc(subtotal):
        tax = subtotal * (0.06)
        return tax

    


    shopping_cart = []
    

    

    #this_list = [5, 4, 3, 2, 1]


    #MAIN TEXT
    while True:
        current_id = input("Please input a product id (if finished shopping, type 'DONE'): ")
        if current_id == "DONE":
            receipt_print(shopping_cart)
            break
        elif (int(current_id) >= 1 & int(current_id) <= 20):
            shopping_cart.append(int(current_id))
            #print(shopping_cart[0])
            #for s in shopping_cart:
                #print(s[0]) 
        else:
            print("Not a viable product number. Please try again!")

      
        #if current_id == "DONE":
            #print("Shopping cart identifiers include: [", end="")
            #for s in shopping_cart: 
                #print(str(s), end="")
                #if s == shopping_cart[-2]:
                    #break
                #else:
                    #print(", ", end="")
            #print("]", end="")
            #break
        
        


    #def product_lookup(selected_id):
        #matching_products = [p for p in products if p["id"] == selected_id]
        #product = matching_products[0]
        #print(product["name"] + " (" + str(product["price"]) + ")")



    #product_lookup(this_list)





        



    #receipt_print(this_list)

    #running_total = 0

    #t = 0

    #while t < 5:
        #selected_id = 1 #input("Please select a product id (1-20): ")
    # product = {
        #    "id":1
        #   "name": "Chocolate Sandwich Cookies",
        #  "department": "snacks",
        # "aisle": "cookie cakes",
            #"price": 3.50
        #}
        #matching_products = [p for p in products if p["id"] == selected_id]
        #product = matching_products[0]
        #price = product["price"] # todo: lookup atual price of the scanned product
        #running_total = running_total + price
        #t = t + 1


    #print("The total price is: " + str(running_total))

    #todo: calculate tax, add tax + total

    #q = datetime.datetime.now()

    #print("Started at: " + str(q))

