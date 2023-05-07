# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
import numpy as np 
import xml.etree.cElementTree as et
import requests as req
import datetime
import re
import xmltodict 
import csv 
import urllib
from utils import *

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
    
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date)
    
    res = req.get(url)
    return res.json()


def rm_function_2(group_names):
    """Your documentation goes here"""
    #groumnames_obj = "http://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName={GROUPNAME}/Json" this one isn't working not reaching the website 
    """
    info_monitoringsites_groupnames = f"http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={group_names[i]}/Json"
    info_monitor_species_groupnames = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={group_names[i]}/Json"
    hourly_groupname = f"http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName={group_names[i+1]}/Json"
    info_groupnames = f"http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringLocalAuthority/GroupName={group_names[i+1]}/Json"
    """
    
    for i in range(1, int(len(group_names))-1):# this doesn't print/return the all 

        info_groupnames = f"http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringLocalAuthority/GroupName={group_names[i+1]}/Json"
        get_url = req.get(info_groupnames)
        try: 
            information = get_url.json()
        except: 
            print("Request Error, bad url")
        
        #print(info_groupnames)
        key = list(information.keys())
        key2 = list(information[key[0]].keys())
        
        info_keys = []
        info_values = []
        k = ""
        v = ""
        for j in list(information[key[0]][key2[0]]): 
            try : 
                for key,values in j.items(): 
                    #print(key,":",values)
                    pass
            except:
                repeating_keys = list(information[key[0]][key2[0]].keys())
                repeating_values = list(information[key[0]][key2[0]].values())
                
                if k == repeating_keys : 
                    pass
                else : 
                    info_keys.append(repeating_keys)
                    
                if v == repeating_values : 
                    pass
                else : 
                    info_values.append(repeating_values)
                
                k = repeating_keys
                v = repeating_values
        
        #print(info_keys, "\n", info_values)
    
#rm_function_2(group_names)
#print(group_names)



