def total_cal(c):
    t = sum(c.values())
    print(f"Initial price: {t}")
    if 20000 < t < 50000:
        t = t*0.9
        return t
    elif t > 50000:
        t = t*0.85
        return t


cart = {"Laptop": 6000, "Monitor": 25000, "Keyboard": 6000, "Mouse": 2000, "Speakers": 3000, "Table": 8000}
total = total_cal(cart)
print(f"Discount price: {total}")
