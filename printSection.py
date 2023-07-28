def printSection(section):
    meetTime = section['meetingsFaculty'][0]['meetingTime']
    meetTimeStr = (
        f'{milToAMPM(meetTime["beginTime"])}'
        ' to '
        f'{milToAMPM(meetTime["endTime"])}'
    )
    
    cols = (
        f"{section['subjectCourse']}   ",
        section["courseReferenceNumber"],
        section["faculty"][0]["displayName"],
        daysOfWeekFixedWidth(section),
        meetTimeStr
    )

    print("\t".join(cols))
    #subjectCourse
    #CRN
    #faculty['displayName']
    #days of week
    #time



def milToAMPM(time):
    minutes = time[-2:]
    hours = time[:-2]

    hoursInt = int(hours)
    if hoursInt == 0:
        return f"12:{minutes} AM"
    elif hoursInt > 12:
        return f"{hoursInt-12}:{minutes} PM"
    else:
        return f"{hours}:{minutes} AM"

def daysOfWeekFixedWidth(section):
    shortstr = ""
    weekdays = (
        ("M","monday"),
        ("T","tuesday"),
        ("W","wednesday"),
        ("R","thursday"),
        ("F","friday"),
    )

    for (abbr,day) in weekdays:
        if section["meetingsFaculty"][0]["meetingTime"][day]:
            shortstr+=abbr
        else:
            shortstr+= "-"
    return shortstr
    
def fixedWidth(string,n):
    if len(string) > n:
        return string[0:n-1]+"-"
    else:
        return string+(" "*(n-len(str)))