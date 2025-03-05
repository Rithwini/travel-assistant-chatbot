class DestinationService:
    def suggest_destination(self, budget):
        destinations = {
            'low': ['Thailand', 'Vietnam', 'Cambodia','Varanasi','Hampi',''],
            'medium': ['Spain', 'Greece', 'Portugal','Visakhapatnam','Coorg','Udaipur'],
            'high': ['Japan', 'Australia', 'Switzerland','Leh-Ladakh-Jammu & Kashmir','Goa','Kerala Backwaters']
        }
        if budget in destinations:
            return f"Based on your budget, you might want to consider visiting: {','.join(destinations[budget])}."
        else:
            return "Please specify a valid budget category: low, medium, or high."
