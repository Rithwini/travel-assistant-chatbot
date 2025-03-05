from flask import Flask, render_template, request
from travel.weatherservices import WeatherService
from travel.destinationservices import DestinationService
from travel.adviceservices import AdviceService
from travel.flightservices import FlightService
from travel.hotelservices import HotelService

app = Flask(__name__)

weather_service = WeatherService()
destination_service = DestinationService()
advice_service = AdviceService()
flight_service = FlightService()
hotel_service = HotelService()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def weather():
    
    city = request.form['city']
    weather_info = weather_service.get_weather(city)
    return render_template('index.html', weather_info=weather_info)

@app.route('/destination', methods=['POST'])
def destination():
    budget = request.form['budget']
    destination_info = destination_service.suggest_destination(budget)
    return render_template('index.html', destination_info=destination_info)

@app.route('/advice', methods=['POST'])
def advice():
    topic = request.form['topic']
    advice_info = advice_service.get_advice(topic)
    return render_template('index.html', advice_info=advice_info)

@app.route('/flight', methods=['POST'])
def flight():
    origin = request.form['origin']
    destination = request.form['destination']
    date = request.form['date']
    
    # Call the modified FlightService to fetch static flight information
    flight_info = flight_service.find_flight(origin, destination, date)

    # Render the template with the flight information
    return render_template('index.html', flight_info=flight_info)

@app.route('/hotel', methods=['POST'])
def hotel():
    city = request.form['city']
    check_in = request.form['check_in']
    check_out = request.form['check_out']
    guests = request.form.get('guests', 2)  # Default to 1 guest if not provided

    # Call the modified HotelService to fetch static hotel information
    hotel_info = hotel_service.find_hotel(city, check_in, check_out, guests)

    # Render the template with the hotel information
    return render_template('index.html', hotel_info=hotel_info)

if __name__ == "__main__":
    try:
        app.run(debug=True)
    except :
        print("e")
