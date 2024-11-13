# writing to a file example

import random


def main():
    outfile = open('data2.txt' , 'a')

    employee = input("Enter the Employee's name: ")
    salary = random.randint(35000,50000)

    outfile.write(employee + '\n')
    outfile.write("$" + str(salary) + "\n")

    outfile.close()

main()