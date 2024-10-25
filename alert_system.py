# alert_system.py
def check_alerts(weather_data, max_temp, min_temp):
    alerts = []
    if weather_data:
        current_temp = weather_data['main']['temp']  # Assuming 'temp' is part of the response
        if current_temp > max_temp:
            alerts.append(f"Alert: Temperature exceeds {max_temp} °C")
        elif current_temp < min_temp:
            alerts.append(f"Alert: Temperature below {min_temp} °C")
    return alerts
