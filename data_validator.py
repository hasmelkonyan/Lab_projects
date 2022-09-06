import re


def is_valid_email(email):
    """This function checks is email address valid or not
    """
    pat = '^[a-z0-9]+[\._]?[a-z0-9]+[@][a-zA-Z0-9_]+[.][a-zA-Z0-9]{2,3}$'  # (user)@(domain).(end)
    # [a-z0-9] begins with any number of alphanumeric characters
    # [\._]? there can be one or zero [\._] characters, two or more not allowed
    # then must be @ character
    # [a-zA-Z0-9_] domain,  alphanumeric characters and _(underscore) also allowed
    # [.][a-zA-Z0-9]{2,3}$ after domain must be ., and alphanumeric characters two or three
    if re.match(pat, email):
        return True
    return False


def is_valid_website_url(url):
    pat = "^((https?|ftp|smtp):\/\/)?(www.)?[a-z0-9]+\.[a-z]+(\/[a-zA-Z0-9#]+\/?)*$"
    if re.match(pat, url):
        return True
    return False


def is_leap_year(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    elif year % 4 == 0:
        return True


def is_valid_date(date):
    """This function checks is date valid or note. Տhe date must be entered in the following format "dd/mm/yyyy"
    """
    if len(date.split("/")) != 3:
        return False
    day = date.split("/")[0]
    month = date.split("/")[1]
    year = date.split("/")[2]
    if len(day) != 2 or len(month) != 2 or len(year) != 4:
        return False
    if not day.isnumeric() or not month.isnumeric() or not year.isnumeric():
        return False
    if int(month) > 12:
        return False
    else:
        if int(month) in [1, 3, 5, 7, 8, 10, 12]:
            if int(day) > 31:
                return False
        elif int(month) in [4, 6, 9, 11]:
            if int(day) > 30:
                return False
        elif int(month) == 2:
            if is_leap_year(int(year)):
                if int(day) > 29:
                    return False
            else:
                if int(day) > 28:
                    return False
    return True


def is_valid_number(val):
    pat = '^[-]?[0-9]+$'
    if re.match(pat, val):
        return True
    return False


def is_valid_credit_card_number(credit_card_type, credit_card_num):
    if credit_card_type == "Maestro" and credit_card_num.isnumeric() and 15 < len(credit_card_num) < 20 \
            and int(credit_card_num[0: 4]) in [5018, 5020, 5038, 5893, 6304, 6759, 6761, 6762, 6763]:
        return True
    elif credit_card_type == "MasterCard" and credit_card_num.isnumeric() and len(credit_card_num) == 16 \
            and int(credit_card_num[0: 2]) in [51, 52, 53, 54, 55]:
        return True
    elif credit_card_type == "Visa" and credit_card_num.isnumeric() and len(credit_card_num) in [13, 16, 19] \
            and int(credit_card_num[1]) == 4:
        return True
    return False


def is_valid_mobile_number(phone_number):
    """This function checks is it valid mobile number in Armenia
    """
    if not phone_number.isnumeric():
        return False
    if len(phone_number) != 11:
        return False
    if int(phone_number[0: 3]) != 374:
        return False
    if int(phone_number[3:5]) not in [91, 99, 96, 43, 33, 79, 55, 95, 41, 44, 66, 50, 93, 94, 77, 98]:
        return False
    return True


def main():
    while True:
        user_choose = input(
            "If you want to check if it's valid, then enter\nemail: 1\nWebsite URL: 2\nDate: 3\nNumber: 4\n"
            "CreditCard Number: 5\nMobile Phone Number: 6\nExit: any other button\nenter: ")
        if user_choose == "1":
            email = input("Input email: ")
            print(is_valid_email(email))
        elif user_choose == "2":
            url = input("Input Website URL: ")
            print(is_valid_website_url(url))
        elif user_choose == "3":
            date = input("Input Date: ")
            print(is_valid_date(date))
        elif user_choose == "4":
            val = input("Input number: ")
            print(is_valid_number(val))
        elif user_choose == "5":
            credit_card_type = input("Input credit card's type: ")
            credit_card_num = input("Input credit card's number: ")
            print(is_valid_credit_card_number(credit_card_type, credit_card_num))
        elif user_choose == "6":
            phone_number = input("Input mobile phone number: ")
            print(is_valid_mobile_number(phone_number))
        else:
            print("bye!!!")
            break


main()