class Book():

    def make_booking(self, **ssmbg):
        raise NotImplementedError

class Air(Book):
    BUS_CLASS = 'Business Class'
    FIRST_CLASS = 'First Class'
    ECO_CLASS = 'Regular Economy class'
    PREMIUM_EC_CLASS = 'Premium Economy'

    def __init__(self, air_name):
        super(Air, self).__init__()
        self.air_name = air_name
        self.seats = {
            self.BUS_CLASS: 25,
            self.FIRST_CLASS: 25,
            self.ECO_CLASS: 50,
            self.PREMIUM_EC_CLASS: 60,
        }

        self.prices = {
            self.BUS_CLASS: 1500,
            self.FIRST_CLASS: 1000,
            self.ECO_CLASS: 500,
            self.PREMIUM_EC_CLASS: 1100,
        }

    def is_avail(self, booking_class):
        return self.seats[booking_class] > 0

    def make_res(self, booking_class):
        if self.is_aval(booking_class):
            self.seats[booking_class] -= 1

    def show(self, booking_class):
        print("seats available:", self.seats[booking_class])
        print("prices:", self.prices[booking_class])


airline = Air("Emirites")
Seat = input("Enter your preference: \n Business Class \n Regular Economy Class \n First Class \n Premium Economy\n ")
booking_class = str(Seat)
airline.show(booking_class)