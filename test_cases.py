import unittest
from weather_data import fetch_weather
from alert_system import check_alerts

class TestWeatherData(unittest.TestCase):
    def test_fetch_weather(self):
        city = "Bangalore"
        weather_data = fetch_weather(city)
        self.assertIsNotNone(weather_data)
        self.assertIn('main', weather_data)

    def test_alert_system(self):
        weather_data = {'main': {'temp': 36}}  # Simulate weather data
        alerts = check_alerts(weather_data, 35, 25)  # Check against thresholds
        self.assertIn("Alert: Temperature exceeds 35 °C", alerts)

if __name__ == '__main__':
    unittest.main()
