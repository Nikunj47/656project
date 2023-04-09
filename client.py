import mysql.connector
import datetime

def MainPage(mydb):
    while(True):
        print("--------------------------------")
        print("Welcome to House Renting System!")
        print("Press 1 to check house list.")
        print("Press 2 to check neighborhood list.")
        print("Press 3 to check host list.")
        print("Press 4 to check review.")
        print("Press 5 to check calendar.")
        print("Press 6 to access into host panel.")
        print("Press 7 to sign up as a host.")
        print("Press 8 to write a review.")
        print("Press 0 to exit program.")

        selected = input()
        if (selected == "1"):
            print("--------------------------------")
            HouseList(mydb)
        elif (selected == "2"):
            print("--------------------------------")
            NeighborhoodList(mydb)
        elif (selected == "3"):
            print("--------------------------------")
            HostList(mydb)
        elif (selected == "4"):
            print("--------------------------------")
            ReviewList(mydb)
        elif (selected == "5"):
            print("--------------------------------")
            CalendarList(mydb)
        elif (selected == "6"):
            print("--------------------------------")
            HostPanel(mydb)
        elif (selected == "7"):
            print("--------------------------------")
            AddHost(mydb)
        elif (selected == "8"):
            print("--------------------------------")
            AddReview(mydb)
        elif (selected == "0"):
            break

def HouseList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Check House List!")
    id = input("Input id of house. You can input null to skip this filter.")
    name = input("Input key words in name to search. You can input null to skip this filter.")
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


    if(id != "null"):
        sqlquery = sqlquery + " and house_id = \"" + id + "\""
    if(name != "null"):
        sqlquery = sqlquery + " and name like \"%" + name + "%\""
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
            print("-Id: " + str(x[0]))
            print("-Name: " + x[1])
            print("-Price: $" + str(x[4]))
            print("-Availability: " + str([5]))
            print("-Instance Bookable: " + x[3])
            print("-Review score: " + str(x[12]))
            print("-Room type: " + x[6])
            print("-property: " + x[15])
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

def NeighborhoodList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Check Neighborhood List!")
    id = input("Input id of neighborhood. You can input null to skip this filter.")
    name = input("Input key words in name to search. You can input null to skip this filter.")
    city = input("Input the keyword of city. You can input null to skip this filter.")
    sqlquery = "select * from neighborhood where 1=1"

    if(id != "null"):
        sqlquery = sqlquery + " and neighborhood_id = \"" + id + "\""
    if(name != "null"):
        sqlquery = sqlquery + " and name like \"%" + name + "%\""
    if(city != "null"):
        sqlquery = sqlquery + " and city like \"%" + city + "%\""
    sqlquery = sqlquery + " limit 10;"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        result = mycursor.fetchall()
        i = 1
        if(len(result) == 0):
            print("No results returned!")
        for x in result:
            print("")
            print("Result #" + str(i))
            print("-Id: " + str(x[0]))
            print("-Name: " + x[1])
            print("-City: " + x[2])
            print("-Latitude: " + str(x[3]))
            print("-Longitude: " + str(x[4]))
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    mycursor.close()

def HostList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Check Host List!")
    id = input("Input id of host. You can input null to skip this filter.")
    name = input("Input key words in name to search. You can input null to skip this filter.")
    since = input("Input the year the host to have become a host before. You can input null to skip this filter.")
    verified = input("Input the host is verified or not. t for true and f for false, null for skip this filter.")
    sqlquery = "select * from host where 1=1"

    if(id != "null"):
        sqlquery = sqlquery + " and host_id = \"" + id + "\""
    if(name != "null"):
        sqlquery = sqlquery + " and name like \"%" + name + "%\""
    if(since != "null"):
        sqlquery = sqlquery + " and year(since) < \"" + since + "\""
    if(verified != "null"):
        sqlquery = sqlquery + " and identity_verified = \"" + verified + "\""
    sqlquery = sqlquery + " limit 10;"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        result = mycursor.fetchall()
        i = 1
        if(len(result) == 0):
            print("No results returned!")
        for x in result:
            print("")
            print("Result #" + str(i))
            print("-Id: " + str(x[0]))
            print("-Name: " + x[1])
            print("-Since: " + str(x[2]))
            print("-About: " + x[3])
            print("-Response Time: " + x[4])
            print("-Response Rate: " + x[5])
            print("-Acceptance Rate: " + x[6])
            print("-Identity Verified: " + x[7])
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    mycursor.close()

