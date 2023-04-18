import csv
import mysql.connector

def importBasicInfo(mydb):
    table = {'nothing': -1}
    with open('data/new_neighborhood.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)
        for row in csv_data:
            table[row[1]] = row[0]
    with open('data/basic_info.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO basic_info (house_id, name, description, renter_id, price, room_type, bathrooms, bedrooms, beds, host_id, neighborhood_id, property) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                if (not row[14] in table):
                    continue
                val = (
                row[0], row[1], row[2], row, row[4][1:], row[6], row[7], row[8], row[9], row[13], table[row[14]], row[15])

                if (len(val[0]) < 1):
                    continue
                try:
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

def importHost(mydb):
    # Import basic_info table
    with open('data/host.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO host (host_id, since, response_time, response_rate, acceptance_rate) VALUES (%s, %s, %s, %s, %s)"
                val = (row[0], row[2], row[4], row[5], row[6])
                if (len(val[0]) < 1):
                    continue

                try:
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

def importNeighborhood(mydb):
    # Import basic_info table
    with open('data/new_neighborhood.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO neighborhood (neighborhood_id, name, city, latitude, longitude) VALUES (NULL, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3])
                if (len(val[0]) < 1):
                    continue
                try:
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

def importCalendar(mydb):
    # Import basic_info table
    with open('data/calendar.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO calendar (calendar_id, house_id, date, price) VALUES (NULL, %s, %s, %s)"
                val = (row[1], row[2], row[4])
                if (len(val[0]) < 1):
                    continue
                val = (row[1], row[2], row[4][1:])
                try:
                    mycursor.execute(sql, val)
                    mydb.commit()
                    if(ptr % 100 == 0):
                        print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

def importReviews(mydb):
    # Import basic_info table
    with open('data/reviews.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO reviews (review_id, house_id, date, reviewer_id, comments) VALUES (%s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4])
                if (len(val[0]) < 1):
                    continue
                try:
                    mycursor.execute(sql, val)
                    mydb.commit()
                    if(ptr % 100 == 0):
                        print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

def importUser(mydb):
    # Import basic_info table
    '''with open('data/host.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO user (user_id, name, about, is_host) VALUES (%s, %s, %s, \"t\")"
                val = (row[0], row[1], row[3])
                if (len(val[0]) < 1):
                    continue

                try:
                    mycursor.execute(sql, val)
                    mydb.commit()
                    print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1'''

    with open('data/reviews.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO user (user_id, name, is_host) VALUES (NULL, \"" + row[4] + "\", \"f\")"

                try:
                    mycursor.execute(sql)
                    mydb.commit()
                    print("Row" + str(ptr) + " has been imported successfully!")
                except Exception as e:
                    print("Line" + str(ptr) + ' Error:', e)
                    mydb.rollback()
                ptr += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

def importAmenities(mydb):
    # Import basic_info table
    with open('data/basic_info.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                house_id = row[0]
                amenities = row[10]
                sql = "INSERT INTO amenities (house_id, amenity) VALUES (%s, %s)"
                tag = False
                ind = 0
                i = 0
                while(len(amenities) > 0):
                    i += 1
                    if(i > 4096):
                        break
                    if(len(amenities) <= ind):
                        break
                    if(amenities[ind] == "\""):
                        if(not tag):
                            tag = True
                            ind = 1
                        else:
                            tag = False
                            val = (house_id, amenities[1:ind])
                            if (len(val[0]) < 1):
                                continue

                            try:
                                mycursor.execute(sql, val)
                                mydb.commit()
                                print("Row" + str(ptr) + " has been imported successfully!")
                            except Exception as e:
                                print("Line" + str(ptr) + ' Error:', e)
                                mydb.rollback()
                            ptr += 1
                            amenities = amenities[ind + 1:]
                            ind = 0
                    else:
                        if(not tag):
                            amenities = amenities[1:]
                        else:
                            ind += 1
            else:
                print("Row" + str(ptr) + " is skipped!")
                ptr += 1
    mycursor.close()

if __name__=="__main__":

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="656project"
    )

    # Using functions below to import data

    importUser(mydb)
    #importHost(mydb)
    #importNeighborhood(mydb)
    #importBasicInfo(mydb)
    #importAmenities(mydb)
    #importCalendar(mydb)
    #importReviews(mydb)


