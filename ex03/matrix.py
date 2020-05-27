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


class Matrix:
    def __init__(self, matrice, value=(0, 0)):
        self.data = []
        self.shape = []
        data_row = []
        if isinstance(matrice, list):
            columns = 0
            for row in matrice:
                if isinstance(row, list):
                    for i in row:
                        data_row.append(i)
                else:
                    print("Type of value is not supported 1", self.data)
                    quit()
                self.data.append(data_row)
                data_row = []
                columns += 1
            self.shape.append(columns)
            self.shape.append(len(row))
        elif isinstance(matrice, tuple) and len(matrice) == 2:
            if isinstance(matrice[0], int) and isinstance(matrice[1], int):
                j = 0
                while j < matrice[1]:
                    i = 0
                    while i < matrice[0]:
                        data_row.append(0)
                        i += 1
                    self.data.append(data_row)
                    data_row = []
                    j += 1
                self.shape.append(matrice[0])
                self.shape.append(matrice[1])
            else:
                print("Type of value is not supported 2")
                quit()
        else:
            print("Type of value is not supported 3")
            quit()

    def __add__(self, operator):
        result = []
        result_add = []
        if isinstance(operator, Real):
            for i in self.data:
                for j in i:
                    result_add.append(float(operator + j))
                result.append(result_add)
                result_add = []
        elif isinstance(operator, Vector):
            if self.shape[0] == 1:
                if self.shape[1] == operator.size:
                    i = 0
                    while i < self.shape[1]:
                        result_add.append(float(self.data[0][i] +
                                                operator.values[i]))
                        i += 1
                    result.append(result_add)
                else:
                    print("Error vect + matrix. col matrix need == size Vect")
                    quit()
            else:
                print("Error vector + matrix. Dimention matrix need == 1")
                quit()
        elif isinstance(operator, Matrix):
            if self.shape == operator.shape:
                y = 0
                while y < self.shape[0]:
                    x = 0
                    while x < self.shape[1]:
                        result_add.append(float(self.data[y][x] +
                                                operator.data[y][x]))
                        x += 1
                    result.append(result_add)
                    result_add = []
                    y += 1
            else:
                print("addition between two matrix of different size")
                quit()
        else:
            print("unsupported argument for addition")
            quit()
        return Matrix(result)

    def __radd__(self, operator):
        return self.__add__(operator)

    def __sub__(self, operator):
        result = []
        result_sub = []
        if isinstance(operator, Real):
            for i in self.data:
                for j in i:
                    result_sub.append(float(j - operator))
                result.append(result_sub)
                result_sub = []
        elif isinstance(operator, Vector):
            if self.shape[0] == 1:
                if self.shape[1] == operator.size:
                    i = 0
                    while i < self.shape[1]:
                        result_sub.append(float(self.data[0][i] -
                                                operator.values[i]))
                        i += 1
                    result.append(result_sub)
                else:
                    print("Error vect + matrix. col matrix need == size vect")
                    quit()
            else:
                print("Error vector + matrix. Dimention matrix need == 1")
                quit()
        elif isinstance(operator, Matrix):
            if self.shape == operator.shape:
                y = 0
                while y < self.shape[0]:
                    x = 0
                    while x < self.shape[1]:
                        result_sub.append(float(self.data[y][x] -
                                                operator.data[y][x]))
                        x += 1
                    result.append(result_sub)
                    result_sub = []
                    y += 1
            else:
                print("substraction between two matrix of different size")
                quit()
        else:
            print("unsupported argument for substraction")
            quit()
        return Matrix(result)

    def __rsub__(self, operator):
        result = []
        result_sub = []
        if isinstance(operator, Real):
            for i in self.data:
                for j in i:
                    result_sub.append(float(operator - j))
                result.append(result_sub)
                result_sub = []
        elif isinstance(operator, Vector):
            if self.shape[0] == 1:
                if self.shape[1] == operator.size:
                    i = 0
                    while i < self.shape[1]:
                        result_sub.append(float(operator.values[i] -
                                                self.data[0][i]))
                        i += 1
                    result.append(result_sub)
                else:
                    print("Error vect + matrix. col matrix need == size Vect")
                    quit()
            else:
                print("Impossible vector + matrix. Dimention matrix need == 1")
                quit()
        elif isinstance(operator, Matrix):
            if self.shape == operator.shape:
                y = 0
                while y < self.shape[0]:
                    x = 0
                    while x < self.shape[1]:
                        result_sub.append(float(operator.data[y][x] -
                                                self.data[y][x]))
                        x += 1
                    result.append(result_sub)
                    result_sub = []
                    y += 1
            else:
                print("substraction between two matrix of different size")
                quit()
        else:
            print("unsupported argument for substraction")
            quit()
        return Matrix(result)

    def __truediv__(self, operator):
        result = []
        result_div = []
        if operator == 0:
            print("Zero division is imposible")
            quit()
        for y in self.data:
            for x in y:
                result_div.append(float(x / operator))
            result.append(result_div)
            result_div = []
        return Matrix(result)

    def __rtruediv__(self, operator):
        result = []
        result_div = []
        if operator == 0:
            print("Zero division is imposible")
            quit()
        for y in self.data:
            for x in y:
                if x == 0:
                    print("Zero division is imposible")
                    quit()
                result_div.append(float(operator / x))
            result.append(result_div)
            result_div = []
        return Matrix(result)

    def __mul__(self, operator):
        scalar = []
        result = 0.0
        matrice = []
        if isinstance(operator, Real):
            for y in self.data:
                for x in y:
                    scalar.append(float(operator * x))
                matrice.append(scalar)
                scalar = []
        elif isinstance(operator, Matrix):
            if self.shape[1] == operator.shape[0]:
                m = 0
                n = 0
                y = 0
                while y < self.shape[0]:
                    x = 0
                    while x < operator.shape[1]:
                        n = 0
                        m = 0
                        result = 0
                        while n < operator.shape[0]:
                            result += float(self.data[y][n] *
                                            operator.data[m][x])
                            n += 1
                            m += 1
                        scalar.append(result)
                        x += 1
                    matrice.append(scalar)
                    scalar = []
                    y += 1
            else:
                print("multiplcation between two matrix of different size")
                quit()
        elif isinstance(operator, Vector):
            if self.shape[1] == operator.size:
                x = 0
                while x < self.shape[0]:
                    n = 0
                    result = 0
                    while n < self.shape[1]:
                        result += float(self.data[x][n] * operator.values[n])
                        n += 1
                    scalar.append(result)
                    x += 1
                matrice.append(scalar)
                scalar = []
            else:
                print("Multi between vectors and matrix of different size")
                quit()
        else:
            print("unsupported argument for multiplication")
            quit()
        return Matrix(matrice)

    def __rmul__(self, operator):
        return self.__mul__(operator)

    def __str__(self):
        s = '['
        for i, val in enumerate(self.data):
            s += "{}".format(val)
            if i != self.shape[0] - 1:
                s += '\n'
        s += ']'
        return s

    def __repr__(self):
        return str(self.data)
