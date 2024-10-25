from flask import Flask, render_template, request
from weather_data import get_weather_data  # Ensure the correct function is imported

def create_app():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        weather_data = {}
        alerts = []

        if request.method == 'POST':
            city = request.form['city']
            weather_data = get_weather_data(city)  # Call the correct function

            # Example logic for setting alerts based on the fetched weather data
            if weather_data and 'main' in weather_data:
                temperature = weather_data['main']['temp']
                if temperature > 35:  # Example threshold for alert
                    alerts.append("High temperature alert!")

        return render_template("index.html", weather_data=weather_data, alerts=alerts)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
