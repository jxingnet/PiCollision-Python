#PiCollisions
import time


class Block:
    def __init__(self, x,  w,  m,  v,  xc):
        self.x = x*1.0
        #self.y = height - w
        self.w = w*1.0
        self.v = v*1.0
        self.m = m*1.0
        self.xConstraint = xc*1.0

    def hitWall(self):
        return self.x <= 0

    def reverse(self):
            self.v *= -1

    def collide(self, other):
        return not (self.x + self.w < other.x or self.x > other.x + other.w)

    def bounce(self, other):
            sumM = self.m + other.m
            newV = (self.m - other.m) / sumM * self.v
            newV += (2 * other.m / sumM) * other.v
            return newV        

    def update(self):
        self.x += self.v
        


class Sketch:
        __piMax = "3141592653589793238"
        count = 0
        timeSteps = 0
        def __init__(self, digits):
            if (digits > len(self.__piMax)):
                raise Exception("Digit is too large")

            print("Digits : ", digits)
            self.timeSteps = pow(10, digits - 1)

            pistr = self.__piMax[0:digits]
            self.pi = int(pistr)

            # setup
            self.block1 = Block(100, 20, 1, 0, 0)
            m2 = pow(100, digits - 1)
            self.block2 = Block(300, 100, m2, -1.0 / self.timeSteps, 20)
        
        def draw(self):
            clackSound = False

            for i in range(0, self.timeSteps-1):
                if (self.block1.collide(self.block2)):
                    v1 = self.block1.bounce(self.block2)
                    v2 = self.block2.bounce(self.block1)
                    self.block1.v = v1
                    self.block2.v = v2
                    clackSound = True
                    self.count+=1
                if (self.block1.hitWall()):
                    self.block1.reverse()
                    clackSound = True
                    self.count+=1
                self.block1.update()
                self.block2.update()
            

            if (clackSound):
                print("Clack...")
            

            #block1.show();
            #block2.show();

            print(self.count)

            return self.pi == self.count


class App:
    def Run(self):
        digits = 7 # number of digits
        sketch = Sketch(digits)
        r = False
        while not r:
            r = sketch.draw()

if __name__ == '__main__':
    print("Start...")
    t0 = time.time()
    App().Run()
    print("Elapsed in seconds: ", time.time() - t0)
    print("...end")

