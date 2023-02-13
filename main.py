import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, cust_name, hotel_object):
        self.cust_name = cust_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are your reservation details:
        Name: {self.cust_name}
        Hotel: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in df_cards:
            return True


print(df)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = CreditCard(number="1234")
    if credit_card.validate(expiration="12/26",
                            holder="JOHN SMITH", cvc="123"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(cust_name=name, hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("Invalid card details")
else:
    print("Sorry. Hotel currently unavailable")
