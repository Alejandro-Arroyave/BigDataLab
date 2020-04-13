from mrjob.job import MRJob

class SalarioPromEmpl(MRJob):

    def mapper(self, _, line):
        words = line.split(',')
        empl = words[0]
        try:
            salario = float(words[2])
        except ValueError:
            pass
        else:
            yield empl, salario

    def reducer(self, empl, salario):
        cont = 0
        suma = 0
        for i in salario:
            cont += 1
            suma += i
        yield empl, suma/cont

if __name__ == '__main__':
    SalarioPromEmpl.run()