def ReviewList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Check Review List!")
    id = input("Input id of house.")
    date = input("Input the year the review posted after. You can input null to skip this filter.")
    sqlquery = "select * from reviews where 1=1"

    if(id != "null"):
        sqlquery = sqlquery + " and house_id = \"" + id + "\""
    if(date != "null"):
        sqlquery = sqlquery + " and year(date) > \"" + date + "\""
    sqlquery = sqlquery + " limit 10;"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        result = mycursor.fetchall()
        i = 1
        if(len(result) == 0):
            print("No results returned!")
        for x in result:
            print("")
            print("Result #" + str(i))
            print("-Date: " + str(x[2]))
            print("-Reviewer Name: " + x[3])
            print("-Comments: " + x[4])
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    mycursor.close()

def CalendarList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Check Calendar List!")
    id = input("Input id of house.")
    year = input("Input the year you want to search.")
    month = input("Input the month you want to search.")
    day = input("Input the day you want to search.")
    sqlquery = "select * from calendar where 1=1"

    if(id != "null"):
        sqlquery = sqlquery + " and house_id = \"" + id + "\""
    if(year != "null"):
        sqlquery = sqlquery + " and year(date) = \"" + year + "\""
    if(month != "null"):
        sqlquery = sqlquery + " and month(date) = \"" + month + "\""
    if(day != "null"):
        sqlquery = sqlquery + " and day(date) = \"" + day + "\""
    sqlquery = sqlquery + " limit 10;"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        result = mycursor.fetchall()
        i = 1
        if(len(result) == 0):
            print("No results returned!")
        for x in result:
            print("")
            print("Result #" + str(i))
            print("-Date: " + str(x[2]))
            print("-Available: " + x[3])
            print("-Price: $" + str(x[4]))
            if(x[4] != x[5]):
                print("-Adjusted Price: $" + str(x[5]))
            print("-Minimum Nights: " + str(x[6]))
            print("-Maximum Nights: " + str(x[7]))
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    mycursor.close()

