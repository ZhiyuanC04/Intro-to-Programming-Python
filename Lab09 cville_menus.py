

menu = {"rice": 1, "noodles": 2, "apple": 3}
all_cville_restaurants = {}

def cville_menus(name, price, menu = menu):
    menu[name] = price
    return

def calculate_order(order, menu = menu, tips = 0.18):
    sum = 0
    for i in range(len(order)):
        if order[i] not in menu.keys():
            print("Sorry", order[i], "not available")
        else:
            sum += menu.get(order[i])
    sum = sum * 1.06
    sum = sum + tips
    return sum


def print_the_menu(menu = menu):
    result = []
    for k,v in menu.items():
        print(k,v)


cville_menus("orange", 4, menu)
print(menu)

print(calculate_order(["apple", "orange", "noodles"],menu, 0.2))

print(print_the_menu(menu))

























