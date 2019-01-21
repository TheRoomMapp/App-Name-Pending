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
   
def create_new_ldict(old_ldict, old_key, new_key):
    '''
    Function to build upon existing list of dictionary (eg. adds course numbers to ldict_dept, adds sections to ldict_dept_course)
    Note: does not work for coure schedule because json from these sites are not lists of dictionaries
    @param old_ldict - current list of dictionary to be built upon
    @param old_key - key in SFU's json corresponding to value of interest
    @param new_key - key name chosen to correspond with value in new dictionaries
    '''
    new_ldict = []
    webname_exceptions =[]
    for dictionary in old_ldict:
        webname = SFU_DATA_WEBSITE
        for key in dictionary:
            webname += dictionary[key] +'/'
        if url_is_alive(webname):
            unrefined_ldict = get_data_from_url(webname)
            for item in unrefined_ldict:
                new_dict = {}
                new_dict.update(dictionary)
                new_dict[new_key] = item[old_key]
                new_ldict.append(new_dict)
        else: webname_exceptions.append(webname)
    print("URL's causing error:", webname_exceptions)
    return new_ldict

import urllib.request
import json
import time

#Top Level Variables
CURRENT_YEAR = "2019"
CURRENT_SEASON = "spring"
SFU_DATA_WEBSITE = "http://www.sfu.ca/bin/wcm/course-outlines?"+CURRENT_YEAR+"/"+CURRENT_SEASON+"/"

start = time.time()

print("Pulling departments")
ldict_dept = create_new_ldict([{}], 'text', 'department')

print("Pulling course numbers")
ldict_dept_course = create_new_ldict(ldict_dept, 'text', 'course')

print("Pulling section numbers")
ldict_dept_course_sect = create_new_ldict(ldict_dept_course, 'text', 'section')

print("Pulling Course Schedules")
ldict_sched = []
schedule_exceptions = []
for dictionary in ldict_dept_course_sect:
    webname = SFU_DATA_WEBSITE
    for key in dictionary:
        webname += dictionary[key] +'/'
    if url_is_alive(webname):
        unrefined_dict = get_data_from_url(webname)
        try:
            ldict_sched += unrefined_dict['courseSchedule']
        except KeyError:
            schedule_exceptions.append(webname)
print("URL's causing course schedule errors:", schedule_exceptions) 

end = time.time()
print("epoch time:",start,"-",end)
