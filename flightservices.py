class FlightService:
    def __init__(self):
        # Static flight data for predefined routes
        self.flights_data = {
            ("Mumbai", "Delhi"): [
                {
                    "airline_name": "Air India",
                    "flight_number": "AI101",
                    "origin_airport": "Chhatrapati Shivaji Intl",
                    "origin_iata": "BOM",
                    "departure_time": "2024-10-16 06:30 ",
                    "destination_airport": "Indira Gandhi Intl",
                    "destination_iata": "DEL",
                    "arrival_time": "2024-10-15 08:45",
                    "flight_status": "On Time",
                },
                {
                    "airline_name": "IndiGo",
                    "flight_number": "6E305",
                    "origin_airport": "Chhatrapati Shivaji Intl",
                    "origin_iata": "BOM",
                    "departure_time": "2024-10-15 09:00",
                    "destination_airport": "Indira Gandhi Intl",
                    "destination_iata": "DEL",
                    "arrival_time": "2024-10-15 11:15",
                    "flight_status": "On Time",
                },
            ],
            ("Bangalore", "Goa"): [
                {
                    "airline_name": "SpiceJet",
                    "flight_number": "SG202",
                    "origin_airport": "Kempegowda Intl",
                    "origin_iata": "BLR",
                    "departure_time": "2024-10-16 12:30",
                    "destination_airport": "Goa Intl",
                    "destination_iata": "GOI",
                    "arrival_time": "2024-10-16 13:45",
                    "flight_status": "Delayed",
                }
            ],
        }

    def find_flight(self, origin, destination, date):
        # Lookup the static data based on origin and destination
        flights = self.flights_data.get((origin, destination), [])
        if not flights:
            return f"No flights found from {origin} to {destination} on {date}."

        # Build a detailed report of the available flights
        flight_details_list = []
        for flight in flights:
            flight_info = (
                f"Airline: {flight['airline_name']}\n"
                f"Flight Number: {flight['flight_number']}\n"
                f"Origin: {flight['origin_airport']} ({flight['origin_iata']})\n"
                f"Scheduled Departure: {flight['departure_time']}\n"
                f"Destination: {flight['destination_airport']} ({flight['destination_iata']})\n"
                f"Scheduled Arrival: {flight['arrival_time']}\n"
                f"Flight Status: {flight['flight_status']}"
            )
            flight_details_list.append(flight_info)

        # Join all flight details in a human-readable format
        return "\n\n".join(flight_details_list)
