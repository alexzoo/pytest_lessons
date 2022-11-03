
from faker import Faker

from src.base_classes.builder import BuilderBaseClass

fake = Faker()


class FilmGenerator(BuilderBaseClass):

    def __init__(self):
        super().__init__()
        self.result = {}
        self.reset()

    def set_film_type(self,
                      film_id=fake.random_number(2),
                      status=fake.random_element(['active', 'delayed']),
                      title=fake.sentence(10),
                      is_premiere=fake.boolean()):
        self.result['film_id'] = film_id
        self.result['status'] = status
        self.result['title'] = title
        self.result['is_premiere'] = is_premiere
        return self

    def reset(self):
        self.set_film_type()

    def build(self):
        return self.result
