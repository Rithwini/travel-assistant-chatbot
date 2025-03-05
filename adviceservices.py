class AdviceService:
    def get_advice(self, topic):
        advice = {
            'packing': "Pack light and only bring essentials.\nUse packing cubes to organize your items.",
            'safety': "Always keep your valuables in a secure place and be aware of your surroundings."
                      " Donot trust strangers easily.",
            'budget': "Set a daily budget and try to stick to it."
                      " Use apps to track your expenses."
        }
        return advice.get(topic.lower(), "Sorry, I don't have advice on that topic.")
