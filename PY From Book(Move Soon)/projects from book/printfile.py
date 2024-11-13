def main():
    fname = input("Enter a file name: ")
    infile = open(fname, "r")
    data = infile.read()
    print(data)

main()