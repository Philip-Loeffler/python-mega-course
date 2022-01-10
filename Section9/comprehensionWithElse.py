temps = [221, 234, 340, -9999, 230]

# if if/else is inside a list comprehension the expression is flipped and you would see the for loop at the end
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)
