#Hotel Class
from room import Room
from availability import roomType

class Hotel:
    def __init__(self, name, nSRooms, nDRooms, nERooms, n):

        try:
            self.name = name
            if int(nSRooms + nDRooms + nERooms) > 0:
                self.nSRooms = nSRooms
                self.nDRooms = nDRooms
                self.nERooms = nERooms
            else:
                print('Hotel must have more than 1 room!, defaulting to 1 standard room..')
                self.nSRooms = 1
                self.nDRooms = 0
                self.nERooms = 0
        except ValueError:
            print('Invalid Data Type, defaulting to 1 standard room')
            self.nSRooms = 1
            self.nDRooms = 0
            self.nERooms = 0         
        
        self.totalRooms = self.nSRooms + self.nDRooms + self.nERooms
        self.roomsData = {}
        self.roomsData['Room'] = []
        self.fullyBooked = 0
        for i in range(self.nSRooms):
            r = Room(roomType.STANDARD, n)
            self.roomsData['Room'].append(r)
        for i in range(self.nDRooms):
            r = Room(roomType.DELUXE, n)
            self.roomsData['Room'].append(r)
        for i in range(self.nERooms):
            r = Room(roomType.EXECUTIVE, n)
            self.roomsData['Room'].append(r)
            
    def checkIfHotelBooked(self, chkInDate, chkOutDate):
        numBooked = 0
        for i in range(len(self.roomsData['Room'])):
            (a, b) = self.roomsData['Room'][i].checkReservationDates(chkInDate,chkOutDate)
            if b == Room.reservedStatus['2']:
                numBooked += 1
            else:
                print('Room #:', self.roomsData['ID'][i], 'is available for your chosen dates')
        if numBooked == self.totalRooms:
            self.fullyBooked = 1
        else:
            self.fullyBooked = 0
        return self.fullyBooked
    def returnRoomsData(self):
        return self.roomsData
    def returnName(self):
        return self.name