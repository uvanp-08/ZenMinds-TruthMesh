import requests

# Replace this URL with the actual base URL of your API
base_url = "http://daksh.sastra.edu/fun/apis"

# Replace 'googleEmail' with the actual email or user identifier
cookie_data = {"googleEmail": "126003009@sastra.ac.in"}

# Make the API request to get questions
questions_endpoint = "/questions"
questions_url = f"{base_url}{questions_endpoint}"
questions_response = requests.post(questions_url, json={"email": cookie_data["googleEmail"]})

# Check if the request was successful (status code 200)
if questions_response.status_code == 200:
    questions_data = questions_response.json()

    # Print the questions
    for question in questions_data["questions"]:
        print(question)
else:
    print(f"Failed to retrieve questions. Status code: {questions_response.status_code}")
