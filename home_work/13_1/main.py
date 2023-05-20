def ticket_price(age):

    if 0 <= age < 7:
        return "FREE"
    elif 7 <= age < 18:
        return "100 $"
    elif 18 <= age < 25:
        return "200 $"
    elif 25 <= age < 60:
        return "300 $"
    else:
        return "ERROR"


def get_rating(stars):
    if stars == '*':
        return 1
    elif stars == '**':
        return 2
    elif stars == '***':
        return 3
    elif stars == '****':
        return 4
    elif stars == '*****':
        return 5
    else:
        return "ERROR"