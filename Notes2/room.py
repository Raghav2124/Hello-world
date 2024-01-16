# Room Class
from datetime import *
from availability import roomReservationStatus, roomType
class book:
    
    def __init__(self, n):
        
        if n > 0:
            self.nDays = int(n)
        else:
            print('Calendar must look ahead more than 1 day!, defaulting to 1 day')
            self.nDays = 1
        self.bookingDays = []
        startDate = date.today()
        self.bookingDate = startDate.strftime('%Y-%m-%d')
        endDate = startDate + timedelta(days = self.nDays)
        self.finalDate = endDate.strftime('%Y-%m-%d')
        for i in range(n + 1):
            day = startDate + timedelta(days = i)
            #since nobody is initially booked, append 'none' to each day
            x = list((day, 'none'))
            self.bookingDays.append(x)

    def returnAllbookingDays(self):
        return self.bookingDays 

    def returnAvailableDateRange(self):
        return self.bookingDate, self.finalDate
    
class Room(book):
    
    reservedStatus = {}
    reservedStatus['1'] = roomReservationStatus.AVAILABLE
    reservedStatus['2'] = roomReservationStatus.RESERVED
    
    def __init__(self, suite, n):
        
        self.suiteType = suite
        self.status = Room.reservedStatus['1']
        self.rFlag = False
        self.rangeStart = None
        self.rangeEnd = None
        self.bookFlag = False
        if self.suiteType == roomType.STANDARD:
            self.price = 100
        elif self.suiteType == roomType.DELUXE:
            self.price = 200
        elif self.suiteType == roomType.EXECUTIVE:
            self.price = 300


    def returnRoomCalendar(self):
        return self.roomCal.returnAllbookingDays()
    
    def returnRoomPrice(self):
        return self.price
    

    def checkReservationDates(self, chkInDate, chkOutDate):
        self.rFlag = False
        self.rangeStart = None
        self.rangeEnd = None
        datesOnly = [date[0] for date in self.returnAllbookingDays()]
        for i in range (len(datesOnly)):
            if datesOnly[i] == chkInDate:
                self.rangeStart = i
            elif datesOnly[i] == chkOutDate:
                self.rangeEnd = i
        if (self.rangeStart and self.rangeEnd)!=None:
            idOnly = [days[1] for days in self.returnAllbookingDays[self.rangeStart:self.rangeEnd]]
            result = all(elem == 'none' for elem in idOnly)
            if result:
                self.status = Room.reservedStatus['1']  
                self.rFlag = True
            else:
                self.status = Room.reservedStatus['2']
                self.rFlag = False
        else:
            print('Dates out of range or invalid values')
            self.rFlag = False
        return self.rFlag, self.status
    
    def cancelBookingByID(self, ID):
        for i in range(0, len(self.returnAllbookingDays())):
            if self.returnAllbookingDays[i][1] == ID:
                self.returnAllbookingDays[i][1] = 'none'
    