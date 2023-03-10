# import modules
import mystuff

# this is a class
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

# access a function apple() from mystuff
mystuff.apple()
# print a variable tangerine from mystuff
print(mystuff.tangerine)

# getting things from 'things'

# class style

# instantiate a class
thing = MyStuff()
thing.apple()
print(thing.tangerine)


# dict style
#MyStuff['apples']
