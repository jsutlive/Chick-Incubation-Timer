class HamburgerHamilton:

    @staticmethod
    def get_time_from_stage(incubation_hours):
        if incubation_hours == 1:
            return 0
        elif incubation_hours == 2:
            return 6
        elif incubation_hours == 3:
            return 12
        elif incubation_hours == 4:
            return 18
        elif incubation_hours == 5:
            return 22
        elif incubation_hours == 6:
            return 23
        elif incubation_hours == 7:
            return 26
        elif incubation_hours == 8:
            return 27
        elif incubation_hours == 9:
            return 29
        elif incubation_hours == 10:
            return 33
        elif incubation_hours == 11:
            return 40
        elif incubation_hours == 12:
            return 45
        elif incubation_hours == 13:
            return 50
        elif incubation_hours == 14:
            return 53
        elif incubation_hours == 15:
            return 55
        else:
            return -1
