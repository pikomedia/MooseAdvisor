from googlemaps import GoogleMaps
api_key='AIzaSyCa4Z4UBYzondsv6vB_To6_7ZPREEgbdVA'
gmaps = GoogleMaps(api_key)
address = 'Constitution Ave NW & 10th St NW, Washington, DC'
lat, lng = gmaps.address_to_latlng(address)
print lat, lng
