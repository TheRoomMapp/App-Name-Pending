def readWebpage(url):
    page = urllib.request.urlopen(url)
    res = page.read()
    return res

def bytesToList(bytesItem):
    strItem = str(bytesItem)
    strList = ""
    for char in strItem:
        if char=="{":
            strList+=""
        elif char=="}":
            strList+="new_item"
        else: strList+=char        
    strList = strList[3:-2]
    ##print("TRACE: strDepart is", strList)
    lstList = strList.split("new_item,")
    for i in range(len(lstList)):
        newElmt = lstList[i].split(",")
        lstList[i] = newElmt
    ##print("TRACE: _lstDepart is", lstList)
    return lstList

def listOfNeeds(lst,pointer): #pointer is the word before the word we're looking for. For example, in the department data list, the pointer is "text"
    newList=[]
    for sublist in lst:
        for st in sublist:
            if pointer in st:
                startPos=st.find(pointer)+len(pointer)+3
                newList.append(st[startPos:-1])
    return newList

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
        return False ##save exceptions to a list so we can test the errors.
        
import urllib.request

bytesDepart = readWebpage("http://www.sfu.ca/bin/wcm/course-outlines?2018/fall")
lolDepart=bytesToList(bytesDepart)
lDepart=listOfNeeds(lolDepart,"text")
print(lDepart)

lCourseNum = [] ##[[dept code, [course numbers]]]
for item in lDepart:
    lSubCourseNum = [item]
    webName = 'http://www.sfu.ca/bin/wcm/course-outlines?2018/fall/' + item ##Eventually change this so year and season are not hard-coded
    print("TRACE: webName is", webName)
    if urlIsAlive(webName) == True:
        unrefined = bytesToList(readWebpage(webName))
        lSubCourseNum.append(listOfNeeds(unrefined, "text"))
        print("TRACE lSubCourseNum is", lSubCourseNum)
        lCourseNum.append(lSubCourseNum)

lSectionNum = [] ##[[dept code, [course numbers], [section numbers]]]
for item in lCourseNum:
    lSubSectionNum.append(item) ## item = [dept code, [course numbers]]
    for i in range(len(item[1])):
        webName = 'http://www.sfu.ca/bin/wcm/course-outlines?2018/fall/' + item[0] + item[1][i]
        if urlIsAlive(webName) == True:
            unrefined = bytesToList(readWebpage(webName))
            lSubSectionNum.append(listOfNeeds(unrefined, "text"))
            print("TRACE lSubSectionNum is", lSubSectionNum)
            lSectionNum.append(lSubCourseNum)
        
        






    
    
    
    
    


