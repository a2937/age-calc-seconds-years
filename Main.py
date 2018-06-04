def age_calc():
    seconds_or_years = input(
        "Type 's' if you want to enter your age in seconds. Type 'y' if you want to enter it as years. \n")
    if seconds_or_years.lower() == 's':

        user_age = input("Enter your age in seconds:")
        age_as_years = (int(user_age) / 365 / 24 / 60 / 60)
        print("You have lived for {} years.".format(age_as_years))
    elif seconds_or_years.lower() == 'y':
        user_age = input("Enter your age in years:")
        age_as_seconds = (int(user_age) * 365 * 24 * 60 * 60)
        print("You have lived for {} seconds.".format(age_as_seconds))
    return;


age_calc()
