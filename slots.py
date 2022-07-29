from sys import getsizeof

class WithoutSlots():
    def __init__(self) -> None:
        self.foo = 1
        self.bar = 2
        self.baz = 3

class WithSlots():
    __slots__ = ["foo", "bar", "baz"]
    def __init__(self) -> None:
        self.foo = 1
        self.bar = 2
        self.baz = 3

if __name__=="__main__":
    no_slots = [WithoutSlots() for _ in range(1000000)]
    slots = [WithSlots() for _ in range(1000000)]
    print(f"Without Slots = {getsizeof(no_slots)}")
    print(f"With Slots = {getsizeof(slots)}")

