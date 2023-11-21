import json
import requests
import re

jsonFile = open('test.json')
data = json.load(jsonFile)

url = "http://localhost:3002/people"

headers = {
    'Content-Type': 'application/json'
}


def checkStatusCode(type, statusCode, desiredResponseCode):
    if statusCode == desiredResponseCode:
        print(f"{type} Status Code {statusCode}: Sucess")
        return True
    else: 
        print(f"{type} Status Code {statusCode}: Fail")
        return False




# # POST REQUEST
def validateData(data):
    # Define a regex for email validation
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # Define a regex for date validation (format: YYYY-MM-DD)
    date_regex = r'\b\d{2}[/]\d{2}[/]\d{4}\b'
    # print("DATA: ", data)
    if not isinstance(data.get('id'), str):
        raise ValueError(f"Error in element {data}: id should be a string.")
    if not isinstance(data.get('fullName'), str):
        raise ValueError(f"Error in element {data}: fullName should be a string.")
    if not re.match(email_regex, data.get('email')):
        raise ValueError(f"Error in element {data}: email is not valid.")
    if not isinstance(data.get('job'), str):
        raise ValueError(f"Error in element {data}: job should be a string.")
    if not re.match(date_regex, data.get('dob')):
        raise ValueError(f"Error in element {data}: dob is not a valid date.")
    

def postData(data):
    if type(data) == list:
        for entry in data:
            try:
                validateData(entry)
            except ValueError as e:
                print(e)
            else:
                peopleResponse = requests.post(url, json=entry, headers=headers)
                checkStatusCode("POST", peopleResponse.status_code, 201)
    elif type(data) == dict:
        try:
            validateData(data)
        except ValueError as e:
            print(e)
        else:
            peopleResponse = requests.post(url, json=data, headers=headers)
            response_data = peopleResponse.json()
            new_id = response_data.get('id')
            print("Newly created ID:", new_id)
    else:
        print("Cannot POST. Invalid data type.")

# postData(data)




# # GET REQUEST 

def getData(index=None):
    if index is not None:
        getURL = f"{url}/{index}"
    else:
        getURL = f"{url}"

    peopleResponse = requests.get(getURL, headers=headers)

    if checkStatusCode('GET', peopleResponse.status_code, 200):
        responseData = peopleResponse.json()
        print(json.dumps(responseData, indent=2))

# getData("15")




# # PATCH REQUEST

def patchDataByIndex(index):
    patchURL = f"{url}/{index}"
    patch_data = {
        "fullName": "Michael Griffiths"
    }

    peopleResponse = requests.get(patchURL, headers=headers)

    if checkStatusCode('GET', peopleResponse.status_code, 200):
        peopleResponse = requests.patch(patchURL, json=patch_data, headers=headers)
        checkStatusCode('PATCH', peopleResponse.status_code, 200)

# patchDataByIndex("15")






 
# # DELETE REQUEST - IS IT BETTER TO CHECK IF IT IS THERE BEFORE DELETING OR RETURNING THE RESPONSE (EG SUCCESS OR FAIL?)

def deleteDataByIndex(index):
    deleteURL = f"{url}/{index}"
    peopleResponse = requests.get(deleteURL, headers=headers)
    statusCode = peopleResponse.status_code
    if checkStatusCode('GET', statusCode, 200):
        peopleResponse = requests.delete(deleteURL, headers=headers)
        statusCode = peopleResponse.status_code
        checkStatusCode('DELETE', statusCode, 200)


# deleteDataByIndex("4")
    
    




# TASK 5
# Extract all ids into an array


def deleteDuplicates():
    peopleResponse = requests.get(url, headers=headers)
    responseData = peopleResponse.json()
    
    # print(json.dumps(responseData, indent=2))
    
    id_array = [obj["id"] for obj in responseData]

    # print(id_array)
    
    seen = set()
    duplicates = []
    
    for item in id_array:
        if item in seen:  
            duplicates.append(item)
        else:
            seen.add(item)
    
    # print("Duplicates Found: ", duplicates)
    
    if len(duplicates) > 0:
        for item in duplicates:
            deleteURL = f"{url}/{item}"
            peopleResponse = requests.delete(deleteURL, headers=headers)
    else: 
        print("No duplicates found.")
        
    











#Task 1: Create a file in your directory containing valid JSON data for your server, import it, and send it to the API using a POST request.

#Task 2: Send a get request to your API and filter the data until you find the data you posted

#Task 3: Update the data using a PATCH and PUT request

#Task 4: Remove the data using a DELETE request

#Task 5: Create a json file with various example of people data, within the data create several duplicates, 
# import this data, remove duplicates and POST to the API

#Task 6: When importing the data, add some validation to ensure the data is structured how you would expect. Correct data types, etc.









while True:
    print("""
    Please select an option:
    1. Option 1 (POST DATA)
    2. Option 2 (GET DATA)
    3. Option 3 (PATCH DATA)
    4. Option 4 (DELETE DATA)
    5. Option 5 (REMOVE DUPLICATES)
    6. Exit
    """)

    choice = input("Enter your choice: ")

    if choice == "1":
        print("You selected Option 1.")
        postData(data)
        
    elif choice == "2":
        print("You selected Option 2.")
        index = input("Enter the index of data required. Alternatively, enter nothing to get all data back: ")
        getData(index)
        
    elif choice == "3":
        print("You selected Option 3.")
        index = input("Enter the index of data to patch: ") # we could ask what info to change and to what (if we had time)
        if index:
            patchDataByIndex(index)
        else: 
            print("No index supplied, please try again.")
        
    elif choice == "4":
        print("You selected Option 4.")
        index = input("Enter the index of data to delete: ")
        deleteDataByIndex(index)
        
    elif choice == "5":
        print("You selected Option 5.")
        deleteDuplicates()
        
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
