##program to convert temperature in centigrade to fahrenheit
cent=float(input("Enter the temperature in centigrade:"))
'''why do we multiply with 9/5?
on celsius scale:0 degrees->freezing,100 degrees->boiling=>100 units
on fahrenheit:32 degrees->freezing,212 degrees->boiling=>180 units
1 degree celsius=180/100=9/3 degree in F
we add 32 because 0 degree in celsius corresponds to 32F
formula=>F=(c*(9/5))+32'''
fahrenheit=9/5*cent+32
print(f"The converted temperature is {fahrenheit:.2f}")
