temps = [221, 234, 340, 230]

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# or you can do this with list comprehensions 
# same thing as above, but in one line
newer_temps = [temp / 10 for temp in temps]
print(newer_temps)