<h2>**Python JSON API Interaction**</h2>

This Python script interacts with a JSON API to perform CRUD operations on a 'people' resource. The script uses the requests library to send HTTP requests to a local JSON server and reads data from a JSON file named test.json. The primary operations include:

Importing Data: The script reads data from test.json and sends it to the API using a POST request. It validates the data structure and handles both individual dictionaries and lists of dictionaries.

Getting Data: The script includes a section for sending a GET request to the API to retrieve data. This task is associated with finding and filtering data.

Updating Data: There is a section for sending a PATCH request to update existing data in the API. It demonstrates how to modify specific attributes of a resource.

Deleting Data: Another section is dedicated to sending a DELETE request to remove data from the API. It checks if the data exists before attempting deletion.

Task 5 - Duplicates: There is a section that handles Task 5, which involves creating a JSON file with various examples of people data, including duplicates. The script imports this data, removes duplicates, and performs POST requests on the API.

Additional Validation: The script includes a validation function (validateData) to ensure that the imported data adheres to expected structures, such as correct data types.
