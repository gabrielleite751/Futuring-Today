class Rodada_1(object):
    def __init__(self):
        super(Rodada_1, self).__init__()
        self.a = 0
        self.sq = 0
        self.an = 0
        self.cr = 0
        self.j = 0
        self.c = 0
        self.nsq = 0

    def append_a(self, new_value):
        self.a = new_value

    def append_sq(self, new_value):
        self.sq = new_value

    def append_an(self, new_value):
        self.an = new_value

    def append_cr(self, new_value):
        self.cr = new_value

    def append_j(self, new_value):
        self.j = new_value

    def append_c(self, new_value):
        self.c = new_value

    def append_nsq(self, new_value):
        self.nsq = new_value

    def print_states(self):
        print('Arquétipo: ', self.a, '\tStatus-Quo: ',self.sq, '\tAnimal: ', self.an, '\tCrise: ', self.cr,
              '\tJornada: ', self.j, '\tConflito: ', self.c, '\tNovo Status-Quo: ', self.nsq)







