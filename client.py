import mysql.connector

def MainPage(mydb):
    while(True):
        print("--------------------------------")
        print("Welcome to House Renting System!")
        print("Press 1 to check house list.")

        selected = input()
        if(selected == "1"):
            end = HouseList(mydb)

def HouseList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("--------------------------------")
    print("Welcome to Check House List!")
    name = input("Input name to search. You can input null to skip this filter.")
    bookable = input("Is the house instant bookable? t for true and f for false, null to skip this filter.")
    bedrooms = input("Input how many bedrooms you want. You can input null to skip this filter")
    print("Which kind of room type do you want?")
    print("Press 1 to choose Entire Home / Apt")
    print("Press 2 to choose Private Room")
    print("Press 3 to choose Shared Room")
    print("Press 4 to choose Hotel Room")
    print("You can input null to skip this filter.")
    room_type = input()

    sqlquery = "select * from basic_info where 1=1"

    if(name != "null"):
        sqlquery = sqlquery + " and name = \"" + name + "\""
    if (bookable != "null"):
        sqlquery = sqlquery + " and instant_bookable = \"" + bookable + "\""
    if (bedrooms != "null"):
        sqlquery = sqlquery + " and bedrooms >= " + bedrooms
    if (room_type != "null"):
        if(room_type == "1"):
            sqlquery = sqlquery + " and room_type = \"Entire home / apt\""
        if(room_type == "2"):
            sqlquery = sqlquery + " and room_type = \"Private room\""
        if(room_type == "3"):
            sqlquery = sqlquery + " and room_type = \"Shared room\""
        if(room_type == "4"):
            sqlquery = sqlquery + " and room_type = \"Hotel room\""
    sqlquery = sqlquery + " limit 10;"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        result = mycursor.fetchall()
        i = 1
        for x in result:
            print("")
            print("Result #" + str(i))
            print("-Name: " + x[1])
            print("-Price: $" + str(x[4]))
            print("-Room type: " + x[6])
            print("-Review score: " + str(x[12]))
            print("-Bathrooms: " + x[7])
            print("-Bedrooms: " + str(x[8]))
            print("-Beds: " + str(x[9]))
            print("-Amenities: " + x[10])
            print("-Description: " + x[2])
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    mycursor.close()

    return True

if __name__=="__main__":


    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="656project"
    )

    MainPage(mydb)