def rm_function_4(*args,**kwargs):
    """Your documentation goes here"""

    # each of these urls have diffrent style of displaying information 
    # how to group them in diffrent functions properly ???? 
    
    groumnapes_obj = "http://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName={GROUPNAME}/Json"
    year_groumnapes_requiered = "https://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/GroupName={GROUPNAME}/Year={YEAR}/Json"
    year_localauthorityid_requiered = " http://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/LocalAuthorityId={LOCALAUTHORITYID}/Year={YEAR}/Json"
    sitecode_sitedate = "http://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/SiteCode={SITECODE}/StartDate={STARTDATE}/Json"
    sitecode_year = "http://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringObjective/SiteCode={SITECODE}/Year={YEAR}/Json"
    sitecode_year_obj = "https://api.erg.ic.ac.uk/AirQuality/Annual/MonitoringReport/SiteCode={SITECODE}/Year={YEAR}/Json"
    year_site_backa_backb_backc_backd_mean = "http://api.erg.ic.ac.uk/AirQuality/Annualiser/Calculate/year={YEAR}/site={SITE}/backA={BACKA}/backB={BACKB}/backC={BACKC}/backD={BACKD}/species={SPECIES}/mean={MEAN}/Json"
    year_species = "http://api.erg.ic.ac.uk/AirQuality/Annualiser/Sites/year={YEAR}/species={SPECIES}/Json"
    groupname_date = "https://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/GroupName={GROUPNAME}/Date={DATE}/Json"
    groupname_indx = " http://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/GroupName={GROUPNAME}/Json"
    localauthorityid = "http://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/LocalAuthorityId={LOCALAUTHORITYID}/Json"
    sitecode_indx = "http://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode={SITECODE}/Json"
    localauthorityid_date = "http://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/LocalAuthorityId={LOCALAUTHORITYID}/Date={DATE}/Json"
    date_sitecode = "http://api.erg.ic.ac.uk/AirQuality/Daily/MonitoringIndex/SiteCode={SITECODE}/Date={DATE}/Json"
    code_montype = "http://api.erg.ic.ac.uk/AirQuality/Data/DiffusionTube/code={CODE}/montype={MONTYPE}/Json"
    sitecode_startdate_enddate = "https://api.erg.ic.ac.uk/AirQuality/Data/Site/SiteCode={SITECODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/Json"
    sitecode_startdate_enddate_csv = "https://api.erg.ic.ac.uk/AirQuality/Data/Site/Wide/SiteCode={SITECODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/csv"
    sitecode_speciescode_startdate_enddate = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiCODE}/SpteCode={SITEeciesCode={SPECIESCODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/Json"
    sitecode_speciescode_startdate_enddate = "http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={SITECODE}/SpeciesCode={SPECIESCODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/csv"
    period_units_step_json = "http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={SITECODE}/SpeciesCode={SPECIESCODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/Period={PERIOD}/Units={UNITS}/Step={STEP}/Json"
    sitecode_speciescode_period_json = "http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpeciesIndexDays/SiteCode={SITECODE}/SpeciesCode={SPECIESCODE}/Period={PERIOD}/Json"
    traffic = "https://api.erg.ic.ac.uk/AirQuality/Data/Traffic/Site/SiteCode={SITECODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/Json"
    wide_json = "http://api.erg.ic.ac.uk/AirQuality/Data/Wide/Site/SiteCode={SITECODE}/StartDate={STARTDATE}/EndDate={ENDDATE}/Json"
    hourly_map_speciesname = "http://api.erg.ic.ac.uk/AirQuality/Hourly/Map/SpeciesName={SPECIESNAME}/Json"
    hourly_groupname = "http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName={GROUPNAME}/Json"
    hourly_sitecode = " http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/SiteCode={SITECODE}/Json"
    info_health_airqualityoindex = "http://api.erg.ic.ac.uk/AirQuality/Information/IndexHealthAdvice/AirQualityIndex={AIRQUALITYINDEX}/Json"
    info_groupnames = "http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringLocalAuthority/GroupName={GROUPNAME}/Json"
    info_monitoringsites_groupnames = "http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={GROUPNAME}/Json"
    info_monitor_species_groupnames = " https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={GROUPNAME}/Json"
    info_skip_limit = "http://api.erg.ic.ac.uk/AirQuality/Information/News/Skip={SKIP}/limit={LIMIT}/Json"
    speciescode = "https://api.erg.ic.ac.uk/AirQuality/Information/Species/SpeciesCode={SPECIESCODE}/Json"
    
    info_obj = "http://api.erg.ic.ac.uk/AirQuality/Information/Objective/Json"
    hourly_map = "http://api.erg.ic.ac.uk/AirQuality/Hourly/Map/Json"
    info_guide = "https://api.erg.ic.ac.uk/AirQuality/Information/AirPollutionGuide/Json"
    info_guide = "http://api.erg.ic.ac.uk/AirQuality/Information/Documentation/pdf"
    info_groups = "http://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json"
    info_health = "http://api.erg.ic.ac.uk/AirQuality/Information/IndexHealthAdvice/Json"
    info_species = "http://api.erg.ic.ac.uk/AirQuality/Information/Species/Json"
    info_terms = "http://api.erg.ic.ac.uk/AirQuality/Information/Terms/pdf"
    
    # i have to decide the style of the monitoring and how to involve the user in this program
    
def get_species_code():
    hourly_map = "http://api.erg.ic.ac.uk/AirQuality/Hourly/Map/Json"
    
    get_url = req.get(hourly_map)
    website = get_url.json()
    user_species_code = [i['@SpeciesCode'] for i in  website['Maps']['Map']]
    print("user species code : " , user_species_code)
    user_input_text = "Enter a species code :"
    user_input = input(user_input_text)
    if user_input in user_species_code : 
        
        return website , user_input
    else : 
        print("User species code not entered correctly...")
        get_species_code()
    
species_code = 'NO2'
def get_hourly_map_date(website, species_code):
    for idx,spc in enumerate(website['Maps']['Map']):
        if spc['@SpeciesCode'] == species_code:
            return website['Maps']['Map'][idx]['@EndDate'],website['Maps']['Map'][idx]['@StartDate']

#website,species_cose = get_species_code()
#start,end = get_hourly_map_date(website,species_code)



def url_info_groupnames(group_names):
    
    #print(group_names)
    #user = input("Enter one of the group names")
    i = "All"

    
    info_groupnames = f"http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringLocalAuthority/GroupName={i}/Json"
    
    
    # for local authorities : (info groups)
    url = info_groupnames
    get_url = req.get(url)
    website = get_url.json()
    
    key = list(website.keys())
    subkeys = list(website[key[0]].keys())
    subvalues = list(website[key[0]].values())
   
    subvalues = subvalues[0]
    try: 
        for ky,val in subvalues.items(): 
            print(f" {ky} : {val} ")
    except:
        for k in subvalues:
            for ky,val in k.items(): 
                print(f" {ky} : {val} ")

        
#url_info_groupnames(group_names)# none is usefull

def url_info_houtly_groupname(group_names , user_site): # The problem with returns 
    
    hourly_groupname = f"http://api.erg.ic.ac.uk/AirQuality/Hourly/MonitoringIndex/GroupName={group_names}/Json"
    
    url = hourly_groupname
    get_url = req.get(url)
    website = get_url.json()
    
    key = list(website.keys())
    subkeys = list(website[key[0]].keys())
    subvalues = list(website[key[0]].values())
    All_site_names = []
    
    try : 
        if type(subvalues[2]) == list : 
            for k in subvalues[2] : 
                for ky,val in k.items():
                    if ky == "Site":
                        if type(val) == list : 
                            for j in val : 
                                site_code = j["@SiteCode"]
                                site_name = j["@SiteName"]
                                if site_name == user_site :
                                    site = []
                                    site.append(site_code) 
                                    print(site_code,"HI") 
                                    return site_code
                                All_site_names.append(site_name)
                                #print(f" Site Name : {site_name}")
                                #print(f" Site Code : {site_code}")
                                if type(j["Species"]) == list :
                                    for m in j["Species"] : 
                                        species_name = m["@SpeciesDescription"]
                                        species_code = m["@SpeciesCode"]
                                        #print(f" Species Name : {species_name}")
                                        #print(f" Species Code : {species_code}")
                                elif type(j["Species"]) == dict :
                                    species_name = j["Species"]["@SpeciesDescription"]
                                    species_code = j["Species"]["@SpeciesCode"]
                                    #print(f" Species Name : {species_name}")
                                    #print(f" Species Code : {species_code}")
                                
                        elif type(val) == dict :
                            site_code = val["@SiteCode"]
                            site_name = val["@SiteName"]
                            #print(f" Site Name : {site_name}")
                            #print(f" Site Code : {site_code}")
                            if site_name == user_site :
                                site = []
                                site.append(site_code) 
                                print(site_code,"HI2") 
                                return site_code
                            All_site_names.append(site_name)
                            #print(f" Site Name : {site_name}")
                            #print(f" Site Code : {site_code}")
                            if type(val["Species"]) == list :
                                for m in val["Species"] : 
                                    species_name = m["@SpeciesDescription"]
                                    species_code = m["@SpeciesCode"]
                                    #print(f" Species Name : {species_name}")
                                    #print(f" Species Code : {species_code}")
                            elif type(val["Species"]) == dict :
                                species_name = val["Species"]["@SpeciesDescription"]
                                species_code = val["Species"]["@SpeciesCode"]
                                #print(f" Species Name : {species_name}")
                                #print(f" Species Code : {species_code}")
        elif type(subvalues[2]) == dict : 
            for ky,val in subvalues[2].items():
                    if ky == "Site":
                        if type(val) == list : 
                            for j in val : 
                                site_code = j["@SiteCode"]
                                site_name = j["@SiteName"]
                                if site_name == user_site :
                                    site = []
                                    site.append(site_code) 
                                    print(site_code,"HI1") 
                                    return site_code
                                All_site_names.append(site_name)
                                #print(f" Site Name : {site_name}")
                                #print(f" Site Code : {site_code}")
                                if type(j["Species"]) == list :
                                    for m in j["Species"] : 
                                        species_name = m["@SpeciesDescription"]
                                        species_code = m["@SpeciesCode"]
                                        #print(f" Species Name : {species_name}")
                                        #print(f" Species Code : {species_code}")
                                elif type(j["Species"]) == dict :
                                    species_name = j["Species"]["@SpeciesDescription"]
                                    species_code = j["Species"]["@SpeciesCode"]
                                    #print(f" Species Name : {species_name}")
                                    #print(f" Species Code : {species_code}")
                                
                        elif type(val) == dict:
                            site_code = val["@SiteCode"]
                            site_name = val["@SiteName"]
                            #print(f" Site Name : {site_name}")
                            #print(f" Site Code : {site_code}")
                            if site_name == user_site :
                                site = []
                                site.append(site_code) 
                                print(site_code,"HI")
                                Site = site_code 
                                return print("hi")
                            All_site_names.append(site_name)
                            #print(f" Site Name : {site_name}")
                            #print(f" Site Code : {site_code}")
                            if type(val["Species"]) == list :
                                for m in val["Species"] : 
                                    species_name = m["@SpeciesDescription"]
                                    species_code = m["@SpeciesCode"]
                                    #print(f" Species Name : {species_name}")
                                    #print(f" Species Code : {species_code}")
                            elif type(val["Species"]) == dict :
                                species_name = val["Species"]["@SpeciesDescription"]
                                species_code = val["Species"]["@SpeciesCode"]
                                #print(f" Species Name : {species_name}")
                                #print(f" Species Code : {species_code}")
    except : 
        print("No Record of Data in This Group Name")
        print(url)
        
    
    if len(All_site_names) != 0 : 
        print("These Are All The Sites : ", All_site_names)
        user_site = input("Choose from the given Site Names : ")
        url_info_houtly_groupname(group_names, user_site)
    else : 
        print("No Record of Sites Found in the Given Groupname ... ")
        return url
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
def get_group_names():
    """ This is a functions that recieves information about group names from a particular url 
    and will return all the group names as a list 
    
    Argument(s) : 
    ---------------
    - No argumments is passed to this function 
    ---------------
    Note(s) : This function reads a json format pre defined url to return all group names 
    ---------------
    Return(s) : This function return's a list containing all the group names 
    """
    
    info_groups = "http://api.erg.ic.ac.uk/AirQuality/Information/Groups/Json"
    url = info_groups
    get_url = req.get(url)
    try: 
        url = get_url.json()
    except: 
        print("Request Error, bad url")
   
    group_length = len(url["Groups"]["Group"])
    group_names = []
    for i in range(group_length):
        group_names.append(url["Groups"]["Group"][i]["@GroupName"])
    
    return group_names


def get_site_names_single(group_name):
    """ This is a functions that recieves a particular group name choosen by the user and place 
    the group name into a specific url and returns information about the sitenames for a single pollutant 
    
    Argument(s) : 
    ---------------
    - group_name : a particular group name choosen from the list of group names by the user 
    ---------------
    Note(s) : This function reads a json format pre defined url to return all Site names 
    ---------------
    Return(s) : This function return's a list containing all the Site names 
    """
    info_monitor_species_groupnames = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={group_name}/Json" 
    
    url = info_monitor_species_groupnames
    try : 
        get_url = req.get(url)
        website = get_url.json()
    except : 
        print("Request Error (bad url) try a different groupname")
        
    key = list(website.keys())
    subvalues = list(website[key[0]].values())
    All_site_names = []
    subvalues = subvalues[0]
    
    try : 
        for i in subvalues:
            for ky,val in i.items() :
                if type(val) == str : 
                    if ky == "@SiteName" :
                        site_name = i["@SiteName"]
                        All_site_names.append(site_name)
        All_site_names = set(All_site_names)
        return All_site_names
    except:
        for ky,val in subvalues.items() :
                if type(val) == str : 
                    if ky == "@SiteName" :
                        site_name = subvalues["@SiteName"]
                        All_site_names.append(site_name)
        All_site_names = set(All_site_names)
        print(url)
        return All_site_names
    
def get_site_names_all(group_name):
    """ This is a functions that recieves a particular group name choosen by the user and place 
    the group name into a specific url and returns information about the sitenames for all pollutants 
    
    Argument(s) : 
    ---------------
    - group_name : a particular group name choosen from the group names list by the user 
    ---------------
    Note(s) : This function reads a json format pre defined url to return all Site names 
    ---------------
    Return(s) : This function return's a list containing all the Site names 
    """
    info_monitoringsites_groupnames = f"http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={group_name}/Json"
    
    url = info_monitoringsites_groupnames
    try : 
        get_url = req.get(url)
        website = get_url.json()
    except : 
        print("Request Error (bad url) try a different groupname")
        
    key = list(website.keys())
    subvalues = list(website[key[0]].values())
    All_site_names = []
    subvalues = subvalues[0]
    
    try : 
        for i in subvalues:
            for ky,val in i.items() :
                if type(val) == str : 
                    if ky == "@SiteName" :
                        site_name = i["@SiteName"]
                        All_site_names.append(site_name)
        All_site_names = set(All_site_names)
        return All_site_names
    except:
        for ky,val in subvalues.items() :
                if type(val) == str : 
                    if ky == "@SiteName" :
                        site_name = subvalues["@SiteName"]
                        All_site_names.append(site_name)
        All_site_names = set(All_site_names)
        print(url)
        return All_site_names
    
def url_info_monitoring(site):
    """ This is a functions that recieves a particular Site name choosen by the user and place 
    the group name into a specific url and returns information about the Site code(s) and Pollutant Code(s).
    
    Argument(s) : 
    ---------------
    - site : a particular Site choosen from the list of site names by the user 
    ---------------
    Note(s) : This function reads a json format pre defined url to return all Site code(s) and Pollutant Code(s)
    - This function will search for the Site name in all cities to find a match 
    ---------------
    Return(s) : This function return's Two lists containing all the Site Code(s) and Pollutant Code(s) respectively 
    """
    group_name = "All"
    info_monitoringsites_groupnames = f"http://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSites/GroupName={group_name}/Json"
    
    url = info_monitoringsites_groupnames
    get_url = req.get(url)

    website = get_url.json()
    
    key = list(website.keys())
    subvalues = list(website[key[0]].values())
    subvalues = subvalues[0]
    
    user_site_code = []
    user_species_code = [] 
    
    for i in subvalues:
        for ky,val in i.items() :
            if type(val) == str : 
                if ky == "@SiteName" :
                    site_name = i["@SiteName"]
                    if site == site_name:
                        site_code = i["@SiteCode"]
                        user_site_code.append(site_code) 
            elif type(val) == list and len(user_site_code) != 0:
                for k in val :
                    for key1,value1 in k.items():
                        if value1 == k["@SpeciesCode"]:
                            species_code = k["@SpeciesCode"]
                            species_name = k["@SpeciesDescription"]
                            user_species_code.append(species_code)
                return user_site_code , user_species_code
            elif type(val) == dict and len(user_site_code) != 0: 
                for key1,value1 in val.items():
                    if value1 == val["@SpeciesCode"]:
                        species_code = val["@SpeciesCode"]
                        species_name = val["@SpeciesDescription"]
                        user_species_code.append(species_code)
                return user_site_code , user_species_code
    
    user_site_code = set(user_site_code)
    user_species_code = set(user_species_code)
    return list(user_site_code) , list(user_species_code)

def url_info_monitoring_species(site):
    """ This is a functions that recieves a particular Site name choosen by the user and place 
    the group name into a specific url and returns information about the Site code(s) and Pollutant Code(s).
    
    Argument(s) : 
    ---------------
    - site : a particular Site choosen from the list of site names by the user 
    ---------------
    Note(s) : This function reads a json format pre defined url to return all Site code(s) and Pollutant Code(s)
    - This function will search for the Site name in all cities to find a match 
    ---------------
    Return(s) : This function return's Two lists containing all the Site Code(s) and Pollutant Code(s) respectively 
    """
    group_name = "All"
    info_monitor_species_groupnames = f"https://api.erg.ic.ac.uk/AirQuality/Information/MonitoringSiteSpecies/GroupName={group_name}/Json" 
    
    url = info_monitor_species_groupnames
    get_url = req.get(url)

    website = get_url.json()
    
    key = list(website.keys())
    subvalues = list(website[key[0]].values())
    subvalues = subvalues[0]
    
    user_site_code = []
    user_species_code = [] 
    
    for i in subvalues:
        for ky,val in i.items() :
            if type(val) == str : 
                if ky == "@SiteName" :
                    site_name = i["@SiteName"]
                    if site == site_name:
                        site_code = i["@SiteCode"]
                        user_site_code.append(site_code) 
            elif type(val) == list and len(user_site_code) != 0:
                for k in val :
                    for key1,value1 in k.items():
                        if value1 == k["@SpeciesCode"]:
                            species_code = k["@SpeciesCode"]
                            species_name = k["@SpeciesDescription"]
                            user_species_code.append(species_code)
                return user_site_code , user_species_code
            elif type(val) == dict and len(user_site_code) != 0: 
                for key1,value1 in val.items():
                    if value1 == val["@SpeciesCode"]:
                        species_code = val["@SpeciesCode"]
                        species_name = val["@SpeciesDescription"]
                        user_species_code.append(species_code)
                return user_site_code , user_species_code
    
    user_site_code = set(user_site_code)
    user_species_code = set(user_species_code)
    return list(user_site_code) , list(user_species_code)


def get_answer_from_the_user(site_code , species_code): 
    """ This is a functions that recieves a site code and species code and will make sure that 
    futur functions that are using site code and species code will recieve the right data and returns the site code 
    and species code as a string. 
    
    Argument(s) : 
    ---------------
    - site_code : a list of all available site code(s) inside a site 
    - species code : a list of all available species code(s)  inside a site 
    ---------------
    Note(s) : This function is making sure that the data is passing to other relevant functions in a correct form 
    ---------------
    Return(s) : This function return's Two strings containing the Site Code and Pollutant Code respectively 
    """
    if len(site_code) > 1 : 
        while True : 
            print(f"All The site codes of this website : {site_code}")
            user = input("Enter one of the (site codes)")
            if user not in site_code : 
                print(f"Invalid input ({user}) ... Try Again")
            else : 
                user = site_code
                break
    else : 
        try : 
            site_code = site_code[0]
        except : 
            return print("No Data Found On The Server")
    if len(species_code) > 1 : 
        while True : 
            print(f"All The species code on this website : {species_code}")
            user = input("Enter one of the species code ")
            if user not in species_code : 
                print(f"Invalid input ({user}) ... Try Again")
            else : 
                species_code = user
                break
    elif len(species_code) == 1 : 
        species_code = species_code[0]
    else : 
        species_code = "NO"
    return site_code , species_code 


def convert_csv_url_to_data(site_code , species_code, start_date=None, end_date=None) : 
    """ This is a functions that recieves a site code, species code, start date and end date 
    choosen by the user to recieve the right csv file from the api and convert that data to a list 
    for later calculations. 
    
    Argument(s) : 
    ---------------
    - site_code : a string containing the site code of the choosen site by the user 
    - species code : a string of a particular pollutant species code choosen by the user 
    ---------------
    Note(s) : This function will set the start date and end date to the current day if no start date or end date is entered by the user 
    - This function will convert the csv url recieved by the api into a list for later calculations 
    ---------------
    Return(s) : This function return's data recived from the csv url from the api as a list 
    """
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    if species_code == "NO" : 
        url = f"https://api.erg.ic.ac.uk/AirQuality/Data/Site/Wide/SiteCode={site_code}/StartDate={start_date}/EndDate={end_date}/csv" # All pollutants
    elif type(site_code) == str and type(species_code) == str and species_code != "NO" : 
        url = f"http://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/csv" # A particular pollutant 
    
    with req.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        info = csv.reader(decoded_content.splitlines(), delimiter=',')

    data = list(info)
    print( "URL of the website : ", url)
    return data

def get_data (data, Site):
    """ This is a functions that recieves data and site name to detect the available data 
    on the website and add the data from the pollutants to relavent lists specified for that pollutant 
    
    Argument(s) : 
    ---------------
    - data : a list containing all available data that exists in the csv url in the api
    - Site : a string containing site name recived by the user inside main_menu()
    ---------------
    Note(s) : This function will use the header of the file to find available pollutants and will remove it from the data after wards 
    - This function will add all available pollutant data to their relavent lists . 
    ---------------
    Return(s) : This function return's a list containing all available pollutant data inside the main data list as a 2D list 
    """
    
    
    header = data[0]
    data.pop(0)
    All_available_data = []
    for i in range(1,len(header)):
        if header[i] == f"{Site}: Nitric Oxide (ug/m3)" :
            No = []
            No.append("No")
            for d in data : 
                No.append(d[i])
            if len(No) >= 1 :
                All_available_data.append(No)
        elif header[i] == f"{Site}: Nitrogen Dioxide (ug/m3)" :
            No2 = []
            No2.append("No2")
            for d in data : 
                No2.append(d[i])
            if len(No2) >= 1 :
                All_available_data.append(No2)
        elif header[i] == f"{Site}: Oxides of Nitrogen (ug/m3)" :
            Nox = []
            Nox.append("Nox")
            for d in data : 
                Nox.append(d[i])
            if len(Nox) >= 1 :
                All_available_data.append(Nox)
        elif header[i] == f"{Site}: PM10 Particulate (ug/m3)" :
            Pm10 = []
            Pm10.append("Pm10")
            for d in data : 
                Pm10.append(d[i])
            if len(Pm10) >= 1 :
                All_available_data.append(Pm10)
        elif header[i] == f"{Site}: PM2.5 Particulate (ug/m3)" :
            Pm25 = []               
            Pm25.append("Pm25")
            for d in data : 
                Pm25.append(d[i])
            if len(Pm25) >= 1 :
                All_available_data.append(Pm25)
        elif header[i] == f"{Site}: Carbon Monoxide (mg/m3)" :
            Co = [] 
            Co.append("Co")
            for d in data : 
                Co.append(d[i])
            if len(Co) >= 1 :
                All_available_data.append(Co)
        elif header[i] == f"{Site}: Ozone (ug/m3)" :
            o3 = []
            o3.append("o3")
            for d in data : 
                o3.append(d[i])
            if len(o3) >= 1 :
                All_available_data.append(o3)
        elif header[i] == f"{Site}: Sulphur Dioxide (ug/m3)" :
            So2 = []
            So2.append("So2")
            for d in data : 
                So2.append(d[i])
            if len(So2) >= 1 :
                All_available_data.append(So2)
        elif header[i] == f"{Site}: Benzene (ug/m3)" :
            benzen = []
            benzen.append("benzen")
            for d in data : 
                benzen.append(d[i])
            if len(benzen) >= 1 :
                All_available_data.append(benzen)
        else : 
            print("Unknown Pollutant Detected...")  
    return All_available_data

def fill_missing(data):
    """ This is a functions that recieves a list of pollutant data and will detect and replace the 
    missing data by the new value specified by the user (inside the function) and will return the 
    filled data with missing values 
    
    Argument(s) : 
    ---------------
    - data : a list containing all available pollutant extracted from main data list 
    ---------------
    Note(s) : This function will ask for a new value inside it from the user . 
    - This function will replace all missing values inside the input with the given value entered by the user 
    ---------------
    Return(s) : This function return's the input it self with filled missing data(s)
    """
    while True:
        new_value = input("Enter a new value to replace : ")
        try : 
            float(new_value)
            break
        except : 
            print(f"Invalid Input ! {new_value}")
            print("Try Again and enter a valid number")
            
    for i in range(len(data)): 
        try: 
            float(data[i])
        except:
            data[i] = new_value
    return data


def manage_available_data (All_available_data):
    """ This is a functions that recieves a 2D list containing all available pollutant data and will 
    make sure that all missing data(s) are either removed or replaced and returns a 2D list 
    containing all pollutant data with no missing data(s).
    
    Argument(s) : 
    ---------------
    - All_available_data : a 2D list containing all available pollutant data in the main data list that exists inside the api 
    ---------------
    Note(s) : This function will ask for a new value inside it from the user . 
    - This function will detect if there is no pollutant data and returns None . 
    - This function will ask the user to remove or replace missing value(s) inside the 2D pollutant list
    ---------------
    Return(s) : This function return's a 2D list containing all filled or removed data from relavent pollutant(s) inside  main data list (returns all numbers)
    """
    count_all = 0
    names = []
    for i in All_available_data : 
        name = i[0]
        names.append(name)
        i.pop(0)
        count = 0
        for j in i : 
            if j == "":
                count += 1
        if count == len(i) : 
            print(f"No Data on ({name})")
            count_all += 1
    if count_all == len(All_available_data):
        return None , None
    
    if count != 0:
        print("There are few data(s) Missing")
        print("Enter (R) to replace them or (D) to Delete( or remove) them for analysing")
        new_data = []
        while True:
            user = input("Enter (R) to replace or (D) to remove : ")
            if user in {'R', 'r'}: 
                for k in range(len(All_available_data)): 
                    print(f"Enter a value for missing ({names[k]}) Data(s)")
                    data = fill_missing(All_available_data[k])
                    new_data.append(data)
                    print(f" {names[k]} data replaced")
                break
            elif user in {'D', 'd'}:
                for k in All_available_data: 
                    for m in range(len(k)): 
                        try : 
                            float(k[m])
                        except:
                            k = [l for l in k if l != ""]

                new_data = All_available_data
                break
            else : 
                print(f"Invalid Input ! {user}")
                print("Try Again and Choose From (R, r, D, d)")
    else : 
        new_data = All_available_data
        
    return new_data, names 



    """
    
    These functions should be decided then document 
    
    the missing and removing datas should be fixed 
    
    
    """


def calculate_Sum_data (new_data, names):
   for values in range(len(new_data)) : 
       sum = sumvalues(new_data[values])
       print(f"Sum of {names[values]} available in the data : {sum} ")

def calculate_Maxvalue_data (new_data, names):
   for values in range(len(new_data)) : 
       max = maxvalue(new_data[values])
       print(f"highest amount of pollutant {names[values]} available in the data : {max}")
       
def calculate_Minvalue_data (new_data, names):
   for values in range(len(new_data)) : 
       min = minvalue(new_data[values])
       (f"highest amount of pollutant {names[values]} available in the data : {min}")
       
def calculate_Meanvalue_data (new_data, names):
   for values in range(len(new_data)) : 
       mean = meannvalue(new_data[values])
       print(f"Sum of {names[values]} available in the data : {mean} ")




