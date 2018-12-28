#Function to pull data from a URL/API/website address
#@param url - takes a url/api/website address
#@returns - the data that was provided by url (note: SFU returns 'byte-type' data)
def read_webpage_and_get_data(url):
   page = urllib.request.urlopen(url)
   res = page.read()
   return res

#Function to turn 'byte'-type data from a URL/API/website address into a list
#@param bytesItem - takes a 'byte-type' item (likely from somewhere else like a webpage)
#@returns - a string list of the 'byte-type' items entered
def convert_bytes_to_list(bytesItem):
   stringItem = str(bytesItem)
   string_of_all_items = ""
   for char in stringItem:
       if char=="{":
           string_of_all_items+=""
       elif char=="}":
           string_of_all_items+="new_item"
       else: string_of_all_items+=char
   stringList = string_of_all_items[3:-2]
   ##print("TRACE: strDepart is", stringList)
   list_of_string_items_separated_by_department = stringList.split("new_item,")
   for i in range(len(list_of_string_items_separated_by_department)):
       newElmt = list_of_string_items_separated_by_department[i].split(",")
       list_of_string_items_separated_by_department[i] = newElmt
   ##print("TRACE: _lstDepart is", list_of_string_items_separated_by_department)
   return list_of_string_items_separated_by_department

#Function to extract required information (eg. department name, course numbers, etc.) from a larger string in a list of lists
#@param lst - takes a list of strings
#@param pointer - word before the word we're looking for. For example, in the department data list, the pointer is "text"
#@returns - a single list of required information in each position

def convert_list_of_list_to_single_list(lst,pointer): 
   newList=[]
   for sublist in lst:
       for st in sublist:
           if pointer in st:
               startPos=st.find(pointer)+len(pointer)+3
               newList.append(st[startPos:-1])
   return newList

#Function to create a list of course numbers
#@param lst - takes a list of departments
#@returns - a list of course numbers
def create_list_of_course_numbers(lst):
   list_of_course_numbers = [] ##[[dept code, [course numbers]]]
   for item in lst:
       list_of_sub_course_numbers = [item]
       webName = SFU_DATA_WEBSITE + item
       #print("TRACE: webName is", webName)
       if urlIsAlive(webName):
           unrefined = convert_bytes_to_list(read_webpage_and_get_data(webName))
           list_of_sub_course_numbers.append(convert_list_of_list_to_single_list(unrefined, "text"))
           #print("TRACE list_of_sub_course_numbers is", list_of_sub_course_numbers)
           list_of_course_numbers.append(list_of_sub_course_numbers)
   return list_of_course_numbers

#Function to create a list of section numbers
#@param lst - takes a list of course numbers
#returns - a list of section numbers
def create_list_of_section_numbers(lst):
   list_of_section_numbers = [] ##[[dept code, [course numbers, [section numbers]]]]
   department_code = ""
   course_number = ""
   for item in lst:
       temp_list_section_numbers = [] ##[dept code, [course numbers, [section numbers]]]
       #print("TRACE temp_list_section_numbers is", temp_list_section_numbers)
       for i in range(len(item[1])):
           department_code = item[0]
           course_number = item[1][i]
           webName = SFU_DATA_WEBSITE + department_code + "/" + course_number
           #print("TRACE webName is:", webName)
           if urlIsAlive(webName):
               unrefined = convert_bytes_to_list(read_webpage_and_get_data(webName))
               #print(unrefined[0])
               temp_list_section_numbers = convert_list_of_list_to_single_list(unrefined,"text") ##change this so it inserts [section numbers] into the [course numbers] beside the course number corresponding to the section
               ##temp_list_section_numbers.insert(i+1, convert_list_of_list_to_single_list(unrefined, "text")) ##change this so it inserts [section numbers] into the [course numbers] beside the course number corresponding to the section
               ##When I make this list_of_subsection_numbers[0][1].insert(i+1, convert_list_of_list_to_single_list(unrefined, "text")), "webName = SFU_DATA_WEBSITE + item[0] + "/" + item[1][i]" returns error.. why
               list_of_section_numbers.append([department_code+course_number,temp_list_section_numbers])
   return list_of_section_numbers

def urlIsAlive(url):
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

def read_csv_into_list_of_lists(IN_file):
   '''
   PROVIDED. CMPT 120
   A csv file should be available in the folder (where this program is)
   A string with the name of the file should be passed as argument to this function
   when invoking it
   (the string would include the csv extension, e.g "ID_data.csv")
   '''

   import csv

   lall = []

   print("\n.... TRACE - data read from the file\n")
   with open(IN_file) as csv_file:
       csv_reader = csv.reader(csv_file, delimiter=',')

       for inrow in csv_reader:
           print(".......",inrow)
           lall.append(inrow)
   return lall

def write_list_of_output_lines_to_file(lout,file_name):
   '''
   PROVIDED. CMPT 120
   Assumptions:
   1) lout is the list containing all the lines to be saved in the output file
   2) file_name is the parameter receiving a string with the exact name of the output file
      (with the csv extension, e.g "OUT_results.csv")
   3) after executing this function the output file will be in the same
      directory (folder) as this program
   4) the output file contains just text representing one draw data per line
   5) after each line in the file  there is the character "\n"
      so that the next draw is in the next line, and also
      there is (one single) "\n" character after the last line
   6) after the output file was created you should be able to open it
      with Excell as well
   '''
  
   fileRef = open(file_name,"w") # opening file to be written
   for line in lout:
       fileRef.write(line)
                                  
   fileRef.close() 
   return


import csv
import urllib.request

#Top Level Variables
CURRENT_YEAR = "2018"
CURRENT_SEASON = "fall"
SFU_DATA_WEBSITE = "http://www.sfu.ca/bin/wcm/course-outlines?"+CURRENT_YEAR+"/"+CURRENT_SEASON+"/"

departments_in_bytes_form = read_webpage_and_get_data(SFU_DATA_WEBSITE)

list_of_list_of_departments=convert_bytes_to_list(departments_in_bytes_form)
list_of_departments=convert_list_of_list_to_single_list(list_of_list_of_departments,"text")
list_of_courses=create_list_of_course_numbers(list_of_departments)
list_of_sections=create_list_of_section_numbers(list_of_courses)
final_list_for_export = []
list_for_dictionary_key = []
list_for_dictionary_value = []
for c in range(len(list_of_sections)):
   for d in range(len(list_of_sections[c][1])):
       final_list_for_export.append(list_of_sections[c][0]+","+list_of_sections[c][1][d]+"\n")
       list_for_dictionary_key.append(list_of_sections[c][0]+"-"+list_of_sections[c][1][d])
       #print(final_list_for_export)
write_list_of_output_lines_to_file(final_list_for_export,"list_of_everything.csv")
#dictionary_of_courses = {k:v for k,v in zip(list_for_dictionary_key,list_for_dictionary_value)}




        
        






    
    
    
    
    


