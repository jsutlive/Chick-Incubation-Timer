class ChickIncubationTimer:

    #def __init__(self):
     #   self.hh_stages = new

    @staticmethod
    def calculate_ending_hour(starting_hour, time_required):
        return (starting_hour + time_required) % 24

    @staticmethod
    def calculate_ending_day(starting_day, starting_hour, ending_hour, time_required):
        full_days = int(time_required / 24)
        starting_day = starting_day + full_days
        if starting_hour > ending_hour:
            starting_day += 1
        return starting_day % 7


class HHStage:
    def __init__(self, hasRange, start, end):
        self.hasRange = hasRange
        if(hasRange):
            self.end = end
        self.start = start