def HostPanel(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Host Management Panel!")
    hostid = input("Please input your host id.")

    while(True):
        sqlquery = "select * from basic_info where "

        sqlquery = sqlquery + "host_id = \"" + hostid + "\";"
        try:
            mycursor.execute(sqlquery)
            mydb.commit()
            result = mycursor.fetchall()
            i = 1
            print("Here is your house list: ")
            for x in result:
                print("")
                print("Result #" + str(i))
                print("-Id: " + str(x[0]))
                print("-Name: " + x[1])
                print("-Price: $" + str(x[4]))
                print("-Availability: " + str(x[5]))
                print("-Instance Bookable: " + x[3])
                print("-Review score: " + str(x[12]))
                print("-Room type: " + x[6])
                print("-property: " + x[15])
                print("-Bathrooms: " + x[7])
                print("-Bedrooms: " + str(x[8]))
                print("-Beds: " + str(x[9]))
                print("-Amenities: " + x[10])
                print("-Description: " + x[2])
                i = i + 1
        except Exception as e:
            print("Database error: ", e)
            mydb.rollback()

        print("")
        print("Press 1 to add a new house")
        print("Press 2 to change an existing house")
        print("Press 3 to delete an existing house")
        print("Press 0 to exit host panel.")
        ch = input()
        if(ch == "0"):
            break
        elif(ch == "1"):
            AddHouse(mycursor)
        elif(ch == "2"):
            ChangeHouse(mycursor, result)
        elif(ch == "3"):
            DeleteHouse(mycursor, result)

    mycursor.close()

def AddHouse(mycursor):#not test
    name = input("Input name of new house.")
    description = input("Input description of new house.")
    price = input("Input price of new house.")
    availability = input("Input availability of new house.")
    print("Input room type of new house. 1 for Entire home. 2 for Private room. 3 for Shared room. 4 for Hotel room")
    room_type = input()
    if(room_type == "1"):
        room_type = "Entire home"
    if(room_type == "2"):
        room_type = "Private room"
    if(room_type == "3"):
        room_type = "Shared room"
    if(room_type == "4"):
        room_type = "Hotel room"
    bathrooms = input("Input number of bathrooms of new house.")
    bedrooms = input("Input number of bedrooms of new house.")
    beds = input("Input number of beds of new house.")
    amenities = input("Input amenities of new house.")
    neighborhood_id = input("Input neiborhood id of new house.")
    property = input("Input property of new house.")

    sqlquery = "INSERT INTO basic_info (house_id, name, description, instant_bookable, price, availability, room_type, bathrooms, bedrooms, beds, amenities,"
    sqlquery = sqlquery + " numbers_of_reviews, review_score, host_id, neighborhood_id, property) VALUES (NULL, \""
    sqlquery = sqlquery + name + "\", \"" + description + "\", \"" + price + "\", \"" + availability + "\", \"" + room_type + "\", \"" + bathrooms + "\", \"" + bedrooms
    sqlquery = sqlquery + "\", \"" + beds + "\", \"" + amenities + "\", \"" + neighborhood_id + "\", \"" + property + "\");"

    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

def ChangeHouse(mycursor, result):
    index = input("Input the index of house you want to change")
    if (int(index) <= 0 or int(index) > len(result)):
        print("Index don't exist!")
        return

    description = input("Input new description. Input null to skip changing.")
    price = input("Input new price. Input null to skip changing.")
    availability = input("Input new availability. Input null to skip changing.")
    tag = False

    if(description == "null" and price == "null" and availability == "null"):
        return
    sqlquery = "UPDATE basic_info "
    if(description != "null"):
        if(not tag):
            tag = True
        else:
            sqlquery = sqlquery + "and "
        sqlquery = sqlquery + "set description = \"" + description + "\" "
    if(price != "null"):
        if(not tag):
            tag = True
        else:
            sqlquery = sqlquery + "and "
        sqlquery = sqlquery + "set price = \"" + price + "\" "
    if(availability != "null"):
        if(not tag):
            tag = True
        else:
            sqlquery = sqlquery + "and "
        sqlquery = sqlquery + "set availability = \"" + availability + "\" "
    sqlquery = sqlquery + "WHERE house_id = \"" + str(result[int(index) - 1][0]) + "\";"

    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

def DeleteHouse(mycursor, result):
    index = input("Input the index of house you want to delete")
    if (int(index) <= 0 or int(index) > len(result)):
        print("Index don't exist!")
        return

    sqlquery = "DELETE FROM calendar WHERE house_id = \"" + str(result[int(index) - 1][0]) + "\";"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()
        return

    sqlquery = "DELETE FROM reviews WHERE house_id = \"" + str(result[int(index) - 1][0]) + "\";"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()
        return

    sqlquery = "DELETE FROM basic_info WHERE house_id = \"" + str(result[int(index) - 1][0]) + "\";"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        print("Deleted Successfully!")
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()
        return


def AddHost(mycursor):  # not test
    name = input("Input name of you.")
    about = input("Input description of you.")

    sqlquery = "INSERT INTO basic_info (host_id, name, since, about, identity_verified) VALUES (NULL, \"" + name + "\", \""
    sqlquery = sqlquery + str(datetime.date.today()) + "\", \"" + about + "\", \"f\");"

    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()


def AddReview(mycursor):  # not test
    house_id = input("Input house id.")
    name = input("Input your name.")
    comments = input("Input comments.")

    sqlquery = "INSERT INTO basic_info (review_id, house_id, date, reviewer_name, comments) VALUES (NULL, \""
    sqlquery = sqlquery + house_id + "\", \"" + str(datetime.date.today()) + "\", \"" + name + "\", \"" + comments + "\");"

    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()
        return

    sqlquery = "update basic_info set numbers_of_reviews = numbers_of_reviews + 1 where house_id = \"" + house_id + "\";"

    try:
        mycursor.execute(sqlquery)
        mydb.commit()
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()
        return

if __name__=="__main__":


    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="656project"
    )

    MainPage(mydb)