from mrjob.job import MRJob

class NoSec(MRJob):

    def mapper(self, _, line):
        words = line.split(',')
        empl = words[0]
        try:
            salario = float(words[2])
        except ValueError:
            pass
        else:
            yield empl, 1

    def reducer(self, empl, values):
        yield empl, sum(values)

if __name__ == '__main__':
    NoSec.run()