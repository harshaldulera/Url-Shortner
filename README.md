# URL Shortener

This is a URL shortener project built with Django, AJAX, CSS, and JavaScript. It allows users to input a URL and receive a shortened version of that URL in localhost format.

## Features

- Converts a user-provided URL into a shortened localhost URL.
- Uses AJAX for asynchronous requests to the backend.
- Utilizes Django's built-in database for storing and retrieving URL mappings.
- Simple and intuitive user interface.

## Prerequisites

Make sure you have the following installed on your local machine:

- Python 3.x
- Django (version 3.x or later)

## Getting Started

To get started with the URL shortener, follow these steps:

1. Clone this repository to your local machine or download the ZIP file.
2. Navigate to the project directory.
```cd Url-Shortner```

3. Install the project dependencies.
```pip install -r requirements.txt```


4. Apply the database migrations.
```python manage.py migrate```


5. Start the development server.
```python manage.py runserver```


6. Open your web browser and go to `http://localhost:8000` to access the URL shortener.

## Usage

1. Enter a URL into the input field on the homepage.
2. Click the "Shorten" button.
3. The shortened URL will be displayed below the input field.
4. Click the "Copy" button to copy the shortened URL to your clipboard.

## Technologies Used

- Django - A Python-based web framework used for building the backend of the URL shortener.
- AJAX - Used for making asynchronous requests to the backend and updating the webpage without refreshing.
- CSS - Used for styling the user interface.
- JavaScript - Used for handling user interactions and AJAX requests.

## Contributing

If you want to contribute to this project, you can follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request in this repository.


## Acknowledgements

The URL shortener project was inspired by the need to create concise and memorable URLs for local development purposes. It was built as a learning exercise and can be customized and expanded upon to fit specific requirements.

## Contact

If you have any questions, suggestions, or issues, please feel free to reach out to me.

Email: harshaldulera82@gmail.com

## Conclusion

The URL shortener project provides a simple and efficient way to convert long URLs into shortened localhost URLs. It can be a valuable tool for web developers and anyone who needs to work with URLs in a local development environment.
