class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def get_commands(self):
        return self.commands

class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self, name, animal_type):
        if name and animal_type:
            animal = Animal(name, animal_type)
            self.animals.append(animal)
            self.counter.add()
            return animal
        else:
            raise ValueError("Name and animal type must be provided to add an animal.")

    def train_animal(self, animal, new_commands):
        for command in new_commands:
            animal.add_command(command)

    def list_animals(self):
        return self.animals

class Counter:
    def __init__(self):
        self._count = 0

    def add(self):
        self._count += 1

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._count > 0:
            raise Exception("Resource not properly closed")

def main():
    registry = AnimalRegistry()

    while True:
        print("\nAnimal Registry Menu:")
        print("1. Add a new animal")
        print("2. List registered animals")
        print("3. Train an animal")
        print("4. Display commands for an animal")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the animal: ")
            animal_type = input("Enter the type of the animal: ")
            try:
                animal = registry.add_animal(name, animal_type)
                print(f"Added a new {animal_type}: {name}")
            except ValueError as e:
                print(e)
        elif choice == '2':
            animals = registry.list_animals()
            if animals:
                print("List of registered animals:")
                for idx, animal in enumerate(animals, 1):
                    print(f"{idx}. {animal.name} ({animal.animal_type})")
            else:
                print("No animals in the registry.")
        elif choice == '3':
            name = input("Enter the name of the animal to train: ")
            new_commands = input("Enter new commands (comma-separated): ").split(',')
            for animal in registry.list_animals():
                if animal.name == name:
                    registry.train_animal(animal, new_commands)
                    print(f"{name} has been trained with new commands.")
                    break
            else:
                print(f"No animal with the name {name} found.")
        elif choice == '4':
            name = input("Enter the name of the animal to display commands: ")
            for animal in registry.list_animals():
                if animal.name == name:
                    commands = animal.get_commands()
                    if commands:
                        print(f"{name} knows the following commands:")
                        for idx, command in enumerate(commands, 1):
                            print(f"{idx}. {command}")
                    else:
                        print(f"{name} does not know any commands yet.")
                    break
            else:
                print(f"No animal with the name {name} found.")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
