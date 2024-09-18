import random

class RandomList(list):
    def get_random_element(self):
        if self:
            index = random.randint(0, len(self) - 1)
            return self.pop(index)
        return None