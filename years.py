def zodiac(year:int):
    """ Find out zodiac sign of year.
        Return animal name.
    """
    animals = {
        0: "monkey", 1: "rooster", 2: "dog", 3: "pig", 4: "rat", 5: "bull",
        6: "tiger", 7: "hare", 8: "dragon", 9: "snake", 10: "horse", 11: "sheep"
    }

    if isinstance(year, int) and year > 0:
        return animals[year % 12]
    elif isinstance(year, str):
        try:
            year = int(year)
            if year > 0:
                return animals[year % 12]
        except ValueError:
            return f"What is '{year}'? I don't understand :("
    else:        
        return f"What is '{year}'? I don't understand :("


def leap_year(year):
    """ Check if year is leap year.
        Return true if the year is a leap year else false.
    """
    if isinstance(year, int) and year > 0:
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            return True
        return False
    elif isinstance(year, str):
        try:
            year = int(year)
            if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                return True
            return False
        except ValueError:
            return f"What is '{year}'? I don't understand :("
    else:
        return f"What is '{year}'? I don't understand :("


if __name__ == "__main__":
    print(f"1999: {zodiac(1999)}")
    print(f"2000: {zodiac(2000)}")
    print(f"0000: {zodiac(0000)}")
    print(f"-1999: {zodiac(-1999)}")
    print(f"19.99: {zodiac(-19.99)}")
    print(f"'1999': {zodiac('1999')}")
    print(f"'19a9': {zodiac('19a9')}")
    print()
    print(f"1999: {leap_year(1999)}")
    print(f"2000: {leap_year(2000)}")
    print(f"0000: {leap_year(0000)}")
    print(f"-1999: {leap_year(-1999)}")
    print(f"19.99: {leap_year(-19.99)}")
    print(f"'1999': {leap_year('1999')}")
    print(f"'19a9': {leap_year('19a9')}")
