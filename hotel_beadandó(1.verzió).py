from datetime import datetime

class room:
    def __init__(self, roomnumber, price):
        self.roomnumber = roomnumber
        self.price = price

class onebedroom(room):
    def __init__(self, roomnumber):
        super().__init__(roomnumber, 5000)  

class twobedroom(room):
    def __init__(self, roomnumber):
        super().__init__(roomnumber, 8000) 

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.room.append(room)

class reserve:
    def __init__(self, room, date):
        self.room = room
        self.date = date

class ReserveHandler:
    def __init__(self, hotel):
        self.hotel = hotel
        self.reserves = []

    def reserve(self, roomnumber, date):
        for room in self.hotel.rooms:
            if room.roomnumber == roomnumber:
                reserve = reserve(room, date)
                self.reserves.append(reserve)
                return room.price
        return None

    def unreserve(self, roomnumber, date):
        for reserve in self.reserve:
            if reserve.room.roomnumber == roomnumber and reserve.date == date:
                self.reserves.remove(reserve)
                return True
        return False

    def list(self):
        for reserve in self.reserves:
            print(f"Szoba: {reserve.szoba.szobaszam}, Dátum: {reserve.datum}")

def fill_system(hotel):
    hotel.add_room(onebedroom("1"))
    hotel.add_room(onebedroom("2"))
    hotel.add_room(twobedroom("3"))
    hotel.add_room(twobedroom("6"))
    hotel.add_room(twobedroom("7"))

    reserve_handler = ReserveHandler(hotel)
    reserve_handler.reserve("1", datetime(2024, 5, 10))
    reserve_handler.reserve("2", datetime(2024, 5, 12))
    reserve_handler.reserve("3", datetime(2024, 5, 15))

if __name__ == "__main__":
    hotel = Hotel("Példa Szálloda")
    fill_system(hotel)
    reserve_handler = ReserveHandler(hotel)

    while True:
        print(f"\nVálassz az alábbiak közül:\n1. Foglalás\n2. Lemondás\n3. Foglalások listázása\n0. Kilépés")

        inp = input("Választásod: ")

        if inp == "1":
            roomnumber = input("Add meg a szoba számát: ")
            date_raw = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            date = datetime.strptime(date_raw, "%Y-%m-%d")
            price = reserve_handler.foglalas(roomnumber, date)
            if price is not None:
                print(f"Sikeres foglalás! Ár: {price}")
            else:
                print("A foglalás sikertelen.")
        elif inp == "2":
            roomnumber = input("Add meg a szoba számát: ")
            date_raw = input("Add meg a foglalás dátumát (YYYY-MM-DD formátumban): ")
            date = datetime.strptime(date_raw, "%Y-%m-%d")
            if reserve_handler.unreserve(roomnumber, date):
                print("A foglalás sikeresen törölve.")
            else:
                print("Nem sikerült törölni a foglalást.")
        elif inp == "3":
            print("Összes foglalás:")
            reserve_handler.reserve()
        elif inp == "0":
            print("Kilépés")
            break
        else:
            print("Érvénytelen választás.")