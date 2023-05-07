from csv import reader
from reporting import *
from intelligence import *
from monitoring import *
import sys 
from datetime import date, timedelta

def main_menu():
    """This is the primary function called to execute the program, within this function you can access different 
    options (Pollution Reporting module, The Mobility Intelligence module, Real-time Monitoring module, about and quit )
    
    Argument(s) : 
    ---------------
    No arguments is passed to this function 
    ---------------
    Note(s) : This program will always go back to it self unless user presses (q) or (Q) which will terminate the program.
    (This program designed in a way that it will always go back to main menu regardless of what option you choose 
    unless pressing (q) or (Q) in main menu, which will quit the program)
    ---------------
    Return(s) : This function doesn't return anything and only run other functions inside it and print the results properly
    """
                
    print("\n\t\tWelcome to the Main Menu")
    print("\t----------------------------------------")
    print("- To Access The Pollution Reporting module (PR) Enter:  (R)")
    print("- To Access The Mobility Intelligence module (MI) Enter:  (I)")
    print("- To Access The Real-time Monitoring module (RM) Enter:  (M)")
    print("- To Access The About text Enter:  (A)")
    print("- To Quit the Application Enter:  (Q)")
    print("\n")
    
    while True:
        User = input("Enter One of (R,I,M,A,Q): ")
        if User in {'R','I','M','A','Q','r','i','m','a','q'}:
            break
        else: 
            print(f"Invalid Input ! {User}")
            print("Try Again and Choose From: (R,I,M,A,Q)")
            
    if User in {"R","r"}:
        reporting_menu()
    elif User in {"M","m"}:
        monitoring_menu()
    elif User in {"I","i"}:
        intelligence_menu()
    elif User in {"A","a"}:
        about()
    elif User in {"Q","q"}:
        quit()
    else :
        print("Something went wrong start over...")
        main_menu()

