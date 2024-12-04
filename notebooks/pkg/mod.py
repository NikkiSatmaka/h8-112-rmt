def add_member(array: list = ["a", "b", "c"], new_member="default"):
    return array + [new_member]


class Foo:
    def __init__(self) -> None:
        self.foo = "bar"

    def bar(self):
        print(self.foo)
