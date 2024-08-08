# Technical Test

This technical test is designed to assess your skills in both backend development using Python and FastAPI and frontend development using JavaScript with React. Please ensure that you complete all the questions within the provided timeframe.

If you encounter any issues while taking the test, please do not hesitate to contact us for assistance.

## FastAPI

In this section, you will implement new functionalities for the application's API. The data source is `database.json`, which contains user information.

### Task 1

In the `main.py` file, write an API endpoint that retrieves a user from the database based on their `id`. For example, an API call to `http://localhost:8000/users/1` should return a JSON response like the one below. The API call should also return the full list if no user `id` is provided. Ensure the API call validates the input and outputs.

```json
{
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
        "name": "Romaguera-Crona",
        "catchPhrase": "Multi-layered client-server neural-net",
        "bs": "harness real-time e-markets"
    }
}
```

### Task 2

Write an API endpoint that adds a new entry to the database.

## JavaScript React

Using the provided [sandbox](https://codesandbox.io/), complete the following tasks:

### Task 1

Make the app fetch data from the URL `https://jsonplaceholder.typicode.com/users/1` and display the data in the browser.

### Task 2

Extend the app to include a component that accepts a user's ID, fetches that user's data from `https://jsonplaceholder.typicode.com/users/{id}`, and displays the data.

Please ensure that the provided sandbox link is working correctly, and the URL `https://jsonplaceholder.typicode.com/users/1` is accessible.
