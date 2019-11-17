"""
This code turn country names to continents.
"""


import country_converter as coco
from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

Continents = {
    'NA': 'North America',
    'SA': 'South America',
    'EU': 'Europe',
    'AS': 'Asia',
    'OC': 'Australia',
    'AF': 'Africa',
}


def country_to_continent(countries):
    """
    Convert countries to continents.
    A single country is ok but must be in a list.
    """
    continents = []
    for country in countries:
        try:
            iso = country_name_to_country_alpha2(country)
        except Exception:
            iso = coco.convert(names=country, to='ISO2')
        continent = country_alpha2_to_continent_code(iso)
        continent = Continents[continent]
        continents.append(continent)
    return continents
