import csv
from datetime import datetime
from datetime import timedelta
import random


p_rate = 1.3
maintenance = 35

reasons = ["Customer meeting", "Technical meeting", "Product discussion meeting", "Client Support", "Configuration of devices", "Client Support", "Client Support"]

#places = ["Randburg", "Paulshof", "Midrand", "Johannesburg", "Magaliesburg", "Illovo"]

places = [("Midrand","Randburg",32,""),("Midrand","Illovo",22,""),("Midrand","KemptonPark",24,""),("Midrand","Paulshof",15,""),("Midrand","Bryanston",26,"")]

personal = [("Midrand","Paulshof",24,"Personal Travel"),("Midrand","Fortsburg",50,"Personal Travel")]


tmp_start_date = "19-09-2019"
tmp_end_date = "29-02-2020"

def day_get(number):
    if number == 0:
        return 'Monday'
    elif number == 1:
        return 'Tuesday'
    elif number == 2:
        return 'Wednesday'
    elif number == 3:
        return 'Thursday'
    elif number == 4:
        return 'Friday'
    elif number == 5:
        return 'Saturday'
    elif number == 6:
        return 'Sunday'





def main():
    start_date = datetime(2019,3,1)
    end_date = datetime(2019,11,3)
    f = open('output.csv','w',newline='')
    csv_write = csv.writer(f)
    start_km = 134021
    end_km = 144021
    while True:
        if start_km < end_km:
            #2-Mar-17	101539	101564	25	Paulshof	Randburg	Customer Meeting	33.25	11.47
            random_choice = random.choice(places)
            res = random.choice(reasons)
            if random_choice[3] == "" and start_date != end_date:
                if start_date.weekday() == 5 or start_date.weekday() == 6: 
                    personal_choice = random.choice(personal)
                    tmp_end = start_km + personal_choice[2]
                    csv_write.writerow([start_date,day_get(start_date.weekday()),start_km, tmp_end, personal_choice[2], personal_choice[0], personal_choice[1], personal_choice[3], (personal_choice[2] * p_rate), (maintenance * personal_choice[2] * p_rate)/100])
                    start_km = start_km + personal_choice[2]
                    start_date = start_date + timedelta(days=1)
                    if personal_choice[1] == "Graskop":
                        del personal[-1]

                       
                else:   
                    tmp_end = start_km + random_choice[2]
                    csv_write.writerow([start_date,day_get(start_date.weekday()),start_km, tmp_end, random_choice[2], random_choice[0], random_choice[1], res, (random_choice[2] * p_rate), (maintenance * random_choice[2] * p_rate)/100])
                    start_km = start_km + random_choice[2]
                    start_date = start_date + timedelta(days=1)
            else:
                if (start_date.weekday() == 5 or start_date.weekday() == 6) and (random_choice[3] == "Personal Travel"): 
                    tmp_end = start_km + random_choice[2]
                    csv_write.writerow([start_date,day_get(start_date.weekday()),start_km, tmp_end, random_choice[2], random_choice[0], random_choice[1], random_choice[3], (random_choice[2] * p_rate), (maintenance * random_choice[2] * p_rate)/100])
                    start_km = start_km + random_choice[2]
                    start_date = start_date + timedelta(days=1)
                elif (start_date.weekday() == 5 or start_date.weekday() == 6) and (random_choice[3] != "Personal Travel"):
                    numb = [0,1]
                    if random.choice(numb) == 1:
                        personal_choice = random.choice(personal)
                        tmp_end = start_km + personal_choice[2]
                        csv_write.writerow([start_date,day_get(start_date.weekday()),start_km, tmp_end, personal_choice[2], personal_choice[0], personal_choice[1], personal_choice[3], (personal_choice[2] * p_rate), (maintenance * personal_choice[2] * p_rate)/100])
                        start_km = start_km + personal_choice[2]
                        start_date = start_date + timedelta(days=1)
                        if personal_choice[1] == "Graskop":
                            del personal[-1]
                    else:
                       start_date = start_date + timedelta(days=1)
                else:
                    tmp_end = start_km + random_choice[2]
                    csv_write.writerow([start_date,day_get(start_date.weekday()),start_km, tmp_end, random_choice[2], random_choice[0], random_choice[1], random_choice[3], (random_choice[2] * p_rate), (maintenance * random_choice[2] * p_rate)/100])
                    start_km = start_km + random_choice[2]
                    start_date = start_date + timedelta(days=1)

                       
        else:
            break

if __name__ == "__main__":
    main()