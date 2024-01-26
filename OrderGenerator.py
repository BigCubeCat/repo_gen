import random
import json

from utils import random_string

  
class OrderGenerator:
    def __init__(self, towns, count_waypoints=2):
        self.towns = towns
        self.count_waypoints = count_waypoints
        self.data = {
            "clientId": random_string(random.randrange(1, 10)),
            "cargo": self.generate_cargo(),
            "deadline": self.generate_deadline(),
            "waypoints": {
                "points": self.generate_waypoints(self.count_waypoints)
            }
        }

    def shotrify(self, value: float) -> str:
        return str(int(value * K) / K)

    def generate_deadline(self):
        return {
            "noDeadline": True,
            "beginDate": 0,
            "endDate": 0
            }
        
    def generate_cargo(self):
        count = random.randrange(1, 100)
        return {
            "unit": "good",
            "count": count,
            "description": random_string(count),
            "price": 100
        }


    def generate_waypoint(self):
        return random.choice(self.towns)


    def generate_waypoints(self, count: int):
        return [
            self.generate_waypoint() for _ in range(count)
        ]

    def get_request_body(self):
        return self.data
    
    def dump(self, filename: str):
        with open(filename, 'w', encoding="utf-8") as file:
            json.dump(self.data, file, indent=4)
