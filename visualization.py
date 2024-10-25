import matplotlib.pyplot as plt
import pandas as pd

def generate_weather_plot(weather_data_store):
    plt.clf()  # Clear the current figure
    df = pd.DataFrame.from_dict(weather_data_store, orient='index')
    
    # Extract temperature and weather condition
    df['temp'] = df['main'].apply(lambda x: x['temp'])  # Extract temperature from main field
    df['weather'] = df['weather'].apply(lambda x: x[0]['description'])  # Extract weather description
    
    # Plotting
    plt.bar(df.index, df['temp'], color='blue')
    plt.xlabel('Cities')
    plt.ylabel('Temperature (°C)')
    plt.title('Current Temperature in Various Cities')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/weather_plot.png")  # Save the plot to the static directory
