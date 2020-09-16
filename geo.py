import geoip2.database
city_reader = geoip2.database.Reader('/home/antslab/GeoIP2-DB/GeoIP2-City_20200526/GeoIP2-City.mmdb')
city_reader_response = dict()
ip = "198.143.158.82"
city_response = city_reader.city(ip)
latitude = city_response.location.latitude
longitude = city_response.location.longitude