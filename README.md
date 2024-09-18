# Local API Tester

![exmaple](./images/example.jpeg)

Local API Tester is a lightweight, user-friendly tool for making API calls directly from your local machine. Built with Python and Flask, it provides an attractive web interface for sending requests and viewing responses without the need for complex external tools like Postman.

## Features

- Support for GET, POST, PUT, and DELETE HTTP methods
- Custom header input
- Request body input for POST and PUT requests
- Clean and intuitive web interface
- Real-time response display
- Local deployment for privacy and speed

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed
- pip (Python package installer)

## Installation

1. Clone this repository to your local machine:
   ```
   git clone https://github.com/labeveryday/local-api-tester.git
   ```

2. Navigate to the project directory:
   ```
   cd simple-api-tester
   ```

3. Install the required Python packages:
   ```
   pip install flask requests
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```

2. Open your web browser and go to `http://localhost:5000`

3. Use the web interface to make API calls:
   - Enter the API URL in the "URL" field
   - Select the HTTP method (GET, POST, PUT, DELETE)
   - Add any headers in JSON format in the "Headers" field
   - For POST or PUT requests, enter the request body in the "Body" field
   - Click "Send Request"

4. View the API response in the "Response" section below the form

## Configuration

The application runs on `localhost` port 5000 by default. To change this, modify the `app.run()` line in `app.py`:

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
```

## To test your app

Here are a few free, public APIs you can use to test the API calling tool:

1. JSONPlaceholder - A fake online REST API for testing and prototyping
   - GET request: https://jsonplaceholder.typicode.com/posts/1
   - POST request: https://jsonplaceholder.typicode.com/posts

2. OpenWeatherMap - Current weather data
   - GET request: http://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY
   (You'll need to sign up for a free API key)

3. Random User Generator - Generate random user data
   - GET request: https://randomuser.me/api/

4. Dog API - Random dog images
   - GET request: https://dog.ceo/api/breeds/image/random

5. Pokemon API - Information about Pokemon
   - GET request: `https://pokeapi.co/api/v2/pokemon/ditto`

6. REST Countries - Information about countries
   - GET request: `https://restcountries.com/v3.1/name/united`

7. NASA API - Various NASA data, including Astronomy Picture of the Day
   - GET request: https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY
   (You can use DEMO_KEY for testing, but it's rate limited)

8. Cat Facts - Random cat facts
   - GET request: https://catfact.ninja/fact

9. IP API - Geolocation data for an IP address
   - GET request: http://ip-api.com/json/

10. Jokes API - Random jokes
    - GET request: https://official-joke-api.appspot.com/random_joke

These APIs are generally free to use and don't require authentication (except for OpenWeatherMap and NASA, which require API keys). They're perfect for testing your API tool with different types of requests and responses.

Remember to respect the usage limits of these APIs. Some may have rate limiting or require attribution for extensive use.

## Customization

You can customize the look and feel of the application by modifying the HTML and CSS in the `templates/index.html` file. The application uses Bootstrap for styling, which can be easily adjusted to fit your preferences.

## Security Note

This tool is designed for local use and testing. It does not include authentication or encryption features. Do not use it to send sensitive data or deploy it on a public server without implementing proper security measures.

### About me

My passions lie in Network Engineering, Cloud Computing, Automation, and impacting people's lives. I'm fortunate to weave all these elements together in my role as a Developer Advocate. On GitHub, I share my ongoing learning journey and the projects I'm building. Don't hesitate to reach out for a friendly hello or to ask any questions!

My hangouts:
- [LinkedIn](https://www.linkedin.com/in/duanlightfoot/)
- [YouTube](https://www.youtube.com/@LabEveryday)
