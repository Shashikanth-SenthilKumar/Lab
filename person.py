class Person:
    def __init__(self):
        self.name = None
        self.height = None
        self.mass = None
        self.hair_color = None
        self.skin_color = None
        self.eye_color = None
        self.birth_year = None
        self.gender = None
        self.homeworld = None
        self.films = None
        self.species = None
        self.vehicles = None
        self.starships = None
        self.created = None
        self.edited = None
        self.url = None

    def from_json(self, json_data: dict):
        self.name = json_data.get('name')
        self.height = json_data.get('height')
        self.mass = json_data.get('mass')
        self.hair_color = json_data.get('hair_color')
        self.skin_color = json_data.get('skin_color')
        self.eye_color = json_data.get('eye_color')
        self.birth_year = json_data.get('birth_year')
        self.gender = json_data.get('gender')
        self.homeworld = json_data.get('homeworld')
        self.films = json_data.get('films')
        self.species = json_data.get('species')
        self.vehicles = json_data.get('vehicles')
        self.starships = json_data.get('starships')
        self.created = json_data.get('created')
        self.edited = json_data.get('edited')
        self.url = json_data.get('url')

    def print_name(self):
        return f"My name is {self.name}"

    def compare_age(self, person):
        if self.birth_year < person.birth_year:
            return "I, {self.name}, am younger than {person.name}"

        elif self.birth_year > person.birth_year:
            return f"I, {self.name}, am older than {person.name}"

        else:
            return f"I, {self.name}, am the same age as {person.name}"

    def count_starships(self):
        starships = len(self.starships)
        return f"I, {self.name}, have {starships} starships"
