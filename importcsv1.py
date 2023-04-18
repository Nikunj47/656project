import csv
import datetime

import mysql.connector

def importAmenities(mydb):
    with open('airbnb/Amenities.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO amenities (AmenityID, AmenityDescription) VALUES (%s, %s)"
                val = (row[0], row[1])

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

def importBedType(mydb):
    # Import basic_info table
    with open('airbnb/BedType.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO bedtype (BedTypeID, BedType) VALUES (%s, %s)"
                val = (row[0], row[1])
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

def importBooking(mydb):
    # Import basic_info table
    with open('airbnb/Booking.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO booking (ListingID, date, AvailablilityStatus, price) VALUES (%s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3])
                try:
                    date_string = row[1]
                    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
                    val = (row[0], date_obj.strftime('%Y/%m/%d'), row[2], row[3])
                except Exception as e:
                    print(e)
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
    with open('airbnb/Host.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO host (HostID, HostName, HostSince, HostCity, HostNeighborhood, HostState, HostIdentityVerified) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                try:
                    date_string = row[2]
                    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
                    val = (row[0], row[1], date_obj.strftime('%Y/%m/%d'), row[3], row[4], row[5], row[6])
                except Exception as e:
                    print(e)
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

def importHostListing(mydb):
    # Import basic_info table
    with open('airbnb/Host_has_listing.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO host_has_listing (ListingID, HostID, daily_price, number_of_reviews, review_scores_rating) VALUES (%s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4])
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

def importListing(mydb):
    with open('airbnb/Listing.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO listing (ListingID, ListingName, Street, neighborhood, City, State, Zipcode, bathrooms, bedrooms, beds, instant_bookable, BedTypeID, RoomTypeID, PropertyTypeID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
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

def importListingAmenities(mydb):
    # Import basic_info table
    with open('airbnb/Listing_has_amenities 1.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO listing_has_amenities (ListingID, AmenityID) VALUES (%s, %s)"
                val = (row[0], row[1])
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
    with open('airbnb/Listing_has_amenities 2.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO listing_has_amenities (ListingID, AmenityID) VALUES (%s, %s)"
                val = (row[0], row[1])
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
    mycursor.close()

def importPropertyType(mydb):
    with open('airbnb/PropertyType.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO propertytype (PropertyTypeID, Property_type) VALUES (%s, %s)"
                val = (row[0], row[1])
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

def importReviewer(mydb):
    with open('airbnb/Reviewer.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO reviewer (reviewerID, reviewerName) VALUES (%s, %s)"
                val = (row[0], row[1])
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

def importReviews(mydb):
    with open('airbnb/Reviews.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO reviews (reviewID, date, ReviewerID, ListingID) VALUES (%s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3])
                try:
                    date_string = row[1]
                    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
                    val = (row[0], date_obj.strftime('%Y/%m/%d'), row[2], row[3])
                except Exception as e:
                    print(e)
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

def importRoomType(mydb):
    with open('airbnb/RoomType.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO roomtype (RoomTypeID, room_type) VALUES (%s, %s)"
                val = (row[0], row[1])
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

if __name__=="__main__":

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="airbnb"
    )

    # Using functions below to import data

    importAmenities(mydb)
    importBedType(mydb)
    importPropertyType(mydb)
    importRoomType(mydb)
    importListing(mydb)
    importListingAmenities(mydb)
    importHost(mydb)
    importHostListing(mydb)
    importReviewer(mydb)
    importReviews(mydb)
    importBooking(mydb)










