# This is Zhiyuan Chang's work, my computing id is: vgs3qt

def gellish2(age):
    a = 191.5 - (0.007 * age ** 2)
    a = float(a)
    return a

def in_target_range(hr, age):
    a = gellish2(age)
    b = a * 0.65 <= hr <= a * 0.85
    return b