def secsToTime(secs):
    smallUnits = ("s", "ms", "us", "ns", "ps")
    bigUnits = ("s", "m", "h", "d", "y")
    bigUnitsConverters = (1, 60, 60, 24, 365)
    assert(secs>=0)
    
    i=0
    if secs<1:
        while secs<1:
            secs *=1000
            i+=1
        else:
            units = smallUnits[i]
    else:
        while secs /bigUnitsConverters[i] >1:
            secs /=bigUnitsConverters[i]
            i+=1
        else:
            units = bigUnits[i]
    
    return ("%.2f%s" % (secs,units))

while s = input("please enter a time")