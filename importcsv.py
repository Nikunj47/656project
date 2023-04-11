import csv
import mysql.connector

#Do not use this function, try using setNeighborhoodId()
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
                sql = "INSERT INTO basic_info (house_id, name, description, instant_bookable, price, availability, room_type, bathrooms, bedrooms, beds, amenities, numbers_of_reviews, review_score, host_id, neighborhood_id, property) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                if (not row[14] in table):
                    continue
                val = (
                row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10], row[11],
                row[12], row[13], table[row[14]], row[15])

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
                sql = "INSERT INTO host (host_id, name, since, about, response_time, response_rate, acceptance_rate, identity_verified) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if (len(val[0]) < 1):
                    continue
                if len(val[1]) > 44:
                    val = (row[0], row[1][:44], row[2], row[3], row[4], row[5], row[6], row[7])
                if len(val[2]) > 20:
                    val = (row[0], row[1], row[2][:20], row[3], row[4], row[5], row[6], row[7])
                if len(val[3]) > 199:
                    val = (row[0], row[1], row[2], row[3][:199], row[4], row[5], row[6], row[7])
                if len(val[4]) > 44:
                    val = (row[0], row[1], row[2], row[3], row[4][:44], row[5], row[6], row[7])
                if len(val[5]) > 44:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5][:44], row[6], row[7])
                if len(val[6]) > 44:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6][:44], row[7])
                if len(val[7]) > 4:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7][:4])

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
                if len(val[0]) > 44:
                    val = (row[0][:44], row[1], row[2], row[3])
                if len(val[1]) > 44:
                    val = (row[0], row[1][:44], row[2], row[3])
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
                sql = "INSERT INTO calendar (calendar_id, house_id, date, available, price, adjusted_price, minimum_nights, maximum_nights) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if (len(val[0]) < 1):
                    continue
                if len(val[3]) > 4:
                    val = (row[1], row[2], row[3][:4], row[4], row[5], row[6], row[7])
                val = (row[1], row[2], row[3], row[4][1:], row[5][1:], row[6], row[7])
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
                sql = "INSERT INTO reviews (review_id, house_id, date, reviewer_name, comments) VALUES (%s, %s, %s, %s, %s)"
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

if __name__=="__main__":

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="656project"
    )

    # Using functions below to import data

    importHost(mydb)
    importNeighborhood(mydb)
    importBasicInfo(mydb)
    importCalendar(mydb)
    importReviews(mydb)


