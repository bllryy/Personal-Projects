def main():
    # get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    # split into components 
    monthStr, dayStr, yearStr = dateStr.split("/")

    # convert monthStr to month name
    months = ["January", "Febuary", "March", "April",
              "May", "July", "August",
              "September", "October", "November", "December"]
    monthStr = months[int(monthStr)-1]

    # output result in month day, year format
    print("The converted date is:", monthStr, dayStr+",", yearStr)

main()