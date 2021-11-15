# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# part 1
leek_price = 2
print("Leek is " + str(leek_price) + " euro per kilo.")

# part 2
first_order = "leek 4"
sum_total = int(first_order[first_order.find("4"):]) * leek_price
print(sum_total)

# part 3
broccoli_price = 2.34
broccoli_order = "broccoli 1.6"
print(broccoli_order[broccoli_order.find("1"):] + "kg broccoli costs " + str(round(float(broccoli_order[broccoli_order.find("1"):]) * broccoli_price, 2)) + "e")