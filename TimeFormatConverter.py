class TimeFormatConverter:

    @staticmethod
    def get_time_format(time, time_format):
        if time_format == "standard":
            if time >= 12:
                am_or_pm = "PM"
                if time > 12:
                    time -= 12
            else:
                am_or_pm = "AM"
            return str(time) + ":00 " + am_or_pm
        if time_format == "military":
            return str(time) + ":00"
        return "INVALID PARAMETER, PLEASE SET TIME FORMAT AS 'standard' OR 'military'"


days_to_int = {"0": "Sunday", "1": "Monday", "2": "Tuesday", "3": "Wednesday", "4": "Thursday", "5": "Friday",
               "6": "Saturday"}

days_of_week = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

available_time = [
    "1:00",
    "2:00",
    "3:00",
    "4:00",
    "5:00",
    "6:00",
    "7:00",
    "8:00",
    "9:00",
    "10:00",
    "11:00",
    "12:00"
]

am_pm = ["AM", "PM"]


def time_to_int(time):
    return (int)(time.split(":")[0])


def get_int_from_days(day):
    for key, value in days_to_int.items():
        if day == value:
            return int(key)
    return "NONEXISTENT KEY"
