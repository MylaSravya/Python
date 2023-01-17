
class too_much_bonus(Exception):pass

# Block to test the user defined exception

try:
    sal = 1000
    bonus = 100
    if bonus > (sal/2):
        raise too_much_bonus
except too_much_bonus:
    print("Too much bonus")