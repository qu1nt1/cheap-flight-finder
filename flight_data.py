from datetime import datetime

class FlightData:
    date: str

    # GETTING THE DATE
    def __init__(self):
        self.date = datetime.today().strftime("%d/%m/%Y")

    # GETTING THE NEXT 6 MONTHS DATE

    def next_six_months_date(self):
        day_list = self.date.split("/")

        if int(day_list[1]) + 6 > 12:
            date_to = (day_list[0] + "/0" + str(int(day_list[1]) - 6) + "/" + str(int(day_list[2]) + 1))
        else:
            date_to = (day_list[0] + "/" + str(int(day_list[1]) + 6) + "/" + day_list[2])

        return date_to
