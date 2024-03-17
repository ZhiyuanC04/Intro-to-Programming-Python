# Computing ID: vgs3qt
# Name: Zhiyuan Chang

def quad(x , y):
    """
    :param x: the x coordinate
    :param y: the y coordinate
    :return: the quadrant the point lies. (0 means on axis)
    """
    if x == 0 or y == 0:
        return 0
    elif x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
