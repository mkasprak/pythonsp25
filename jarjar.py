class Cat:
    def __init__(self, breed, color, size, temperament, coat):
        self.__breed = breed
        self.__color = color
        self.__size = size
        self.__temperament = temperament
        self.__coat = coat

    # Getters
    def get_breed(self):
        return self.__breed

    def get_color(self):
        return self.__color

    def get_size(self):
        return self.__size

    def get_temperament(self):
        return self.__temperament

    def get_coat(self):
        return self.__coat

    # Setters
    def set_breed(self, breed):
        self.__breed = breed

    def set_color(self, color):
        self.__color = color

    def set_size(self, size):
        self.__size = size

    def set_temperament(self, temperament):
        self.__temperament = temperament

    def set_coat(self, coat):
        self.__coat = coat


    def verbal_demand():
        print("Neow")

    def communicate():
        print("taps you with paw")
    
    def display_info(self):
        print(f"Breed: {self.__breed}")
        print(f"Color: {self.__color}")
        print(f"Size: {self.__size}")
        print(f"Temperament: {self.__temperament}")
        print(f"Coat: {self.__coat}")


class SmartCat(Cat):
    def open_drawer(self):
        print("Cat opens drawer with toys.")

    def fetch(self):
        print("Cat brings back the catnip mouse you threw.")


def main():
    my_cat = Cat("Tabby", "Ginger", "Medium", "Affectionate", "Short-haired")
    my_cat.display_info()

    ginger = SmartCat("Tabby", "Ginger", "Medium", "Affectionate", "Short-haired")
    ginger.display_info()
    ginger.open_drawer()
    ginger.fetch()

main()
