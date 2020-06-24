def format_name(first, last, middle=''):

    if middle:
        fullname = first + ' ' + middle + ' ' + last
    else:
        fullname = first + ' ' + last
    return fullname.title()


def format_city(city, country, population=''):
    if population:
        city_country = city + ',' + country + ' - population' + ' ' + population
    else:
        city_country = city + ',' + country
    return city_country.title()
