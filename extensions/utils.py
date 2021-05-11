
def change_format_date(date):
    print(555)
    jmonth = {
        "1": "فروردین",
        "2": "اردیبهشت",
        "3": "خرداد",
        "4": "تیر",
        "5": "مرداد",
        "6": "شهریور",
        "7": "مهر",
        "8": "آبان",
        "9": "آذر",
        "10": "دی",
        "11": "بهمن",
        "12": "اسفند",
    }
    time_to_str = "{},{},{}".format(date.year, date.month, date.day)
    time_to_tuple = time_to_str.split(',')
    output = "{} {} {},ساعت{}:{}".format(time_to_tuple[2], jmonth[time_to_tuple[1]], time_to_tuple[0], date.hour, date.minute)
    return output
