# writing to a file example

def read_and_write_file():
    outfile = open('data.txt', 'w') # 'w' means write mode

    new_account = input("Please enter your name: ") # im assuming that I can just call the varible when doing this in the lab 
    initial_balance = input("Please enter your last name: ")    # ^^^^^

    outfile.write(new_account + '\n')
    outfile.write(initial_balance + '\n') # hypothetically of what it would look like in the program

    outfile.close

read_and_write_file()

"""
What i mean by is that after the whole process of adding a new acount
i then run this program and can have everything the user did abobve
go to the data.txt


https://www.youtube.com/watch?v=0C2405R-uGk



"""