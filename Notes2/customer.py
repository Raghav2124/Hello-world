#Customer Class
from datetime import date
import random
class Customer:
    def __init__(self, fname, lname, numGuests, number):
        try:
            self.fname = fname
            self.lname = lname
            self.numGuests =numGuests
            self.number = number
        except(NameError, ValueError):
            print('Invalid Input(s), try again')
        
        self.roomAssignment = []
        self.totalCharge = 0
        self.chkInDate = None
        self.chkOutDate = None
        self.durDays = 0
        self.reservationID = random.sample(range(100),1)
    
    def assignCustomerDates(self, chkInDate, chkOutDate):
        self.chkInDate = date(chkInDate[0], chkInDate[1], chkInDate[2])
        self.chkOutDate = date(chkOutDate[0], chkOutDate[1], chkOutDate[2])
        self.durDays = (self.chkOutDate - self.chkInDate).days
        if self.durDays <= 0:
            print('Check in date must be before check out date!')
    
    def assignCustomerRoom(self, roomSel):
        self.roomAssignment.append(str(roomSel))
        
    def resetCustomerData(self):
        self.roomAssignment = []
        self.chkInDate = None
        self.chkOutDate = None
        self.reservationID = None
    
    def chargeCustomer(self, amount):
        self.totalCharge+=amount
    
    def refundCustomer(self, amount):
        self.totalCharge -= amount
        if self.totalCharge <= 0:
            self.totalCharge = 0
            print('Fully refunded: $', amount)

    def returnCustomerDetails(self):
        return self.fname, self.lname, self.numGuests, self.number

    def returnCustomerRooms(self):
        return self.roomAssignment
    
    def returnCustomerCharge(self):
        return self.totalCharge
    
    def returnReservationID(self):
        return self.reservationID
    
    def returnCustomerDates(self):
        return self.chkInDate, self.chkOutDate
    
    def returnCustomerDays(self):
        return self.durDays
