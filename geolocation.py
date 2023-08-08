import requests

def get_geolocation(api_key, url):
    api_endpoint = f"https://api.ipgeolocation.io/ipgeo"
    params = {
        "apiKey": api_key,
        "domain": url,
    }

    try:
        response = requests.get(api_endpoint, params=params)
        response_json = response.json()

        if response.status_code == 200:
            return response_json
        else:
            print(f"Error: {response_json.get('message', 'Unknown Error')}")
            return None

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual IPGeolocation API key
    api_key = "9bdbb45c527d4d799f825809c7d99daf"
    entered_url = input("Enter the URL to geolocate: ")

    geolocation_data = get_geolocation(api_key, entered_url)

    if geolocation_data:
        print("Geolocation Data:")
        print(f"IP Address: {geolocation_data['ip']}")
        print(f"Continent: {geolocation_data['continent_name']}")
        print(f"Country: {geolocation_data['country_name']}")
        print(f"City: {geolocation_data['city']}")
        print(f"Latitude: {geolocation_data['latitude']}")
        print(f"Longitude: {geolocation_data['longitude']}")
        print(f"Timezone: {geolocation_data['time_zone']}")
    
