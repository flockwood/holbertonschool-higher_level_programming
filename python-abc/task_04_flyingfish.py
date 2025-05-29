# Parent class: Fish
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


# Parent class: Bird
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


# Subclass: FlyingFish, inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    def fly(self):
        print("The flying fish is soaring!")

    def swim(self):
        print("The flying fish is swimming!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")


# ✅ Testing
if __name__ == "__main__":
    ff = FlyingFish()

    # Call methods
    ff.swim()       # "The flying fish is swimming!"
    ff.fly()        # "The flying fish is soaring!"
    ff.habitat()    # "The flying fish lives both in water and the sky!"

    # Print Method Resolution Order (MRO)
    print("\nMethod Resolution Order:")
    for cls in FlyingFish.__mro__:
        print(cls)
