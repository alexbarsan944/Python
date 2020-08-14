# b) Write a module named app.py. When this module is run, it will run in an infinite loop, waiting for inputs from
# the user. The program will convert the input to a number and process it using the function process_item implemented
# in utils.py. You will have to import this function in your module. The program stops when the user enters the
# message "q"


import utils as ut

while True:
    x = input("Input variable:")
    if x == 'q':
        print("Exiting ... ")
        break
    print(ut.process_item(int(x)))
