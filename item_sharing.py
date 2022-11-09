from contract import SmartContract, BookingDetails
class Item:
    def __init__(self, item_info, **kwargs):
        self.item_info = item_info
        self.additional = kwargs
        self.is_rented = False
        self.allowed_to_use = False

    def access(self):
        print("item have been accessed")
        self.is_rented = True

    def end_rental(self):
        self.is_rented = False

    def allow_to_use(self):
        self.allowed_to_use = True
class Owner:
    def __init__(self, balance):
        self.contract = SmartContract
        self.balance = balance

    def add_item_to_rent(self, day_price, item_info):
        item = Item(item_info)
        self.contract.add_booking_details(BookingDetails(item, day_price))

    def deploy(self, ether, blockchain):
        self.balance -= ether
        self.contract = SmartContract()
        self.contract.owner_deposit(ether)
        blockchain.add_new_transaction(self.contract)

    def withdraw_earnings(self):
        self.balance += self.contract.withdraw_earnings()

    def allow_item_usage(self):
        self.contract.allow_item_usage()

    def encrypt_and_store_details(self, blockchain):
        blockchain.mine()

class Customer:
    def __init__(self, balance):
        self.balance = balance
        self.contract = SmartContract

    def request_book(self, ether, blockchain):
        self.contract = blockchain.get_unconfirmed_transactions()[0]
        self.contract.client_deposit(ether)
        self.balance -= ether

    def pass_number_of_days(self, days_no):
        self.contract.get_booking_details().request(days_no)

    def retrieve_balance(self):
        self.balance += self.contract.retrieve_balance()

    def end_item_rental(self):
        self.contract.end_item_rental()

    def access_item(self):
        self.contract.get_item().access()








