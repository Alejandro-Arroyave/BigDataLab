from mrjob.job import MRJob

class SalarioProm(MRJob):

    def mapper(self, _, line):
        words = line.split(',')
        sececon = words[1]
        try:
            salario = float(words[2])
        except ValueError:
            pass
        else:
            yield sececon, salario

    def reducer(self, sececon, salario):
        cont = 0
        suma = 0
        for i in salario:
            cont += 1
            suma += i
        yield sececon, suma/cont

if __name__ == '__main__':
    SalarioProm.run()