def reporting_menu():
    """This is a function that will activate if user presses (R) or (r) in the main menu and will
    guid the user to access multiple options to choose from 
    (daily average, daily median, hourly average, monthly average, peak hour in a specific date)
    
    Argument(s) : 
    ---------------
    No arguments is passed to this function 
    ---------------
    Note(s) : This program will always go back to it self unless user presses (0) to go back to main menu.
    ---------------
    Return(s) : This function doesn't return anything and only run other functions inside it and print the results properly
    """
    
    print("\n\tWelcom to The Reporting menu")
    print("--------------------------------------------")
    print("- To go back to the main menu press :  0")
    print("- To calculate the daily average press :  1")
    print("- To calculate the daily median press :  2")
    print("- To calculate the hourly average press :  3")
    print("- To calculate the monthly average press :  4")
    print("- To see the peak hour in a specific date press :  5")
    print("\n") 
     
    while True:
        User = input("Enter One of (0, 1, 2, 3, 4, 5): ")
        if User in {'0', '1', '2', '3', '4', '5'}:
            break
        else: 
            print(f"Invalid Input ! {User}")
            print("Try Again and Choose From: (0, 1, 2, 3, 4, 5)")
    
    if User == '0':
        main_menu()
        
    elif User == '1':
        print("\n")
        print("\t_________________Daily Average_________________")
        print("\n")
        while True:
            station = input("Enter The Name of The Monitoring Station (Harlington, Kensington, Marylebone) (Q or q to go back to reporting menu): ")
            if station in {'Harlington', 'Kensington', 'Marylebone', 'harlington', 'kensington', 'marylebone'}:
                break
            elif station in {"Q", "q"} :
                reporting_menu()
            else: 
                print(f"Invalid Input ! {station}")
                print("Try Again and Choose From: (Harlington, Kensington, Marylebone)")
        while True:
            pollutant = input("Enter One of (no, pm10, pm25): ")
            if pollutant in {'no', 'pm10', 'pm25'}:
                break
            else: 
                print(f"Invalid Input ! {pollutant}")
                print("Try Again and Choose From: (no, pm10, pm25)")
        
        if station in {"Harlington", "harlington"}: 
            with open('data/Pollution-London Harlington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Kensington", "kensington"}:
            with open('data/Pollution-London N Kensington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Marylebone", "marylebone"}:
            with open('data/Pollution-London Marylebone Road.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
              
        try : 
            station_daily_average = daily_average(data, station, pollutant)
            print("-----------------------------------------------------------")
            print("Would you like to see all daily averages or a specific day ?")
            print("Enter (S) for a specific day and Enter (A) to see all days at once (365 values)")
            print("-----------------------------------------------------------")
            while True:
                user = input("Enter One of (S, s, A, a) : ")
                if user in {'S', 's'}:
                    while True:
                        try:
                            day = int(input("Enter The Nth day to see the average in that day in the year 2021-2022: "))
                        except:
                            print(f"Invalid Input ! (Enter a Valid Number)")
                            continue
                        if 0 < day <= 365:
                            print("-----------------------------------------------------------")
                            print(f"The average of {pollutant} in day {day} is {station_daily_average[day-1]}")
                            print("-----------------------------------------------------------")
                            reporting_menu()
                        else: 
                            print(f"Invalid Input ! {day}")
                            print("Try Again and Choose a Number from 1 to 365")
                elif user in {'A', 'a'}:
                    print("-----------------------------------------------------------")
                    print(f"Daily Averages in 2021-2022 : \n{station_daily_average}")
                    print("-----------------------------------------------------------")
                    reporting_menu()
                else: 
                    print(f"Invalid Input ! {user}")
                    print("Try Again and Choose From: (S, s, A, a)")
        except: 
            count = count_missing_data(data, station, pollutant)    
            if count != 0:
                print(f"Some of the {pollutant} Data(s) are missing... ")
                while True:
                    user_input = input("Enter (D) for Details and (R) to Replace : ")
                    if user_input in {'D', 'd'}:
                        if pollutant == "no" : 
                            index = 2
                        elif pollutant == "pm10" : 
                            index = 3
                        elif pollutant == "pm25" : 
                            index = 4
                        for i in data:
                            try: 
                                float(i[index])
                            except:
                                print(f"No Record of pollutant ({pollutant}) from {station} station in {i[0]} at {i[1]}")
                        print(f"There are total number of {count} missing pollutant {pollutant} in {station}")
                        print("-----------------------------------------------------")
                    elif user_input in {'R', 'r'} :
                        while True:
                            new_value = input("Enter a Value for Missing Data(s) : ")
                            try :  
                                float(new_value)
                                break
                            except: 
                                print(f"Invalid Input ! Strings are not Supported : {new_value}")
                        data = fill_missing_data(data, new_value, station, pollutant)
                        station_daily_average = daily_average(data, station, pollutant)
                        print("-----------------------------------------------------------")
                        print("Would you like to see all daily averages or a specific day ?")
                        print("Enter (S) for a specific day and Enter (A) to see all days at once (365 values)")
                        print("-----------------------------------------------------------")
                        while True:
                            user = input("Enter One of (S, s, A, a): ")
                            if user in {'S', 's'}:
                                while True:
                                    try:
                                        day = int(input("Enter The Nth day to see the average in that day in the year 2021-2022: "))
                                    except:
                                        print(f"Invalid Input ! (Enter a Valid Number)")
                                        continue
                                    if 0 < day <= 365:
                                        print("-----------------------------------------------------------")
                                        print(f"The average of {pollutant} in day {day} is {station_daily_average[day-1]}")
                                        print("-----------------------------------------------------------")
                                        reporting_menu()
                                    else: 
                                        print(f"Invalid Input ! {day}")
                                        print("Try Again and Choose a Number from 1 to 365")
                            elif user in {'A', 'a'}:
                                print("-----------------------------------------------------------")
                                print(f"Daily Averages in 2021-2022 : \n{station_daily_average}")
                                print("-----------------------------------------------------------")
                                reporting_menu()
                            else: 
                                print(f"Invalid Input ! {user}")
                                print("Try Again and Choose From: (S, s, A, a)")
                    else :
                        print(f"Invalid Input ! {user_input}")
                        print("Try Again and Choose From: (D, d, R, r)")
    elif User == '2':
        print("\n")
        print("\t_________________Daily Median_________________")
        print("\n")
        while True:
            station = input("Enter The Name of The Monitoring Station (Harlington, Kensington, Marylebone) (Q or q to go back to reporting menu): ")
            if station in {'Harlington', 'Kensington', 'Marylebone', 'harlington', 'kensington', 'marylebone'}:
                break
            elif station in {"Q", "q"}:
                reporting_menu()
            else:
                print(f"Invalid Input ! {station}")
                print("Try Again and Choose From: (Harlington, Kensington, Marylebone)")
        while True:
            pollutant = input("Enter One of (no, pm10, pm25): ")
            if pollutant in {'no', 'pm10', 'pm25'}:
                break
            else: 
                print(f"Invalid Input ! {pollutant}")
                print("Try Again and Choose From: (no, pm10, pm25)")
                
        if station in {"Harlington", "harlington"}: 
            with open('data/Pollution-London Harlington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Kensington", "kensington"}:
            with open('data/Pollution-London N Kensington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Marylebone", "marylebone"}:
            with open('data/Pollution-London Marylebone Road.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        try : 
            station_daily_median = daily_median(data, station, pollutant)
            print("-----------------------------------------------------------")
            print("Would you like to see all daily medians or a specific day ?")
            print("Enter (S) for a specific day and Enter (A) to see all days at once (365 values)")
            print("-----------------------------------------------------------")
            while True:
                user = input("Enter One of (S, s, A, a) : ")
                if user in {'S', 's'}:
                    while True:
                        try:
                            day = int(input("Enter The Nth day to see the median in that day in the year 2021-2022 : "))
                        except:
                            print(f"Invalid Input ! (Enter a Valid Number)")
                            continue
                        if 0 < day <= 365:
                            print("-----------------------------------------------------------")
                            print(f"The median of {pollutant} in day {day} is {station_daily_median[day-1]}")
                            print("-----------------------------------------------------------")
                            reporting_menu()
                        else: 
                            print(f"Invalid Input ! {day}")
                            print("Try Again and Choose a Number from 1 to 365")
                elif user in {'A', 'a'}:
                    print("-----------------------------------------------------------")
                    print(f"Daily Medians in 2021-2022 : \n{station_daily_median}")
                    print("-----------------------------------------------------------")
                    reporting_menu()
                else: 
                    print(f"Invalid Input ! {user}")
                    print("Try Again and Choose From: (S, s, A, a)")
        except:
            count = count_missing_data(data, station, pollutant) 
            if count != 0 :
                print(f"Some of the {pollutant} Data(s) are missing... ")
                while True:
                    user_input = input("Enter (D) for Details and (R) for Replace : ")
                    if user_input in {'D', 'd'}:
                        if pollutant == "no" : 
                            index = 2
                        elif pollutant == "pm10" : 
                            index = 3
                        elif pollutant == "pm25" : 
                            index = 4
                        for i in data:
                            try:
                                float(i[index])
                            except:
                                print(f"No Record of pollutant ({pollutant}) from {station} station in {i[0]} at {i[1]}")
                        print(f"There are total of {count} number of missing pollutant {pollutant} in {station}")
                        print("-----------------------------------------------------")
                    elif user_input in {'R', 'r'} :
                        while True:
                            new_value = input("Enter a Value for Missing Data(s) : ")
                            try :  
                                float(new_value)
                                break
                            except: 
                                print(f"Invalid Input ! Strings are not Supported : {new_value}")
                        data = fill_missing_data(data, new_value, station, pollutant)
                        station_daily_median = daily_median(data, station, pollutant)
                        print("-----------------------------------------------------------")
                        print("Would you like to see all daily medians or a specific day ?")
                        print("Enter (S) for a specific day and Enter (A) to see all days at once (365 values)")
                        print("-----------------------------------------------------------")
                        while True:
                            user = input("Enter One of (S, s, A, a): ")
                            if user in {'S', 's'}:
                                 while True:
                                    try:
                                        day = int(input("Enter The Nth day to see the median in that day in the year 2021-2022: "))
                                    except:
                                        print(f"Invalid Input ! (Enter a Valid Number)")
                                        continue
                                    if 0 < day <= 365:
                                        print("-----------------------------------------------------------")
                                        print(f"The median of {pollutant} in day {day} is {station_daily_median[day-1]}")
                                        print("-----------------------------------------------------------")
                                        reporting_menu()
                                    else: 
                                        print(f"Invalid Input ! {day}")
                                        print("Try Again and Choose a Number from 1 to 365")
                            elif user in {'A', 'a'}:
                                print("-----------------------------------------------------------")
                                print(f"Daily Medians in 2021-2022 : \n{station_daily_median}")
                                print("-----------------------------------------------------------")
                                reporting_menu()
                            else: 
                                print(f"Invalid Input ! {user}")
                                print("Try Again and Choose From: (S, s, A, a)")
                    else :
                        print(f"Invalid Input ! {user_input}")
                        print("Try Again and Choose From: (D, d, R, r)")
                        
    elif User == '3':
        print("\n")
        print("\t_________________Hourly Average_________________")
        print("\n")
        
        while True:
            station = input("Enter The Name of The Monitoring Station (Harlington, Kensington, Marylebone) (Q or q to go back to reporting menu): ")
            if station in {'Harlington', 'Kensington', 'Marylebone', 'harlington', 'kensington', 'marylebone'}:
                break
            elif station in {"Q", "q"}:
                reporting_menu()
            else:
                print(f"Invalid Input ! {station}")
                print("Try Again and Choose From: (Harlington, Kensington, Marylebone)")
        while True:
            pollutant = input("Enter One of (no, pm10, pm25): ")
            if pollutant in {'no', 'pm10', 'pm25'}:
                break
            else: 
                print(f"Invalid Input ! {pollutant}")
                print("Try Again and Choose From: (no, pm10, pm25)")
        
        if station in {"Harlington", "harlington"}: 
            with open('data/Pollution-London Harlington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Kensington", "kensington"}:
            with open('data/Pollution-London N Kensington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Marylebone", "marylebone"}:
            with open('data/Pollution-London Marylebone Road.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        try : 
            station_hourly_average = hourly_average(data, station, pollutant)
            print("-----------------------------------------------------------")
            print("Would you like to see all Hourly Averages or a specific hour ?")
            print("Enter (S) for a specific hour and Enter (A) to see all hours at once (24 values)")
            print("-----------------------------------------------------------")
            while True:
                user = input("Enter One of (S, s, A, a) : ")
                if user in {'S', 's'}:
                    while True:
                        try:
                            hour = int(input("Enter The Nth hour to see the average of that hour in the year 2021-2022 : "))
                        except:
                            print(f"Invalid Input ! (Enter a Valid Number)")
                            continue
                        if 0 < hour <= 24:
                            if hour >= 12:
                                pa = "pm"
                                hour = hour - 12
                            elif hour < 12:
                                pa = "am"
                            print("-----------------------------------------------------------")
                            print(f"The average of {pollutant} at {hour} {pa} is {station_hourly_average[day-1]}")
                            print("-----------------------------------------------------------")
                            reporting_menu()
                        else: 
                            print(f"Invalid Input ! {hour}")
                            print("Try Again and Choose a Number from 1 to 24")
                elif user in {'A', 'a'}:
                    print("-----------------------------------------------------------")
                    print(f"Hourly Averages in 2021-2022 : \n{station_hourly_average}")
                    print("-----------------------------------------------------------")
                    reporting_menu()
                else:
                    print(f"Invalid Input ! {user}")
                    print("Try Again and Choose From: (S, s, A, a)")
        except: 
            count = count_missing_data(data, station, pollutant)    
            if count != 0 :
                print(f"Some of the {pollutant} Data(s) are missing... ")
                while True:
                    user_input = input("Enter (D) for Details and (R) for Replace : ")
                    if user_input in {'D', 'd'}:
                        if pollutant == "no" : 
                            index = 2
                        elif pollutant == "pm10" : 
                            index = 3
                        elif pollutant == "pm25" : 
                            index = 4
                        for i in data:
                            try: 
                                float(i[index])
                            except:
                                print(f"No Record of pollutant ({pollutant}) from {station} station in {i[0]} at {i[1]}")
                        print(f"There are total of {count} number of missing pollutant {pollutant} in {station}")
                        print("-----------------------------------------------------")
                    elif user_input in {'R', 'r'} :
                        while True:
                            new_value = input("Enter a Value for Missing Data(s) : ")
                            try :  
                                float(new_value)
                                break
                            except: 
                                print(f"Invalid Input ! Strings are not Supported : {new_value}")
                        data = fill_missing_data(data, new_value, station, pollutant)
                        station_hourly_average = hourly_average(data, station, pollutant)
                        print("-----------------------------------------------------------")
                        print("Would you like to see all Hourly averages or a specific hour ?")
                        print("Enter (S) for a specific hour and Enter (A) to see all hours at once (24 values)")
                        print("-----------------------------------------------------------")
                        while True:
                            user = input("Enter One of (S, s, A, a): ")
                            if user in {'S', 's'}:
                                 while True:
                                    try:
                                        hour = int(input("Enter The Nth hour to see the average of that hour in the year 2021-2022: "))
                                    except:
                                        print(f"Invalid Input ! (Enter a Valid Number)")
                                    if 0 < hour <= 24:
                                        if hour <= 12 :
                                            pa = "am"
                                        elif hour > 12 : 
                                            pa = "pm"
                                            hour = hour - 12
                                        print("-----------------------------------------------------------")
                                        print(f"The hourly average of {pollutant} in {hour} {pa} is {station_hourly_average[hour-1]}")
                                        print("-----------------------------------------------------------")
                                        reporting_menu()
                                    else: 
                                        print(f"Invalid Input ! {hour}")
                                        print("Try Again and Choose a Number from 1 to 24")
                            elif user in {'A', 'a'}:
                                print("-----------------------------------------------------------")
                                print(f"Hourly Averages in 2021-2022 : \n{station_hourly_average}")
                                print("-----------------------------------------------------------")
                                reporting_menu()
                            else: 
                                print(f"Invalid Input ! {user}")
                                print("Try Again and Choose From: (S, s, A, a)")
                    else :
                        print(f"Invalid Input ! {user_input}")
                        print("Try Again and Choose From: (D, d, R, r)")
    elif User == '4':
        print("\n")
        print("\t_________________Monthly Average_________________")
        print("\n")
        while True:
            station = input("Enter The Name of The Monitoring Station (Harlington, Kensington, Marylebone) (Q or q to go back to reporting menu): ")
            if station in {'Harlington', 'Kensington', 'Marylebone', 'harlington', 'kensington', 'marylebone'}:
                break
            elif station in {"Q", "q"}:
                reporting_menu()
            else:
                print(f"Invalid Input ! {station}")
                print("Try Again and Choose From: (Harlington, Kensington, Marylebone)")
        while True:
            pollutant = input("Enter One of (no, pm10, pm25): ")
            if pollutant in {'no', 'pm10', 'pm25'}:
                break
            else: 
                print(f"Invalid Input ! {pollutant}")
                print("Try Again and Choose From: (no, pm10, pm25)")
    
        if station in {"Harlington", "harlington"}: 
            with open('data/Pollution-London Harlington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Kensington", "kensington"}:
            with open('data/Pollution-London N Kensington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Marylebone", "marylebone"}:
            with open('data/Pollution-London Marylebone Road.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        try : 
            station_monthly_average = monthly_average(data, station, pollutant)
            print("-----------------------------------------------------------")
            print("Would you like to see all Monthly averages or a specific month ?")
            print("Enter (S) for a specific month and Enter (A) to see all months at once (12 values)")
            print("-----------------------------------------------------------")
            while True:
                user = input("Enter One of (S, s, A, a) : ")
                if user in {'S', 's'}:
                    while True:
                        try:
                            month = int(input("Enter The Nth month to see the average in that month in the year 2021-2022: "))
                        except:
                            print(f"Invalid Input ! (Enter a Valid Number)")
                            continue
                        if 0 < month <= 12:
                            print("-----------------------------------------------------------")
                            print(f"The average of {pollutant} in month {month} of the year 2021-2022 is {station_monthly_average[day-1]}")
                            print("-----------------------------------------------------------")
                            reporting_menu()
                        else: 
                            print(f"Invalid Input ! {month}")
                            print("Try Again and Choose a Number from 1 to 12")
                elif user in {'A', 'a'}:
                    print("-----------------------------------------------------------")
                    print(f"Monthly Averages in 2021-2022 : \n{station_monthly_average}")
                    print("-----------------------------------------------------------")
                    reporting_menu()
                else: 
                    print(f"Invalid Input ! {user}")
                    print("Try Again and Choose From: (S, s, A, a)")
        except: 
            count = count_missing_data(data, station, pollutant) 
            if count != 0 :
                print(f"Some of the {pollutant} Data(s) are missing... ")
                while True:
                    user_input = input("Enter (D) for Details and (R) for Replace : ")
                    if user_input in {'D', 'd'}:
                        if pollutant == "no" :
                            index = 2
                        elif pollutant == "pm10" :
                            index = 3
                        elif pollutant == "pm25" :
                            index = 4
                        for i in data:
                            try:
                                float(i[index])
                            except:
                                print(f"No Record of pollutant ({pollutant}) from {station} station in {i[0]} at {i[1]}")
                        print(f"There are total of {count} number of missing pollutant {pollutant} in {station}")
                        print("-----------------------------------------------------")
                    elif user_input in {'R', 'r'} :
                        while True:
                            new_value = input("Enter a Value for Missing Data(s) : ")
                            try :  
                                float(new_value)
                                break
                            except: 
                                print(f"Invalid Input ! Strings are not Supported : {new_value}")
                        data = fill_missing_data(data, new_value, station, pollutant)
                        station_monthly_average = monthly_average(data, station, pollutant)
                        print("-----------------------------------------------------------")
                        print("Would you like to see all Monthly averages or a specific month ?")
                        print("Enter (S) for a specific month and Enter (A) to see all months at once (12 values)")
                        print("-----------------------------------------------------------")
                        while True:
                            user = input("Enter One of (S, s, A, a): ")
                            if user in {'S', 's'}:
                                 while True:
                                    try:
                                        month = int(input("Enter The Nth month to see the average in that month: "))
                                    except:
                                        print(f"Invalid Input ! (Enter a Valid Number)")
                                        continue
                                    if 0 < month <= 12:
                                        print("-----------------------------------------------------------")
                                        print(f"The average of {pollutant} in {month} month of the year is {station_monthly_average[month-1]}")
                                        print("-----------------------------------------------------------")
                                        reporting_menu()
                                    else: 
                                        print(f"Invalid Input ! {month}")
                                        print("Try Again and Choose a Number from 1 to 12")
                            elif user in {'A', 'a'}:
                                print("-----------------------------------------------------------")
                                print(f"Monthly Averages in 2021-2022 : \n{station_monthly_average}")
                                print("-----------------------------------------------------------")
                                reporting_menu()
                            else: 
                                print(f"Invalid Input ! {user}")
                                print("Try Again and Choose From: (S, s, A, a)")
                    else :
                        print(f"Invalid Input ! {user_input}")
                        print("Try Again and Choose From: (D, d, R, r)")
    elif User == '5':
        print("\n")
        print("\t_________________Peak Hour_________________")
        print("\n")
        
        while True:
            station = input("Enter The Name of The Monitoring Station (Harlington, Kensington, Marylebone) (Q or q to go back to reporting menu): ")
            if station in {'Harlington', 'Kensington', 'Marylebone', 'harlington', 'kensington', 'marylebone'}:
                break
            elif station in {"Q", "q"}:
                reporting_menu()
            else:
                print(f"Invalid Input ! {station}")
                print("Try Again and Choose From: (Harlington, Kensington, Marylebone)")
        while True:
            pollutant = input("Enter One of (no, pm10, pm25): ")
            if pollutant in {'no', 'pm10', 'pm25'}:
                break
            else: 
                print(f"Invalid Input ! {pollutant}")
                print("Try Again and Choose From: (no, pm10, pm25)")
       
        if station in {"Harlington", "harlington"}: 
            with open('data/Pollution-London Harlington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Kensington", "kensington"}:
            with open('data/Pollution-London N Kensington.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
        elif station in {"Marylebone", "marylebone"}:
            with open('data/Pollution-London Marylebone Road.csv', 'r') as read_obj:
                csv_reader = reader(read_obj)
                next(csv_reader)
                data = []
                for row in csv_reader:
                    data.append(row)
                        
        while True: 
            date = input("Enter a Valid Date (ex. 2021-10-05): ")
            has = True
            for i in data :
                if i[0] == date :
                    has = False
            if has :
                print(f"Invalid Input ! {date}")
                print("Try Again and Enter a Valid Date (ex. 2021-08-15)")
            else : 
                break
        try : 
            station_peak_hour_date = peak_hour_date(data, date, station, pollutant)
            print(f"The peak amount of pollutant ({pollutant}) in {date} is {station_peak_hour_date}")
            reporting_menu()
        except:
            count = count_missing_data(data, station, pollutant)    
            if count != 0 :
                print(f"Some of the {pollutant} Data(s) are missing... ")
                while True:
                    user_input = input("Enter (D) for Details and (R) for Replace: ")
                    if user_input in {'D', 'd'}:
                        if pollutant == "no" : 
                            index = 2
                        elif pollutant == "pm10" : 
                            index = 3
                        elif pollutant == "pm25" : 
                            index = 4
                        for i in data:
                            try: 
                                float(i[index])
                            except:
                                print(f"No Record of pollutant ({pollutant}) from {station} station in {i[0]} at {i[1]}")
                            print(f"There are total of {count} number of missing pollutant {pollutant} in {station}")
                    elif user_input in {'R', 'r'}:
                        new_value = input("Enter a Value for Missing Data(s) : ")
                        data = fill_missing_data(data, new_value, station, pollutant)
                        station_peak_hour_date = peak_hour_date(data, date, station, pollutant)
                        print(f"The peak amount of pollutant ({pollutant}) in {date} is {station_peak_hour_date} in the year 2021-2022")
                        reporting_menu()
    main_menu()
def monitoring_menu():
    """This is a function that will activate if user presses (M) or (m) in the main menu and will
    guid the user to access live data from the api
    
    Argument(s) : 
    ---------------
    No arguments is passed to this function 
    ---------------
    Note(s) : This program will always go back to it self unless user presses (0) to go back to main menu.
    - user can choose the details about the data that is going to be recieved
    ---------------
    Return(s) : This function doesn't return anything and only run other functions inside it and print the results properly
    """
    
    print("\n\tWelcom to The Monitoring menu")
    print("---------------------------------------------")
    print("To go back to the main menu press :  0")
    print("To see the api information press :  1")
    print("\n")
    
    while True:
        User = input("Enter One of (0, 1): ")
        if User in {'0', '1'}:
            break
        else: 
            print(f"Invalid Input ! {User}")
            print("Try Again and Choose From: (0, 1)")
            

    if User == '0' : 
        main_menu()
    elif User == '1' :
        
        print("\n\tGet data from API")
        print("-------------------------------------")
        print("Choose a citie, website, start date and end date to continue")
        
        group_names = get_group_names()
        print("Choose on of the cities below : ")
        for i in group_names : 
            print(f"- {i}")
        
        while True:
            citie = input("Enter on of the cities :  ")
            if citie in set(group_names):
                break
            else: 
                print(f"Invalid Input ! {citie}")
                print("Try Again and write the citie name as the same format as above")
        
        
        print("Would you like to see the result for All available Species or a particular Species ?")
        while True:
            ask = input("Enter (A) to see All available species and (P) to see a particular Species : ")
            if ask in {"A", "a"}:
                try : 
                    Sites = get_site_names_all(citie)
                    break
                except : 
                    print("Bad URL, Try a Different Citie")
                    monitoring_menu()
            elif ask in {"P", "p"}:
                try : 
                    Sites = get_site_names_single(citie)
                    break
                except : 
                    print("Bad URL, Try a Different Site Name")
                    monitoring_menu()
            else: 
                print(f"Invalid Input ! {ask}")
                print("Try Again and Choose from (A, a, P, p)")

        print("Choose a Site name to continue : ")
        for j in Sites : 
            print(f"- {j}")
            
        
        while True:
            Site = input("Enter on of the Sites :  ")
            if Site in set(Sites):
                break
            else: 
                print(f"Invalid Input ! {Site}")
                print("Try Again and write the Site name as the same format as above")
                
        if ask in {"A", "a"}:
            try : 
                Sitecode , Speciescode = url_info_monitoring(Site)
                Sitecode , Speciescode = get_answer_from_the_user(Sitecode, Speciescode)
            except : 
                print("Bad URL, Try a Different Site Name")
                monitoring_menu()
        elif ask in {"P", "p"}:
            try : 
                Sitecode , Speciescode = url_info_monitoring_species(Site)
                Sitecode , Speciescode = get_answer_from_the_user(Sitecode, Speciescode)
            except : 
                print("Bad URL, Try a Different Site Name")
                monitoring_menu()
        

        while True:
            Start = input("Enter The Start Day of Mesurment (ex. 2022-10-13) or type (T) for today's mesurment (Live Data) : ")
            try: 
                year = Start[0:4]
                month = Start[5:7]
                day = Start[8:10]
                entered_date = date(int(year), int(month), int(day))
                if entered_date > date.today() : 
                    print(f"Day Entered was is in the future : {Start}")
                else : 
                    break
            except:
                if Start in {'T', 't'}: 
                    Start = None
                    break
                else : 
                    print(f"Invalid Input ! {Start}")
                    print("Try Again and write the Date between 2008 and 2022 in format (2022-10-13)")
        if Start != None :         
            while True:
                End = input("Enter The End Day of Mesurment (ex. 2022-10-13) : ")
                if 1970 <= int(Start[0:4]) <= 2022 : 
                    break
                else : 
                    print(f"Invalid Input ! {End}")
                    print("Try Again and write the Date between 2008 and 2022 in format (2022-10-13)")
        else : 
            End = None
            
        data = convert_csv_url_to_data(Sitecode, Speciescode, Start, End)
        
        organized_data = get_data(data, Site)
        
       
        data , pollutant_name = manage_available_data(organized_data)
        
        if data == None and pollutant_name == None :    
            print("No Record of Data on any Pollutant")
            monitoring_menu()
        
        
        print("would you like to See : ")
        print("- Sum of the available data :  S")
        print("- Maxvalue of available data :  X")
        print("- Minvalue of available data :  I")
        print("- Meanvalue of available data :  N")
        print("\n")
        
        while True:
            cal = input("Enter one of (S, X, I, M) : ")
            if cal in {'S', 's'} :
                calculate_Sum_data(data, pollutant_name) 
                break
            if cal in {'X', 'x'} :
                calculate_Maxvalue_data(data,pollutant_name)
                break
            if cal in {'I', 'i'} :
                calculate_Meanvalue_data(data,pollutant_name)
                break
            if cal in {'N', 'n'} :
                calculate_Minvalue_data(data,pollutant_name)
                break
            else : 
                print(f"Invalid Input ! {cal}")
                print("Try Again and Choose from one of (S, X, I, M) :")
            
        
        
        
        
    
    else : 
        main_menu()
def intelligence_menu():
    """This is a function that will activate if user presses (I) or (i) in the main menu and will
    guid the user to access multiple options to choose from 
    (detect red pixels, detect cyan pixels, find and sort the connected components of the picture)
    
    Argument(s) : 
    ---------------
    No arguments is passed to this function 
    ---------------
    Note(s) : This program will always go back to it self unless user presses (0) to go back to main menu.
    ---------------
    Return(s) : This function doesn't return anything and only run other functions inside it and print the results properly
    """
    
    print("\n\tWelcom to The Intelligence menu")
    print("-----------------------------------------------")
    print("- To go back to the main menu press :  0")
    print("- To Find the Connected Components of red pixels in image press :  1")
    print("- To Find the Connected Components of red pixels in image press :  2")
    print("\n")
    
    img = cv2.imread("data/map.png")
    img = np.array(img)
    
    while True:
        User = input("Enter One of (0, 1, 2, 3): ")
        if User in {'0', '1', '2', '3'}:
            break
        else: 
            print(f"Invalid Input ! {User}")
            print("Try Again and Choose From: (0, 1, 2, 3)")
            
    if User == '0' : 
        main_menu()
    elif User == '1':
        print("\t\n________Red Pixels_______")
        print("--------------------------------------------\n")
        img = find_red_pixels(img)
        detect_connected_components(img)
    elif User == '2':
        print("\t\n________Cyan Pixels________")
        print("--------------------------------------------\n")
        img = find_cyan_pixels(img)
        detect_connected_components(img)
    


    
    main_menu()
def about():
    """ This function will activate if the user presses (A) or (a) in the main menu and displays
    the personal information about the person who made this project and returns to the main menu 
    
    Argument(s) : 
    ---------------
    No arguments is passed to this function 
    ---------------
    Note(s) : This program will always go back to main menu.
    ---------------
    Return(s) : This function doesn't return anything and only display information if necessary
    """
    
    print("\n\tWelcom to The About menu")
    print("---------------------------------------")
    print("- To go back to the main menu press :  0")
    print("- To See Information about the project press :  1")
    print("- To See Information about the Module and Student press :  2")
    print("\n")
    
    
    while True:
        user = input("Enter One of (0, 1, 2): ")
        if user in {'0', '1', '2'}:
            break
        else: 
            print(f"Invalid Input ! {user}")
            print("Try Again and Choose From: (0, 1, 2)")
    
    if user == '0' : 
        main_menu()
    elif user == '1':
        print("This project is used to access data in a more appropiate way and have more controll over the given data")
        print("All the necessary information is provided to user as the user navigates through the program (project)")
        print("This program has 3 main functions which provide different services : \n")
        print("- The Pollution Reporting module (PR): Allowing the user to manage the monitoring station data with more flexibility")
        print("- The Mobility Intelligence module (MI): Allowing the user to detect red and blue pixels in a picture and detect the connected components whithin them ")
        print("- The Real-time Monitoring module (RM): Allowing the user to receive live data from the site and manage them with more flexibility")
        about()
    
    elif user == '2' : 
        print("\nFull Name of the Student : Amirali Famili ")
        print("Student Number : 720060845")
        print("Candidate Number : 022378")
        print("Module Code : ECM1400\n")
        about()
        
    main_menu()
def quit():
    """This function will activate if users presses (Q) or (q) and it will terminate the program
    
    Argument(s) : 
    ---------------
    No arguments is passed to this function 
    ---------------
    Note(s) : 
    - This program will always terminate the hole project.
    - this function will terminate the program even if the user dosen't have Python standard library
    ---------------
    Return(s) : This function doesn't return anything and only shuts the program down if necessary
    """
    print("Goodbye...")
    try : 
       sys.exit()
    except: 
        exit()
        
if __name__ == '__main__':
    main_menu()
    
    
    