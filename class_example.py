class SimpleExample:
    """A simple example class"""
    max = 256

    def message(self):
        return 'Hello, Classes!'


simpleObj = SimpleExample()
print(simpleObj.max)
print(simpleObj.message())
del simpleObj


