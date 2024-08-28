months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if date.count("/") == 2:
        month, day, year = date.split("/")
        try:
            month = int(month)
            day = int(day)
            year = int(year)
        except ValueError:
            pass
        else:
            if month <= 12 and day <=31 and year <=9999:
                print(f"{year:04}-{month:02}-{day:02}")
                break
    elif "," in date:
        month, day, year = date.split(" ")
        if any(mon in month for mon in months):
            year = int(year)
            day = int(day.replace(",", ""))
            if day <=31 and year <=9999:
                print(f"{year:04}-{int(months.index(month)+1):02}-{day:02}")
                break
