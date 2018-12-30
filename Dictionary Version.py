def get_data_from_url(url):
    '''
    Gets json from url, decodes json, and returns data
    '''
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    return data

def url_is_alive(url):
   """
   Checks that a given URL is reachable.
   """
   request = urllib.request.Request(url)
   request.get_method = lambda: 'HEAD'

   try:
       urllib.request.urlopen(request)
       return True
   except urllib.request.HTTPError:
       return False

def get_values_from_ldict(unrefined_ldict, old_key, current_dict, new_key):
    '''
    Function to extract required values from an unrefined list of dictionaries and adds them to an existing dictionary
    @param unrefined_ldict - list of dictionaries to extract from
    @param old_key - key in ldict corresponding to value of interest
    @current_dict - dictionary the new_key:value will be added to
    @new_key - key name chosen to correspond with value in new dictionary
    '''
    new_ldict = []
    for item in unrefined_ldict:
        new_dict = {}
        new_dict.update(current_dict)
        new_dict[new_key] = item[old_key]
        new_ldict.append(new_dict)
    return new_ldict
        

import urllib.request
import json

#Top Level Variables
CURRENT_YEAR = "2018"
CURRENT_SEASON = "fall"
SFU_DATA_WEBSITE = "http://www.sfu.ca/bin/wcm/course-outlines?"+CURRENT_YEAR+"/"+CURRENT_SEASON+"/"

ldict_dept = get_values_from_ldict(get_data_from_url(SFU_DATA_WEBSITE), "text", {}, "department")

ldict_dept_course = []
for dictionary in ldict_dept:
    webname = SFU_DATA_WEBSITE + dictionary['department'] + '/'
    if url_is_alive(webname):
        unrefined_list = get_data_from_url(webname)
        ldict_dept_course += get_values_from_ldict(unrefined_list, 'text', dictionary, 'course')

    
    
