# example somone order from your resturent 2 iteam 
def order(iteam1,iteam2):
    print("costomer order: ",iteam1,"and",iteam2)

order("baryani","pepsi")

# example some one order alot of iteam 
# by single iteam get alot of orders

def orders(*iteams):
    print("custmer order: ",iteams)
    
orders("pepsi","baryani","fiza","kabab","fish")

# Imagine a customer orders:
# - Biryani: Rs. 350
# - Chicken karahi: Rs. 800
# - Pepsi: Rs. 100
# - Fries: Rs. 200
# - Ice cream: Rs. 150
# You want Python to calculate the total
# automatically, regardless of how many items the 
# customer order

def calculate_bill(*prices):
    total=0
    
    
    for price in prices:
        total+=price
    print("the total bill are: ",total)
calculate_bill(319,405,342,342,646,560)

# kwargs — Keyword arguments
# kwargs is a conventional name meaning keyword arguments.
# Just like args, the word kwargs is not compulsory. The double asterisk provides the special behavior.
# For example:

def caustomer_detail(**namebill,):
    print(namebill)
    
    
caustomer_detail(name="Rohail",food="baryani",drink="pepsi")

# Let's build a slightly more interesting program.
# Your restaurant manager says:
# "Every customer is different! One wants home delivery, another wants takeaway, and another wants to eat at the restaurant. Build a system that accepts whatever details the customer provides."
# We can use **kwargs to create a flexible customer-information function.

def customer_order(**kwargs):
    print("\n===== ROHAIL'S RESTAURANT =====")

    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print("===============================")


customer_order(
    name="Rohail",
    food="Chicken Biryani",
    drink="Pepsi",
    payment="Cash",
    delivery="Home Delivery"
)

# Finding the maximum value:
def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_value = numbers[0]
  for num in numbers:
    if num > max_value:
      max_value = num
  return max_value

print(my_function(3, 7, 2, 9, 1))