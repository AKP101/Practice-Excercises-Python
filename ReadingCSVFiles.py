import csv #comma separated variables

with open("example.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    dates = []
    colors = []


    #for row in readCSV:
        #print(row)
        #print(row[0])
        #print(row[0], row[1])
        
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)
        
    print()
    print(dates)
    print(colors)
    
    try:
        
        whatColor = input("What colour for date: ")
        if whatColor in colors:
            coldex = colors.index(whatColor.lower())
            thedate = dates[coldex]
            print("The date is: " + thedate)
        else:
            print("Ya done goofed my man >:(")
    except Exception as e:
        print(e)
        print("continuing")
            
