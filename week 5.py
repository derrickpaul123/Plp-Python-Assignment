
class Superhero:
    """
    A base class to represent a Superhero.
    """
    def __init__(self, name, secret_identity, power):
        """
        The constructor method to initialize a new Superhero object.
        'self' refers to the instance of the object.
        name: The superhero's alias.
        secret_identity: The hero's civilian name.
        power: A description of the hero's primary power.
        """
        self.name = name
        self.secret_identity = secret_identity
        self.power = power
        self.is_active = True

    def use_power(self):
        """A method that simulates the superhero using their power."""
        if self.is_active:
            print(f"{self.name} uses their power: {self.power}!")
        else:
            print(f"{self.name} is currently inactive and cannot use their power.")

    def reveal_identity(self):
        """A method to reveal the superhero's secret identity."""
        print(f"The person behind the mask is... {self.secret_identity}!")
        self.is_active = False
        print(f"Oh no! {self.name} is now inactive.")

# A subclass that inherits from the Superhero class
class FlyingSuperhero(Superhero):
    """
    A subclass for a Superhero who can fly, inheriting all features from the
    base Superhero class.
    """
    def __init__(self, name, secret_identity, power, max_altitude):
        """
        The constructor for FlyingSuperhero.
        Calls the parent class's constructor using 'super()' to initialize
        the common attributes, then adds its own unique attribute.
        """
        super().__init__(name, secret_identity, power)
        self.max_altitude = max_altitude

    def fly(self):
        """A unique method for the FlyingSuperhero subclass."""
        print(f"{self.name} soars through the sky up to {self.max_altitude} meters!")

# --- Creating instances and demonstrating functionality ---

print("--- Assignment 1 Demonstration ---")
# Create an instance of the base class
hero_1 = Superhero("Captain Courage", "Leo Valiant", "Super Strength")
print(f"Hero Name: {hero_1.name}, Power: {hero_1.power}")
hero_1.use_power()
hero_1.reveal_identity()
hero_1.use_power() # This call will show the inactive message

print("-" * 20)

# Create an instance of the subclass
flying_hero = FlyingSuperhero("Sky Sentry", "Elara Vance", "Telekinesis", 10000)
print(f"Flying Hero Name: {flying_hero.name}, Power: {flying_hero.power}, Max Altitude: {flying_hero.max_altitude}m")
flying_hero.use_power()
flying_hero.fly()
flying_hero.reveal_identity()


# ==============================================================================
# Activity 2: Polymorphism Challenge! 🎭
# This section demonstrates polymorphism, where different objects can respond
# to the same method call in their own unique way.
# ==============================================================================

class Vehicle:
    """A generic base class for a vehicle."""
    def move(self):
        """A generic method for movement."""
        raise NotImplementedError("Subclass must implement abstract method")

class Car(Vehicle):
    """A specific class for a car."""
    def move(self):
        """The car's unique way of moving."""
        print("The car is driving on the road 🚗")

class Plane(Vehicle):
    """A specific class for a plane."""
    def move(self):
        """The plane's unique way of moving."""
        print("The plane is flying through the air ✈️")

class Boat(Vehicle):
    """A specific class for a boat."""
    def move(self):
        """The boat's unique way of moving."""
        print("The boat is sailing on the water 🚤")

# --- Creating instances and demonstrating polymorphism ---

print("\n--- Activity 2 Demonstration ---")
# Create a list of different vehicle objects
vehicles = [
    Car(),
    Plane(),
    Boat()
]

# Loop through the list and call the 'move()' method on each object.
# Despite all being called with the same method name, they each##
# perform a different action based on their class type. This is polymorphism.
for vehicle in vehicles:
    vehicle.move()
