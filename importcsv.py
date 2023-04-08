import csv
import mysql.connector

def importBasicInfo(mydb):
    # Import basic_info table
    with open('data/basic_info.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO basic_info (house_id, name, description, instant_bookable, price, availability, room_type, bathrooms, bedrooms, beds, amenities, numbers_of_reviews, review_score, host_id, neighborhood_id, property) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                if (len(val[0]) < 1):
                    continue
                if len(val[1]) > 199:
                    val = (row[0], row[1][:199], row[2], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                if len(val[2]) > 199:
                    val = (row[0], row[1], row[2][:199], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                if len(val[3]) > 4:
                    val = (row[0], row[1], row[2], row[3][:4], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                if len(val[6]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6][:19], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                if len(val[7]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6], row[7][:19], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15])
                if len(val[10]) > 199:
                    val = (row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10][:199], row[11], row[12], row[13], row[14], row[15])
                if len(val[15]) > 44:
                    val = (row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10][:199], row[11], row[12], row[13], row[14], row[15][:44])
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

def importScrapeInfo(mydb):
    # Import basic_info table
    with open('data/scrape_info.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO scrape_info (id, scrape_id, last_scraped, source) VALUES (%s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3])
                if (len(val[0]) < 1):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[1], row[2], row[3])
                if len(val[1]) > 44:
                    val = (row[0], row[1][:44], row[2], row[3])
                if len(val[2]) > 19:
                    val = (row[0], row[1], row[2][:19], row[3])
                if len(val[3]) > 44:
                    val = (row[0], row[1], row[2], row[3][:44])
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

def importRooms(mydb):
    # Import basic_info table
    with open('data/rooms.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO rooms (id, room_type, accommodates, bathrooms, bathroom_text, bedrooms, beds, amenities) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if (len(val[0]) < 1):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if len(val[1]) > 44:
                    val = (row[0], row[1][:44], row[2], row[3], row[4], row[5], row[6], row[7])
                if len(val[2]) > 19:
                    val = (row[0], row[1], row[2][:19], row[3], row[4], row[5], row[6], row[7])
                if len(val[3]) > 44:
                    val = (row[0], row[1], row[2], row[3][:44], row[4], row[5], row[6], row[7])
                if len(val[4]) > 44:
                    val = (row[0], row[1], row[2], row[3], row[4][:44], row[5], row[6], row[7])
                if len(val[5]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5][:19], row[6], row[7])
                if len(val[6]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6][:19], row[7])
                if len(val[7]) > 199:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7][:199])
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

def importRentHistory(mydb):
    # Import basic_info table
    with open('data/rent_history.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO rent_history (id, price, minimum_nights, maximum_nights, minimum_minimum_nights, maximum_minimum_nights, minimum_maximum_nights, maximum_maximum_nights, minimum_nights_avg_ntm, maximum_nights_avg_ntm) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                if (len(val[0]) < 1):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                if len(val[1]) > 19:
                    val = (row[0], row[1][:19], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                if len(val[2]) > 19:
                    val = (row[0], row[1], row[2][:19], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                if len(val[3]) > 19:
                    val = (row[0], row[1], row[2], row[3][:19], row[4], row[5], row[6], row[7], row[8], row[9])
                if len(val[4]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4][:19], row[5], row[6], row[7], row[8], row[9])
                if len(val[5]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5][:19], row[6], row[7], row[8], row[9])
                if len(val[6]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6][:19], row[7], row[8], row[9])
                if len(val[7]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7][:19], row[8], row[9])
                if len(val[8]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8][:19], row[9])
                if len(val[9]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9][:19])
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

def importCalendarListing(mydb):
    # Import basic_info table
    with open('data/calendar_listing.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO calendar_listing (id, updated, has_availability, availability_30, availability_60, availability_90, availability_365, calendar_last_scraped) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if (len(val[0]) < 1):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                if len(val[1]) > 44:
                    val = (row[0], row[1][:44], row[2], row[3], row[4], row[5], row[6], row[7])
                if len(val[2]) > 4:
                    val = (row[0], row[1], row[2][:4], row[3], row[4], row[5], row[6], row[7])
                if len(val[3]) > 4:
                    val = (row[0], row[1], row[2], row[3][:4], row[4], row[5], row[6], row[7])
                if len(val[4]) > 4:
                    val = (row[0], row[1], row[2], row[3], row[4][:4], row[5], row[6], row[7])
                if len(val[5]) > 4:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5][:4], row[6], row[7])
                if len(val[6]) > 44:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6][:44], row[7])
                if len(val[7]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7][:19])
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

