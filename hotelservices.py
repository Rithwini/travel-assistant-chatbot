class HotelService:
    def __init__(self):
        # Hardcoded data for hotels in specific locations
        self.hotels_data = {
            "Mumbai": [
                {
                    "hotel_name": "The Taj Mahal Palace",
                    "price_breakdown": {"gross_price": 2500},
                    "currency_code": "Rs",
                },
                {
                    "hotel_name": "Trident Nariman Point",
                    "price_breakdown": {"gross_price": 2700},
                    "currency_code": "Rs",
                }
            ],
            "Goa": [
                {
                    "hotel_name": "The Leela Palace",
                    "price_breakdown": {"gross_price": 3000},
                    "currency_code": "Rs",
                },
                {
                    "hotel_name": "Taj Palace",
                    "price_breakdown": {"gross_price": 2200},
                    "currency_code": "Rs",
                }
            ],
            "Hyderabad": [
                {
                    "hotel_name": "The Leela Goa",
                    "price_breakdown": {"gross_price": 3500},
                    "currency_code": "Rs",
                },
                {
                    "hotel_name": "Taj Exotica Resort & Spa",
                    "price_breakdown": {"gross_price": 3200},
                    "currency_code": "Rs",
                }
            ]
        }

    def find_hotel(self, city, check_in, check_out, guests=1):
        # Fetch hotels for the given city
        hotels = self.hotels_data.get(city, [])

        # Handle case where no hotels are found for the specified city
        if not hotels:
            return f"No hotels available in {city} for the specified dates."

        # Assuming we return the first hotel from the hardcoded list
        hotel_details = hotels[0]
        return (f"Hotel found: {hotel_details['hotel_name']} in {city} "
                f"available from {check_in} to {check_out} for {guests} guests. "
                f"Price: {hotel_details['price_breakdown']['gross_price']} {hotel_details['currency_code']}.")
