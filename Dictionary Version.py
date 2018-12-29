def get_data_from_url(url):
    '''
    Gets json from url, decodes json, and returns data
    '''
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data

def get_values_from_list_of_dict(ldict, old_key, new_key):
    '''
    Function to extract required values from a list of dictionaries and return a new list of dictionaries with required values
    @param ldict - list of dictionaries to extract from
    @param old_key - key in ldict corresponding to value of interest
    @new_key - key name chosen to correspond with value in new dictionary
    '''
    new_ldict = []
    for item in ldict:
        new_dict = {}
        new_dict[new_key] = item[old_key]
        new_ldict.append(new_dict)
    return new_ldict
        

import urllib.request
import json

#Top Level Variables
CURRENT_YEAR = "2018"
CURRENT_SEASON = "fall"
SFU_DATA_WEBSITE = "http://www.sfu.ca/bin/wcm/course-outlines?"+CURRENT_YEAR+"/"+CURRENT_SEASON+"/"

list_of_departments = get_values_from_list_of_dict(get_data_from_url(SFU_DATA_WEBSITE), "text", "dept")

