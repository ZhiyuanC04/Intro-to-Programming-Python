# This is Zhiyuan Chang's work
# Computing ID: vgs3qt

def fine(speed_limit, my_speed, zone="none"):
    """
    :param speed_limit:  a number that indicates the posted speed limit.
    :param my_speed: a number that indicates the speed that the individual was actually traveling at.
    :param zone: an optional string that indicates what zone the individual is driving in.
    :return: the fine that the individual will be ticketed with.
    """
    overspeed = int(my_speed) - int(speed_limit)
    if my_speed > speed_limit:
        if overspeed >= 20:
            return 350
        elif zone == "school" or zone == "work":
            return overspeed * 7
        elif zone == "residential":
            return (overspeed * 8) + 200
        elif zone == "none":
            return overspeed * 6
    elif int(speed_limit) - int(my_speed) > 10:
        return 30
    else:
        return 0


def demerits(speed_limit, my_speed):
    """
    :param speed_limit: a number that indicates the speed limit that should be driven.
    :param my_speed: a number that indicates the speed that the individual was actually traveling at.
    :return: the number of demerit points earned.
    """
    overspeed = int(my_speed) - int(speed_limit)
    if 1 <= overspeed <= 9:
        return 3
    if 10 <= overspeed <= 19:
        return 4
    if overspeed >= 20:
        return 6
    else:
        return 0
