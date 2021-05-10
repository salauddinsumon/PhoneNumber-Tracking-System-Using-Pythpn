import phonenumbers
from test import Number

from phonenumbers import geocoder
ch_number = phonenumbers.parse(Number,"CH")
print(geocoder.description_for_number(ch_number,"en"  ))