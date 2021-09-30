class DogBoarder:
    def __init__(self, total_slots, daily_rate):
        self.total_slots = total_slots
        self.daily_rate = daily_rate
        self.dogs = []
        self.slots_occupied = 0

    def board(self, name, breed, owner):
        boarded_dog = Dog(name, breed, owner)
        if self.is_full() == False:
            self.dogs.append(boarded_dog) 
            self.slots_occupied += 1
        else:
            raise(ValueError)
        

    def dog_in_list(self, name, breed, owner):
            for dog in self.dogs:
                if dog.name == name and dog.breed == breed and dog.owner == owner:
                    return True
                
    def pick_up(self, name, breed, owner, days):
            if self.dog_in_list(name, breed, owner) == True:
                for dog in self.dogs:
                    if dog.name == name and dog.breed == breed and dog.owner == owner:
                            self.dogs.remove(dog)
                            self.slots_occupied -= 1
                            cost = self.daily_rate * int(days)  
                            return cost
            else:
                raise(ValueError)

    def is_full(self):
        if self.slots_occupied == self.total_slots:
            return True
        return False


class Dog(DogBoarder):
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

 
