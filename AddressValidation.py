import googlemaps
import pandas as pd

gmaps = googlemaps.Client(key='API_KEY')

addresses_df = pd.read_excel("/Users/sathyaselvam/Downloads/Google_Address_Validation_Sample.xlsx", usecols=['C', 'D', 'E'])
addresses_df['combined_address'] = addresses_df.apply(lambda row: f"{row['C']} {row['D']} {row['E']}", axis=1)

def process_address(address):
    try:
        result = gmaps.addressvalidation(address)
        address_data = result['result']['address']
        postal_address = address_data['postalAddress']
        address_components = address_data['addressComponents']

        return {
            'Formatted Address': address_data.get('formattedAddress', 'N/A'),
            'Postal Code': postal_address.get('postalCode', 'N/A'),
            'Region Code': postal_address.get('regionCode', 'N/A'),
            'Administrative Area': postal_address.get('administrativeArea', 'N/A'),
            'Locality': postal_address.get('locality', 'N/A'),
            'Address Lines': postal_address.get('addressLines', 'N/A'),
            'Postal Code (Confirmation)': address_components[3].get('confirmationLevel', 'N/A'),
            'Administrative Area (Confirmation)': address_components[2].get('confirmationLevel', 'N/A')
        }
    except Exception as e:
        return {key: 'Error' for key in columns}

columns = ['Formatted Address', 'Postal Code', 'Region Code', 'Administrative Area', 'Locality', 'Address Lines', 'Postal Code (Confirmation)', 'Administrative Area (Confirmation)']
processed_addresses = addresses_df['combined_address'].apply(process_address)

df = pd.DataFrame(processed_addresses.tolist(), columns=columns)
df.to_excel('/Users/sathyaselvam/Downloads/Addresses.xlsx')
