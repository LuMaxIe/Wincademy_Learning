__winc_id__ = '25a8041d2d5e4e3ab61ab1be43bfb863'
__human_name__ = 'dictionaries'


def create_passport(name_requester, birth_date, birth_place, height, nationality):

    pass_port = {
      "name": name_requester,
      "date_of_birth": birth_date,
      "place_of_birth": birth_place,
      "height": height,
      "nationality": nationality
    }
    return pass_port


def add_stamp(passport, country):
    passport_to_update = passport
    if country != passport_to_update['nationality']:
        if "stamps" not in passport_to_update:
            passport_to_update['stamps'] = [country]
        else:
            passport_to_update['stamps'].append(country)

    return passport_to_update


def check_passport(passport, country, countries_access, countries_denied):

    is_allowed = country in countries_access[passport['nationality']]
    is_denied = False

    countries_with_access_limitations = countries_denied.keys()
    if country in countries_with_access_limitations:
        for c in countries_denied[country]:
            if c in passport['stamps'] or c == passport['countries']:
                is_denied = True

    return False if is_denied is True or is_allowed is False else add_stamp(passport, country)
