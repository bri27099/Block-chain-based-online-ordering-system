from datetime import datetime

class SmartContract:
    idCounter = 1

    def __init__(self):
        self.id = SmartContract.idCounter
        SmartContract.idCounter += 1
        self.client_balance = 0
        self.owner_balance = 0
        self.booking_details = BookingDetails

    def retrieve_balance(self):
        return self.client_balance 

    def withdraw_earnings(self):
        return self.owner_balance

    def client_deposit(self, ether):
        self.client_balance += ether

    def owner_deposit(self, ether):
        self.owner_balance += ether

    def allow_item_usage(self):
        self.booking_details.get_item().allow_to_use()

    def add_booking_details(self, booking_details):
        self.booking_details = booking_details

    def get_booking_details(self):
        return self.booking_details

    def end_item_rental(self):
        self.booking_details.get_item().end_rental()
        self.client_balance -= self.booking_details.get_summed_cost()
        self.owner_balance += self.booking_details.get_summed_cost()
    
    def get_item(self):
        return self.booking_details.get_item()


class BookingDetails:
    def __init__(self, item, price_per_day):
        self.item = item
        self.price_per_day = price_per_day
        self.no_of_days = 0
        self.rental_date = datetime.now()

    def request(self, no_of_days):
        self.no_of_days = no_of_days

    def get_summed_cost(self):
        return self.price_per_day * self.no_of_days

    def get_item(self):
        return self.item


