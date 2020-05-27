from numbers import Real


class Vector:

    def create_list_with_size(self, size):
        i = 0.0
        liste = []
        if size > 0:
            while i < size:
                liste.append(float(i))
                i += 1
            return liste
        else:
            print("Need size > 0")
            quit()

    def create_list_with_tuple(self, tab_tuple):
        liste = []
        if len(tab_tuple) == 2:
            if isinstance(tab_tuple[0], int) and isinstance(tab_tuple[1], int):
                if tab_tuple[0] < tab_tuple[1]:
                    i = tab_tuple[0]
                    while i < tab_tuple[1]:
                        liste.append(float(i))
                        i += 1
                elif tab_tuple[0] > tab_tuple[1]:
                    i = tab_tuple[1]
                    while tab_tuple[0] > i:
                        liste.append(float(i))
                        i += 1
                else:
                    print("Error of tuple. Need different number")
                    quit()
            else:
                print("Error values on tuple need Integer")
                quit()
        else:
            print("Error Tuple is bad")
            quit()
        return liste

    def __init__(self, value):
        if isinstance(value, list):
            for d in value:
                if not isinstance(d, float):
                    print("ERROR LIST HAVE NO FLOAT")
                    quit()
            self.values = value
        elif isinstance(value, int):
            self.values = self.create_list_with_size(value)
        elif isinstance(value, tuple):
            self.values = self.create_list_with_tuple(value)
        else:
            print("Type of value is not supported")
            quit()
        self.size = len(self.values)

    def __add__(self, operator):
        result = []
        if isinstance(operator, Real):
            for i in self.values:
                result.append(float(operator + i))
        elif isinstance(operator, Vector):
            if self.size == operator.size:
                i = 0
                while i < self.size:
                    result.append(float(self.values[i] + operator.values[i]))
                    i += 1
            else:
                print("addition between two vectors of different size")
                quit()
        else:
            print("unsupported argument for addition")
            quit()
        return Vector(result)

    def __radd__(self, operator):
        return self.__add__(operator)

    def __rsub__(self, operator):
        result = []
        if isinstance(operator, Real):
            for i in self.values:
                result.append(float(operator - i))
        elif isinstance(operator, Vector):
            if self.size == operator.size:
                i = 0
                while i < self.size:
                    result.append(float(self.values[i] - operator.values[i]))
                    i += 1
            else:
                print("substraction between two vectors of different size")
                quit()
        else:
            print("unsupported argument for substraction")
            quit()
        return Vector(result)

    def __sub__(self, operator):
        result = []
        if isinstance(operator, Real):
            for i in self.values:
                result.append(float(i - operator))
        elif isinstance(operator, Vector):
            if self.size == operator.size:
                i = 0
                while i < self.size:
                    result.append(float(operator.values[i] - self.values[i]))
                    i += 1
            else:
                print("substraction between two vectors of different size")
                quit()
        else:
            print("unsupported argument for substraction")
            quit()
        return Vector(result)

    def __mul__(self, operator):
        scalar = []
        result = 0.0
        if isinstance(operator, Real):
            for i in self.values:
                scalar.append(float(operator * i))
        elif isinstance(operator, Vector):
            if self.size == operator.size:
                i = 0
                while i < self.size:
                    scalar.append(float(self.values[i] * operator.values[i]))
                    i += 1
                for i in scalar:
                    result += float(i)
                return result
            else:
                print("Multiplication between two vectors of different size")
                quit()
        else:
            print("unsupported argument for multiplication")
            quit()
        return Vector(scalar)

    def __rmul__(self, operator):
        return self.__mul__(operator)

    def __truediv__(self, operator):
        result = []
        if operator == 0:
            print("Zero division is imposible")
            quit()
        for i in self.values:
            result.append(float(i / operator))
        return Vector(result)

    def __rtruediv__(self, operator):
        result = []
        if operator == 0:
            print("Zero division is imposible")
            quit()
        for i in self.values:
            if i == 0:
                print("Zero division is imposible")
                quit()
            result.append(float(operator / i))
        return Vector(result)

    def __str__(self):
        s = ''
        for i, val in enumerate(self.values):
            s += "{}".format(val)
            if i != self.size - 1:
                s += ' '
        return s

    def __repr__(self):
        return str(self.values)
