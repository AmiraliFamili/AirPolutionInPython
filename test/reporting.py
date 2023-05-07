import numpy as np 
from csv import reader

def daily_average(data, monitoring_station, pollutant):
    """ This is a functions that calculates the daily average of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base and returns the daily averages in the year 2021-2022 as a list 
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    ---------------
    Note(s) : This program will not function if there is missing data (No data) within the (data) variable.
    ---------------
    Return(s) : This function return's the average of a particular pollutant in all days within the given data (365 values) in a list
    """
     
    if pollutant == "no": 
        index = 2
    elif pollutant == "pm10": 
        index = 3
    elif pollutant == "pm25": 
        index = 4
    
    data = np.array(data)
    data_col = data[::,index].astype(float)
    data_col = data_col.reshape((365,24))
    return data_col.mean(axis = 1)

def daily_median(data, monitoring_station, pollutant):
    """ This is a functions that calculates the daily median of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base and returns the daily medians in the year 2021-2022 as a list 
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    ---------------
    Note(s) : This program will not function if there is missing data (No data) within the (data) variable.
    ---------------
    Return(s) : This function return's the median of a particular pollutant in all days within the given data (365 values) in a list
    """

    if pollutant == "no": 
        index = 2
    elif pollutant == "pm10": 
        index = 3
    elif pollutant == "pm25": 
        index = 4
        
    data = np.array(data)
    data_col = data[::,index].astype(float)
    data_col = data_col.reshape((365,24))
    return np.median(data_col, axis = 1)

def hourly_average(data, monitoring_station, pollutant):
    """ This is a functions that calculates the hourly average of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base in every hour of all the days that exists in data and returns the average of all 24 hours 
    from all the days in data in year 2021-2022 as a list 
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    ---------------
    Note(s) : This program will not function if there is missing data (No data) within the (data) variable.
    ---------------
    Return(s) : This function return's the hourly average of 24 hours of the day from all days within the given data (24 values) in a list
    """
  
    if pollutant == "no": 
        index = 2
    elif pollutant == "pm10": 
        index = 3
    elif pollutant == "pm25": 
        index = 4
    
    data = np.array(data)
    data_col = data[::,index].astype(float)
    data_col = data_col.reshape((24,365))
    return data_col.mean(axis = 1)

def monthly_average(data, monitoring_station, pollutant):
    """ This is a functions that calculates the monthly average of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base and returns the monthly averages (average of pollutant in all days of 12 months)
    in the year 2021-2022 as a list 
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    ---------------
    Note(s) : This program will not function if there is missing data (No data) within the (data) variable.
    - this program's structure is different from the rest of the functions because we have different days within each month
    ---------------
    Return(s) : This function return's the average of a particular pollutant in all days in all months within the given data (12 values) in a list
    """
    
    if pollutant == "no": 
        index = 2
    elif pollutant == "pm10": 
        index = 3
    elif pollutant == "pm25": 
        index = 4
    average = []
    data = np.array(data)
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    newdata =[]
    total_days = 0 
    for days in month:
        newdata.append(data[total_days:total_days + 24*days,index])
        total_days += days * 24
    for i in range(12):
        sum = 0
        for j in newdata[i]:
            sum += float(j) 
        sum = sum / len(newdata[i])
        average.append(sum)
    return average

def peak_hour_date(data, date, monitoring_station,pollutant):
    """ This is a functions that calculates the peak hour of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base and returns the max amount of pollutant in a particular date
    in the year 2021-2022 as a float
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    - date : a specific date entered by the user to search for the max value of pollutant within that date 
    ---------------
    Note(s) : This program will not function if there is missing data (No data) within the (data) variable.
    ---------------
    Return(s) : This function return's the max amount of a particular pollutant in a specific date within the given data (1 variable) as a float
    """

    if pollutant == "no" : 
        index = 2
    elif pollutant == "pm10" : 
        index = 3
    elif pollutant == "pm25" : 
        index = 4
        
    max = 0
    k = 0
    for i in  data : 
        if i[0] == date : 
            k = k + 1
            try : 
                if max <= float(i[index]) : 
                    max = float(i[index]) 
            except : 
                pass 
    if k == 24 :
        return max
        
def count_missing_data(data, monitoring_station, pollutant):
    """ This is a functions that calculates the missing data(s) of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base and returns the number of missing data (No data) in the year 2021-2022 as an integer
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    ---------------
    Note(s) : This function only count the missing data(s) (No data) of one pollutant at a time entered by the user 
    ---------------
    Return(s) : This function return's the number of missing data(s) (No data) of a particular pollutant in the given data (1 variable) as an integer
    """

    total = 0 
    if pollutant == "no" : 
        index = 2
    elif pollutant == "pm10" : 
        index = 3
    elif pollutant == "pm25" : 
        index = 4
        
    for i in data : 
        if i[index] == "No data": 
            total += 1
    return total

def fill_missing_data(data, new_value,  monitoring_station, pollutant):
    """ This is a functions that fills the missing data(s) (No data) of a particular pollutant in three monitoring station 
    (Harlington, Kensington, Marylebone) data base and returns the new data in the year 2021-2022 as a list 
    
    Argument(s) : 
    ---------------
    - data : data from the monitoring station
    - monitoring_station : the name of the monitoring station
    - pollutant : the name of one of the pollutants (no, pm10, pm25)
    - new_value : the new value assigned by the user to be replaced with missing data(s) (No data)
    ---------------
    Note(s) : This function only fills the missing data(s) (No data) of one pollutant at a time entered by the user 
    ---------------
    Return(s) : This function return's the new data (or filled missing data) of a particular pollutant in data (1 variables) as a list
    """
    
    if pollutant == "no": 
        index = 2
    elif pollutant == "pm10": 
        index = 3
    elif pollutant == "pm25": 
        index = 4

    for i in data: 
        try: 
            float(i[index])
        except:
            i[index] = new_value
    return data


