def total_cal(c):
    t = sum(c.values())
    print(f"Initial price: {t}")
    if len(c) > 5:
        t = t*0.9
        return t


cart = {"Laptop": 60000, "Monitor": 25000, "Keyboard": 6000, "Mouse": 2000, "Speakers": 3000, "Table": 1000}
total = total_cal(cart)
print(f"Discount price: {total}")
