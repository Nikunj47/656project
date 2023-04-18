import mysql.connector
import datetime

def MainPage(mydb):
    while (True):
        print("--------------------------------")
        print("Welcome to house renting system!")
        print("Press 1 to move to housing market.")
        print("Press 2 to check host list.")
        print("Press 3 to access into host panel.")
        print("Press 0 to exit program.")

        selected = input()
        if (selected == "1"):
            print("--------------------------------")
            HouseList(mydb)
        elif (selected == "2"):
            print("--------------------------------")
            HostList(mydb)
        elif (selected == "3"):
            print("--------------------------------")
            HostPanel(mydb)
        elif (selected == "0"):
            break

    print("Bye~")


def HouseList(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to housing market")

    id = input("Input id of house. You can input null to skip this filter.")
    name = input("Input key words in name to search. You can input null to skip this filter.")
    neighborhood = input("Input key words in neighborhood to search. You can input null to skip this filter.")
    bookable = input("Is the house instant bookable? t for true and f for false, null to skip this filter.")
    bathrooms = input("Input how many bathrooms you want. You can input null to skip this filter")
    bedrooms = input("Input how many bedrooms you want. You can input null to skip this filter")

    sqlquery = "select * from listing where 1=1"

    if(id != "null"):
        sqlquery = sqlquery + " and listingid = \"" + id + "\""
    if(name != "null"):
        sqlquery = sqlquery + " and listingname like \"%" + name + "%\""
    if(neighborhood != "null"):
        sqlquery = sqlquery + " and neighborhood like \"%" + neighborhood + "%\""
    if (bookable != "null"):
        sqlquery = sqlquery + " and instant_bookable = \"" + bookable + "\""
    if (bedrooms != "null"):
        sqlquery = sqlquery + " and bedrooms >= " + bedrooms
    if (bathrooms != "null"):
        sqlquery = sqlquery + " and bathrooms >= " + bathrooms
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
            print("-Street: " + x[2])
            print("-Neighborhood: " + x[3])
            print("-City: " + x[4])
            print("-State: " + x[5])
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    index = input("Input the index of house you what to know more. Input 0 to exit: ")
    if(int(index) == 0):
        return
    if(int(index) >= 0 and int(index) < len(result)):
        houseId = result[int(index)][0]
        sqlquery = "select * from listing inner join bedtype on listing.bedtypeid = bedtype.bedtypeid "
        sqlquery = sqlquery + "inner join roomtype on listing.roomtypeid = roomtype.roomtypeid inner join propertytype on listing.propertytypeid = propertytype.propertytypeid "
        sqlquery = sqlquery + "inner join listing_has_amenities on listing.listingid = listing_has_amenities.listingid "
        sqlquery = sqlquery + "inner join amenities on listing_has_amenities.AmenityID = amenities.AmenityID "
        sqlquery = sqlquery + "inner join host_has_listing on host_has_listing.listingid = listing.listingid "
        sqlquery = sqlquery + "inner join host on host_has_listing.hostid = host.hostid "
        sqlquery = sqlquery + "where listing.listingid = \"" + str(houseId) + "\";"

        try:
            mycursor.execute(sqlquery)
            mydb.commit()
            result = mycursor.fetchall()
            print("")
            print("House Information: ")
            print("-Id: " + str(result[0][0]))
            print("-Name: " + str(result[0][1]))
            print("-Price: " + str(result[0][26]))
            print("-Street " + str(result[0][2]))
            print("-Neighborhood: " + str(result[0][3]))
            print("-City: " + str(result[0][4]))
            print("-State: " + str(result[0][5]))
            print("-Zip Code: " + str(result[0][6]))
            print("-Bathrooms: " + str(result[0][7]))
            print("-Bedrooms: " + str(result[0][8]))
            print("-Beds: " + str(result[0][9]))
            print("-Instant Bookable: " + str(result[0][10]))
            print("-Bed Type: " + str(result[0][15]))
            print("-Room Type: " + str(result[0][17]))
            print("-Property Type: " + str(result[0][19]))
            print("-Number of Reviews: " + str(result[0][27]))
            print("-Review Scores: " + str(result[0][28]))
            print("-Amenities:", end = " ")
            for x in result:
                print(x[23], end = ", ")
            print("")

            print("Host Information: ")
            print("-Id: " + str(result[0][29]))
            print("-Name: " + str(result[0][30]))
            print("-Host Since: " + str(result[0][31]))
            print("-City " + str(result[0][32]))
            print("-Neighborhood: " + str(result[0][33]))
            print("-State: " + str(result[0][34]))
            print("-Identity Verified: " + str(result[0][35]))

        except Exception as e:
            print("Database error: ", e)
            mydb.rollback()

        while(True):
            print("")
            print("-------------------------------")
            print("Input 1 to show booking history.")
            print("Input 0 to leave this page.")
            r = input()

            if(r == "1"):
                sqlquery = "select date, price from booking where listingid = \"" + str(houseId) + "\" and price != \"\" order by date desc;"
                try:
                    mycursor.execute(sqlquery)
                    mydb.commit()
                    res = mycursor.fetchall()
                    if (len(res) == 0):
                        print("No results returned!")
                    else:
                        print("")
                        print("Price History: ")
                    for x in res:
                        print("In " + str(x[0]) + " the price of this house is " + str(x[1]))
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
        sqlquery = sqlquery + " and hostid = \"" + id + "\""
    if(name != "null"):
        sqlquery = sqlquery + " and hostname like \"%" + name + "%\""
    if(since != "null"):
        sqlquery = sqlquery + " and year(hostsince) < \"" + since + "\""
    if(verified != "null"):
        sqlquery = sqlquery + " and hostidentityverified = \"" + verified + "\""
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
            print("-City: " + x[3])
            print("-Neighborhood: " + x[4])
            print("-State: " + x[5])
            print("-Identity Verified: " + x[6])
            i = i + 1
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    mycursor.close()

def HostPanel(mydb):
    mycursor = mydb.cursor(buffered=True)
    print("Welcome to Host Management Panel!")
    hostid = input("Please input your host id.")

    sqlquery = "select * from host where hostid = \"" + hostid + "\";"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        result = mycursor.fetchall()
        if(len(result) == 0):
            print("Wrong host id inputed！")
            return
        else:
            print("Welcome to host panel!")
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

    while(True):
        sqlquery = "select * from listing inner join host_has_listing on listing.listingid = host_has_listing.listingid where "

        sqlquery = sqlquery + "hostid = \"" + hostid + "\";"
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
                print("-Street: " + str(x[2]))
                print("-Neighborhood: " + str(x[3]))
                print("-City: " + x[4])
                print("-State: " + str(x[5]))
                print("-Price: " + str(x[16]))
                i = i + 1
        except Exception as e:
            print("Database error: ", e)
            mydb.rollback()

        print("")
        print("Press 1 to change an existing house")
        print("Press 2 to delete an existing house")
        print("Press 0 to exit host panel.")
        ch = input()
        if(ch == "0"):
            break
        elif(ch == "1"):
            ChangeHouse(mycursor, result)
        elif(ch == "2"):
            DeleteHouse(mycursor, result)

    mycursor.close()

def ChangeHouse(mycursor, result):
    index = input("Input the index of house you want to change")
    if (int(index) <= 0 or int(index) > len(result)):
        print("Index don't exist!")
        return

    price = input("Input new price.")
    tag = False

    if(price == "null"):
        print("Don't input new price!")
    else:
        sqlquery = "update host_has_listing set daily_price = \"" + price + "\" where listingid = \"" + str(result[int(index) - 1][0]) + "\";"

    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        print("Change house successfully!")
    except Exception as e:
        print("Database error: ", e)
        mydb.rollback()

def DeleteHouse(mycursor, result):
    index = input("Input the index of house you want to delete")
    if (int(index) <= 0 or int(index) > len(result)):
        print("Index don't exist!")
        return

    sqlquery = "DELETE FROM host_has_listing WHERE listingid = \"" + str(result[int(index) - 1][0]) + "\";"
    try:
        mycursor.execute(sqlquery)
        mydb.commit()
        print("Deleted Successfully!")
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
        database="airbnb"
    )

    MainPage(mydb)