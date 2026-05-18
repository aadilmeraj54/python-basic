## #Q.1 You are making a billing system for a grocery store.
## The store has a dictionary of items with their prices.
## Write a function calculate_bill(cart, price_list) that:
## • Takes a cart (list of items),
## • Calculates and returns the total bill.




# def calculate_bill(cart,price_list):
#     total=0
#     for item in cart:
#         if item in price_list:
#             total += price_list[item]
#             ###3#sum=sum+price_list[item]
#     return total        


# price_list = {
#     "milk":50,
#     "bread":30,
#     "butter":90,
#     "eggs":60
# }

# cart = ["milk","bread","eggs","milk"]

# total_bill = calculate_bill(cart, price_list)
# print(f"Total grocery bill: rs{total_bill} ")







##### Question 2: Student Marks Record
## You are managing marks of students in a class.
## Write a function find_topper (marks)
## that:
## • Takes a dictionary where keys are student names and values are marks,
## • Returns the name of the student with the highest marks.

marks = {
    "Ananya":92,
    "Rohit":88,
    "Megha":95,
    "Arjun":89

}

def find_topper(marks):
    topper_name = ''
    topper_marks = 0
    for k, v in marks.items():
        if v>topper_marks:
            topper_name = k
            topper_marks = v

    return topper_name

top_1 = print(find_topper ( marks))        
print (top_1)
        



##### Question 2: Unique Wishlist Items on Amazon
## You saved items to your Amazon wishlist but accidentally added duplicates.
## Write a function get_unique_items (items) that:
## • Takes a list of item names,
## • Returns a set of unique items (no duplicates).

def get_unique_items(items):
    return set(items)

wishlist = ["Headphone", "laptop", "camera", "Laptop", "Camera", "shoes"]

unique_items = get_unique_items(wishlist)
print("unique items:", unique_items)



###### Question 2: Amazon Order Status Checker
## Amazon tracks your orders with their status like "Delivered", "Shipped", "Processing", etc.
## Write a function count_delivered(status_list) that counts how many orders are "Delivered".
## • You are given a list of statuses of 7 orders,
## • Use a for loop inside the function,
## • Print how many have been delivered.

status = ["Deliered","shipped","Delivered","cancleed","Delivered","processing","Delivered"]

def count_delivered(status):
    d = 0
    for s in status:
        if(s.lower()=="delivered"):
            d=d+1
    return d

num=count_delivered(status)
print("number of Delivred ", num )        





# ######You are given:
## • A set of city names where you have weather data.
## • A dictionary where each key is a city name and the value is a tuple of (temperature, humidity).
## Write a function get_weather_report(city_name) that:
## • Checks if the city is available,
## • If yes, prints the temperature and humidity,
## • If not, prints "City not found."

def get_weather_report(city_name):
    for city in city_name:
        if city in weather_data:
            temperature,humidity = weather_data[city] 
        print(f"Temperature= {temperature} and Humidity= {humidity}")
available_cities= {"Delhi", "Mumbai", "Chennai",
"Kolkata"}
weather_data= {
    "Delhi": (35,45),
    "Mumbai": (30,70),
    "Chennai": (33,65),
    "Kolkata": (32,60)
    }
get_weather_report(available_cities)


available_cities = {"delhi","mumbai","chennai","kolkata"}
weather_date = {
    "delhi":(35,45),
    "mumbai":(30,70),
    "chennai":(33,65),
    "kolkata":(32,60)
}

get_weather_report(available_cities)