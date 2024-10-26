Weather Monitoring System


codebase: 
 
This project is hosted on GitHub. You can find the codebase at:
https://github.com/Simsar7/weather_monitoring


Overview
The Weather Monitoring System is designed to retrieve real-time weather data for specified cities using the OpenWeatherMap API.
It provides users with current temperature, weather conditions, and alerts for extreme temperatures.


Features
- Fetches real-time weather data.
- Displays current temperature and weather description for the user-entered city.
- Generates alerts based on user-defined temperature thresholds.


 Installation
 Prerequisites
- Python 3.x
- Docker (optional for containerization)

 Setup Instructions
1. Clone the Repository:
   ```bash
   git clone https://github.com/Simsar7/weather_monitoring

2. Navigate to the Project Directory:cd weather_monitoring

3. Install Dependencies: pip install -r requirements.txt

4. Running the Application: python app.py

5. Access the Application: Open your web browser and go to http://127.0.0.1:5000.


Dependencies
The following dependencies are required to run the application:

Flask
Requests
Matplotlib
These dependencies are specified in the requirements.txt


Design Choices
Modular Architecture: The application is structured with separate files for handling different functionalities.
User-Centric Design: The UI is designed to be simple and intuitive.

Security and Performance Considerations
API Key Management: The OpenWeatherMap API key is stored in config.py.
Input Validation: Basic validation is performed for user input.

Conclusion
This Weather Monitoring System provides a user-friendly way to access real-time weather data and receive alerts based on
 temperature thresholds.

GitHub Link
Access the complete codebase on GitHub: https://github.com/Simsar7/weather_monitoring