def importReviewListing(mydb):
    # Import basic_info table
    with open('data/reviews_listing.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO reviews_listing (id, number_of_reviews, number_of_reviews_ltm, number_of_reviews_l30d, first_review, last_review, review_scores_rating, review_scores_accuracy, review_scores_cleanliness, review_scores_checkin, review_scores_communication, review_scores_location, review_scores_value, reviews_per_month) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if (len(val[0]) < 1):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[1]) > 19:
                    val = (row[0], row[1][:19], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[2]) > 19:
                    val = (row[0], row[1], row[2][:19], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[3]) > 19:
                    val = (row[0], row[1], row[2], row[3][:19], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[4]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4][:19], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[5]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5][:19], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[6]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6][:19], row[7], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[7]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7][:19], row[8], row[9], row[10], row[11], row[12], row[13])
                if len(val[8]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8][:19], row[9], row[10], row[11], row[12], row[13])
                if len(val[9]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9][:19], row[10], row[11], row[12], row[13])
                if len(val[10]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10][:19], row[11], row[12], row[13])
                if len(val[11]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11][:19], row[12], row[13])
                if len(val[12]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12][:19], row[13])
                if len(val[13]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13][:19])
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

def importCalculatedHostListingCount(mydb):
    # Import basic_info table
    with open('data/calculated_host_listing_count.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:
            # Insert each row into MySQL database
            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO calculated_host_listing_count (id, total_homes, entire_homes, private_rooms, shared_rooms) VALUES (%s, %s, %s, %s, %s)"
                val = (row[0], row[1], row[2], row[3], row[4])
                if (len(val[0]) < 1):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[1], row[2], row[3], row[4])
                if len(val[1]) > 19:
                    val = (row[0], row[1][:19], row[2], row[3], row[4])
                if len(val[2]) > 19:
                    val = (row[0], row[1], row[2][:19], row[3], row[4])
                if len(val[3]) > 19:
                    val = (row[0], row[1], row[2], row[3][:19], row[4])
                if len(val[4]) > 19:
                    val = (row[0], row[1], row[2], row[3], row[4][:19])
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

def importHosting(mydb):
    # Import basic_info table
    with open('data/host.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.reader(csvfile)
        next(csv_data)  # Skip header row

        ptr = 2

        for row in csv_data:

            if (ptr > 0):  # Use this pointer to skip rows imported
                mycursor = mydb.cursor()
                sql = "INSERT INTO hosting (id, hostid) VALUES (%s, %s)"
                val = (row[0], row[18])
                if (len(val[0]) < 1 or not (val[0][0] >= '0' and val[0][0] <= '9')):
                    continue
                if len(val[0]) > 19:
                    val = (row[0][:19], row[18])
                if len(val[1]) > 19:
                    val = (row[0], row[18][:19])
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

def setNeighborhoodId(mydb):
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
                if(not row[14] in table):
                    continue
                val = (row[0], row[1], row[2], row[3], row[4][1:], row[5], row[6], row[7], row[8], row[9], row[10], row[11],row[12], row[13], table[row[14]], row[15])

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


if __name__=="__main__":

    # Connect to MySQL
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="656project"
    )

    #Using under func to import data

    #importBasicInfo(mydb)
    #importScrapeInfo(mydb)
    #importHost(mydb)
    #importNeighborhood(mydb)
    #importRooms(mydb)
    #importRentHistory(mydb)
    #importCalendarListing(mydb)
    #importReviewListing(mydb)
    #importCalculatedHostListingCount(mydb)
    importCalendar(mydb)
    #importReviews(mydb)
    #importHosting(mydb)
    #setNeighborhoodId()


