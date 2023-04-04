class Perceptron:
    def __init__(self, length, a, prog, v_type, start):
        self.vectorwag = list()
        for i in range(length):
            self.vectorwag.append(start)
        self.a = a
        self.prog = prog
        self.v_type = v_type

    def czynauczony(self, vector):
        if len(vector) != len(self.vectorwag):
            quit("Wektory i wektor wag nie sa tej samej dlugosci")
        suma = 0
        for i in range(len(vector)):
            suma += vector[i] * self.vectorwag[i]
        return suma >= self.prog

# W' = W + (d-y) * alfa * X
    def naucz(self, przewidywana, otrzymana, vector):
        rightside = (przewidywana - otrzymana)*self.a
        for i in range(len(vector)):
            vector[i] = vector[i]*rightside
        for i in range(len(vector)):
            self.vectorwag[i] += vector[i]
        self.prog += rightside*(-1)
