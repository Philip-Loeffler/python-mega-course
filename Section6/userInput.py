def weather_conditions(temperature):
    if temperature > 7:
        return "Warm"
    else:
        return "Cold"

# message you're showing to the user on command line
# need to convert the user input to a float
user_input = float(input("enter temp"))
print(user_input.lower())


# any user input will be a string, so you must convert the type. dont really know why python thinks that a cool thing to do
print(weather_conditions(user_input))