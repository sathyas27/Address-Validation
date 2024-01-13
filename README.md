# Address-Validation

This code uses the googlemaps API to validate an Excel sheet of random Canadian, Asian, and South American addresses, as they are each sent into the googlemaps.addressvalidation() function and return an intensive list of each component of the address that Google Maps can verify. This including a formatted/correct address, postal code, area code, locality, adminstrative area, confirmation levels for each of these components, and other components as well. These values are stored in a dataframe and once these values are processed, it is then stored in a new Excel sheet that labels each column and keeps all the address data as organized as the dataframe.

Attached below are examples of the original data, versus the data that gets processed and stored in an new Excel file.

## Original Data
<img width="887" alt="Screenshot 2024-01-13 at 2 16 29 AM" src="https://github.com/sathyas27/Address-Validation/assets/82248255/aa7fb3c7-5727-4c65-9d5a-c50ebd216b71">

## Processed Data
<img width="1119" alt="Screenshot 2024-01-13 at 2 16 09 AM" src="https://github.com/sathyas27/Address-Validation/assets/82248255/773ead1f-4e31-42d7-bdcc-6aa98e8b4624">
