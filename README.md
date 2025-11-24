**🌤️ Python Weather App**
A simple, lightweight, and user-friendly desktop weather application built using Python and Tkinter. This app fetches real-time weather data for any city worldwide using the OpenWeatherMap API.

**✨ Features**
>Real-time Weather Data: Get current weather conditions for any city.
>Clean GUI: A simple and intuitive interface built with Tkinter.

**Key Information Display:**

•Weather
•Weather Description (e.g., clear sky, rain)
•Temperature
•Pressure

**🛠️ Technologies Used**

•Python 3
•Tkinter (for the Graphical User Interface)
•Requests library (for making API calls)
•OpenWeatherMap API (for weather data)

**📦 Installation & Setup**

Follow these steps to run the application on your local machine.

*1. Prerequisites*
•Ensure you have Python 3 installed on your system. You can download it from python.org.
•You need an API key from OpenWeatherMap.

*2. Get Your Free API Key*
•Visit OpenWeatherMap.
•Click on "API" in the top navigation bar, then under "Current Weather Data", click on "API doc".
•On the API documentation page, find the section on the right titled "Built-in API request by city name".
•You will need to Sign Up / Register for a free account.
•After registering, verify your email address.
•Once logged in, go to your dashboard and navigate to the "API Keys" tab. Your default key will be there, or you can generate a new one.

*3. Clone the Repository*

**git clone https://github.com/your-username/your-weather-app-repo.git
cd your-weather-app-repo**

*4. Install Required Library*
This project uses the requests library. Install it using pip:

**pip install requests**

*5. Configure the API Key*
Open the Python script (e.g., weather_app.py) and replace the placeholder 'API_KEY' with the actual API key you generated in Step 2.

# In your code, find this line and update it:
**API_KEY = 'YOUR_ACTUAL_API_KEY_HERE'  # Get your free API key from https://openweathermap.org/**

The app uses the following API endpoint, which is already built into the code:
**https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric**

**🚀 How to Run**
•Ensure you have completed the setup steps above.

•Run the Python script from your terminal or command prompt:

**python weather_app.py**

•The application window will open.

•Enter the name of a city in the text field.

•Click the "Done" button.

•The current weather information for that city will be displayed below.

**Acknowledgments**
•Weather data provided by OpenWeatherMap.
•Built with the amazing Python language.
