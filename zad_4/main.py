"""
import requests
response = requests.get('https://api.openbrewerydb.org/v1/breweries', params={"per_page": 2})
data = response.json()
print(data)
"""
class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str,
                 address_1: str | None, address_2: str | None,
                 address_3: str | None, city: str,
                 state_province: str | None, postal_code: str | None,
                 country: str, longitude: float | None,
                 latitude: float | None, phone: str | None,
                 website_url: str | None, state: str | None,
                 street: str | None) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street
    def __str__(self) -> str:
        return (f"{self.name} ({self.brewery_type}) – "
                f"{self.street or 'brak adresu'}, {self.city}, {self.country}")