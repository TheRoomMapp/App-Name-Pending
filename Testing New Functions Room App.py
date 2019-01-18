#Testing New Room App Functions


def all_considered_rooms(biglist):
    room_dict={}
    for dic in biglist:
        for indict in dic['schedule']:
            if 'buildingCode' in indict:
                if indict['buildingCode'] not in room_dict:
                    room_dict[indict['buildingCode']]=[]
            if 'roomNumber' in indict:
                if indict['roomNumber'] not in room_dict[indict['buildingCode']]:
                    room_dict[indict['buildingCode']].append(indict['roomNumber'])
    return room_dict
                
    

def bookings_by_day(two_letter_weekday, biglist):
    lstarttimes=['8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00',
            '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30']
    lendtimes=['8:20', '8:50', '9:20', '9:50', '10:20', '10:50', '11:20', '11:50', '12:20', '12:50', '13:20', '13:50', '14:20',
               '14:50', '15:20', '15:50', '16:20', '16:50', '17:20', '17:50', '18:20', '18:50', '19:20', '19:50', '20:20']
    dfull_by_time={'8:30':[], '9:00': [], '9:30': [], '10:00': [], '10:30': [], '11:00': [], '11:30': [], '12:00': [],
                   '12:30': [], '13:00': [], '13:30': [], '14:00': [], '14:30': [], '15:00': [], '15:30': [], '16:00': [],
                   '16:30': [], '17:00': [], '17:30': [], '18:00': [], '18:30': [], '19:00': [], '19:30': [], '20:00': []}
    for dic in biglist:
        for indict in dic['schedule']:
            if indict['days']==two_letter_weekday:
                startfound="nah"
                endfound="nope"
                check=0
                while startfound=="nah" and check<len(lstarttimes):
                    if indict['startTime']==lstarttimes[check]:
                        startfound=lstarttimes[check]
                    else: check+=1
                checkend=0
                while endfound=="nope" and checkend<len(lendtimes):
                    if indict['endTime']==lendtimes[checkend]:
                        endfound=lendtimes[checkend]
                        for index in range(check, checkend):
                             dfull_by_time[lstarttimes[index]].append(indict['buildingCode']+" "+indict['roomNumber'])
                    checkend+=1
    return dfull_by_time 

testlist=[{'department': 'ACMA', 'course': '210', 'section': 'D100', 'schedule': [{'startTime': '10:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '1014', 'days': 'Tu', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'LEC', 'endTime': '11:20', 'isExam': False, 'buildingCode': 'SECB', 'campus': 'Burnaby'}, {'startTime': '9:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '1012', 'days': 'Th', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'LEC', 'endTime': '11:20', 'isExam': False, 'buildingCode': 'SECB', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '210', 'section': 'D101', 'schedule': [{'startTime': '9:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '8500', 'days': 'Fr', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'TUT', 'endTime': '10:20', 'isExam': False, 'buildingCode': 'TASC2', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '210', 'section': 'D102', 'schedule': [{'startTime': '10:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '7100', 'days': 'Fr', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'TUT', 'endTime': '11:20', 'isExam': False, 'buildingCode': 'RCB', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '336', 'section': 'D100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '336', 'section': 'D200', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '336', 'section': 'I100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '337', 'section': 'D100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '337', 'section': 'D200', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '337', 'section': 'I100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '355', 'section': 'D100', 'schedule': [{'startTime': '14:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '3531', 'days': 'Mo', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'LEC', 'endTime': '16:20', 'isExam': False, 'buildingCode': 'WMC', 'campus': 'Burnaby'}, {'startTime': '14:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '2268', 'days': 'We', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'LEC', 'endTime': '15:20', 'isExam': False, 'buildingCode': 'WMC', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '355', 'section': 'D101', 'schedule': [{'startTime': '9:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '2122', 'days': 'Fr', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'TUT', 'endTime': '10:20', 'isExam': False, 'buildingCode': 'AQ', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '425', 'section': 'D100', 'schedule': [{'startTime': '11:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '5009', 'days': 'We', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'LEC', 'endTime': '12:20', 'isExam': False, 'buildingCode': 'AQ', 'campus': 'Burnaby'}, {'startTime': '10:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '5009', 'days': 'Fr', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'LEC', 'endTime': '12:20', 'isExam': False, 'buildingCode': 'AQ', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '425', 'section': 'D101', 'schedule': [{'startTime': '12:30', 'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'roomNumber': '2122', 'days': 'Mo', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'TUT', 'endTime': '13:20', 'isExam': False, 'buildingCode': 'AQ', 'campus': 'Burnaby'}]}, {'department': 'ACMA', 'course': '436', 'section': 'D100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '436', 'section': 'D200', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '436', 'section': 'I100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}, {'department': 'ACMA', 'course': '437', 'section': 'D100', 'schedule': [{'startDate': 'Tue Sep 04 00:00:00 PDT 2018', 'days': '', 'endDate': 'Mon Dec 03 00:00:00 PST 2018', 'sectionCode': 'PRA', 'isExam': False}]}]

daylist=bookings_by_day('Fr', testlist)
print(daylist)

