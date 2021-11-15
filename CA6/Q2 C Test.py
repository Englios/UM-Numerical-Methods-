import numpy as np
import matplotlib.pyplot as mpl


# Explanation on how the code works:-
# It works by setting a range for the step size,
# For Example from 1 to 100,The user has to put the numbers as requested,
# but to display from 1 to 100 will take a lot of CPU power,
# Therefore to avoid that the user has to put another value of step in it.
# Lets say the value is 2.Then the code will only print the euler's method when n=1,3,4....100
# To only see when N=100,the user needs to put 100 as the lower and upper value then put 1 as the interval size.
# The individual values will only print when the user enters yes and
# the graph will only be labelled if the amount of n to show is less than 5
# Why did i do this?Well i was bored and since the question didn't specify a stopping point,i just went with it :p

# define the Formula
def f(x, y, i):
    return -y[i] * np.log(y[i])


# define for exact method graph
z = np.linspace(0, 1, 1000)
exact = np.exp(np.log(3) * np.exp(-z))

print("WARNING!!!"
      "\n"
      "a BIG Limit interval will take a long time and may reduce the lifespan of your CPU"
      "\n")

low = int(input("Enter Lower limit for stepsize: "))
upper = int(input("Enter Upper limit for stepsize: "))

# check whether the value van be used or not
while upper < low or low <= 0:
    if low <= 0:
        low = int(input("Error Lower Value cannot be less than 1"
                        "\n"
                        "Please re-enter Lower limit: "))
    if upper < low:
        upper = int(input("Error Upper limit Cannot be less than Lower limit"
                          "\n"
                          "Please Re-enter Upper limit: "))

# enters the interval
interval = int(input("Enter Interval in between the values : "))
interval = abs(interval)

# check The choice whether or not if the user wants to see each value of iteration
choice = str(input("\nPrint for every value of each iteration?"
                   "\n"
                   "This will take time if your max limit is big and step size is "
                   "small."
                   "\n"
                   "Type in 'Yes' to print it"
                   "\n"))

# Loop until all iteration value is satisfied
for n in range(low, upper + 1, interval):
    # Initializing Values
    h = 1 / n
    y = [0.00] * (n + 2)
    x = [0.00] * (n + 2)
    y[0] = 3
    x[0] = 0
    i = 0

    # Euler's method calculation
    for i in range(n + 1):
        y[i + 1] = y[i] + h * f(x, y, i)
        x[i + 1] = x[i] + h

        # print individual values when the choice is entered as yes
        if choice == 'yes' or choice == 'Yes' or choice == 'YES':
            print("Iteration Number {0:2d}"
                  "\n"
                  "||I = {0:2d} "
                  "|| X[{0:2d}] Value = {2:10.8f}"
                  "|| Y[{0:2d}] Value = {3:10.8f}"
                  "|| Y[{1:2d}] Value = {4:10.8f}"
                  "\n"
                  .format(i, i + 1, x[i], y[i], y[i + 1]))
        else:
            pass

    print('\n\n')

    # plot with labelling
    if (upper - low) / interval <= 10:
        # only plot the graph until x=1
        mpl.plot(x[0:n + 1], y[0:n + 1],
                 label="Euler's Method when n={0}".format(n),
                 linewidth=0.5,
                 marker='.',
                 markersize=2.5
                 )
    # plot without labelling
    else:
        # only plot the graph until x=1
        mpl.plot(x[0:n + 1], y[0:n + 1],
                 linewidth=0.5,
                 marker='.',
                 markersize=2.5
                 )

# labeling the graph
mpl.ylabel("F(x)")
mpl.xlabel("X")
mpl.plot(z, exact, "k", label='Exact Solution')
mpl.legend()

# annotate the graph only when 2 or more data is given
if (upper - low) / interval > 1:
    mpl.annotate("Euler's method is getting closer \nto the exact equation as n increases",
                 xy=(0, 1.5), verticalalignment='bottom', horizontalalignment='left', )

mpl.show()
