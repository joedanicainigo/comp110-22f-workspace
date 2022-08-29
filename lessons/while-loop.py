"""An example of a while loop statmenet."""

counter: int = 0
maximum: int = int(input("Count up to, but not including what?"))
while counter < maximum:
    counter_squared: int = counter ** 2 # compute the square
    print("The square of " + str(counter) + " is " +str(counter_squared))
    counter = counter + 1

print ("Done!")