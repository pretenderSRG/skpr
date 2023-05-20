from main import ticket_price, get_rating


assert ticket_price(0) == "FREE", "Error for 0"
assert ticket_price(1) == "FREE", "Error for 1"
assert ticket_price(7) == "100 $", "Error for 7"
assert ticket_price(18) == "200 $", "Error for 18"
assert ticket_price(25) == "300 $", "Error for 25"
assert ticket_price(60) == "ERROR", "Error for 60"
assert ticket_price(0.5) == "FREE", "Error for 0.5"
assert ticket_price(-1) == "ERROR", "Error for -1"

print("All ticket tests are completed")


assert get_rating('*') == 1, "Error for *"
assert get_rating('*'*2) == 2, "Error for **"
assert get_rating('*'*3) == 3, "Error for ***"
assert get_rating('*'*4) == 4, "Error for ****"
assert get_rating('*'*5) == 5, "Error for *****"
assert get_rating('*'*6) == "ERROR", "Error for ******"
assert get_rating(25) == "ERROR", "Error for number"

print('ALL raiting teste are completed')