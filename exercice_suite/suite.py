import matplotlib.pyplot as plt

class Suite():

    def __init__(self, last, function, *initials):
        self.initials = list(initials)
        self.last_results = list(initials)
        self.function = function
        self.max_yielded = last
        self.next_yielded = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_yielded < len(self.last_results):
            result = self.last_results[self.next_yielded]
            self.next_yielded += 1
            return result
        elif self.next_yielded <= self.max_yielded:
            new_result = self.function(self.next_yielded, *(self.last_results))
            self.last_results.append(new_result)
            self.last_results.pop(0)
            self.next_yielded += 1
            return new_result
        else:
            raise StopIteration()

    def __add__(self, other):
        return(Suite(float('inf'), (lambda n: self.__next__() + other.__next__())))

    def plot(self):
        plt.plot(list(self))
        plt.show()
            

class Fibonacci(Suite):

    def __init__(self, last):
        Suite.__init__(self, last, (lambda n, x, y: x + y), 1, 1)

   

    

##class Conway(Suite):
##
##    def __init__(self, last, initial):
##        Super.__init__(self, last, self.conway, [initial])
##
##    def conway(self, n, x):
        
class Syracuse(Suite):

    def __init__(self, last, initial):
        Suite.__init__(self, last, self.syracuse, initial)

    def syracuse(self, rang, terme):
        if (terme % 2) == 0:
            return terme // 2
        else:
            return 3 * terme + 1

class SyracuseLength(Suite):

    def __init__(self, last):
        Suite.__init__(self, last, self.syracuse_length)

    def syracuse_length(self, n):
        generator = Syracuse(float('inf'), n)
        res = 0
        for elem in generator:
            if elem <= 4 and elem != 3:
                return res
            else:
                res += 1
        return res


#SyracuseLength(100000).plot()

a = Fibonacci(5)
b = Fibonacci(6)

for x in a+b:
    print(x)
