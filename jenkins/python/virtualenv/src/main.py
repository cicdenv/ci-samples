import sys

from .sample.parsers import ZIP_PATTERN, LL_PATTERN
from .sample.weather import (
    zip_lookup,
    lat_lon_lookup,
    city_lookup,
)


def main():
    input = sys.argv[1]

    if ZIP_PATTERN.match(input):
        zip_code, country_code = input.split(",")
        r = zip_lookup(zip_code, country_code)
    elif LL_PATTERN.match(input):
        lat, lon = input.split(",")
        r = lat_lon_lookup(lat, lon)
    else:  # Assume city
        r = city_lookup(input)
    
    temp = r["main"]["temp"]
    print(temp)


if __name__ == '__main__':
    main()
