import random

#interazione con dati, comportamento gioco,...
class Model(object):
    def __init__(self):
        self._Nmax = 100 #num max
        self._Tmax = 6 #tentativi max
        self._T = self._Tmax #tentativi rimasti
        self._segreto = None #scelto randomico quando iniziamo il gioco

    #come resettare e il gioco
    def reset(self):
        """
        Questo metodo resetta lo stato del gioco. Imposta
        il segreto ad un valore randomico fra 0 e NMax
        e ripristina il numero di tentativi rimanenti
        :return:
        """
        #setta tutte le variabili del gioco
        self._segreto = random.randint(0, self._Nmax) #segreto a valore randomico, ogni volta che chiameremo il metodo il segreto cambiera
        #riinizializzaziamo t
        self._T = self._Tmax
        print(self._segreto)

    def play(self, tentativo): #passo come parametro il mio tentativo
        """
        Questo metodo riceve come argomento un valore intero, che sara
        il tentativo del giocatore, e lo confronta con il segreto
        :return:
        -1 se il segreto è più piccolo del tentativo
        0 se il tentativo è uguale al segreto
        1 se il segreto è più grande del tentativo
        2 se non ho più tentativi disponibili
        """
        #verifico se ho ancora vite per giocare
        self._T -= 1;
        if tentativo == self._segreto:
            """ho vinto"""
            return 0
        if self._T == 0:
            """Allora non ho piu vite, non posso piu giocare"""
            return 2
        elif tentativo > self._segreto:
            """il tentativo dell'utente è piu grande del segreto"""
            return -1
        else:
            return 1

    @property
    def Nmax(self): #buon comportamento per "privatezza" _Nmax
        return self._Nmax
    @property
    def Tmax(self):
        return self._Tmax
    @property
    def T(self):
        return self._T
    @property
    def segreto(self):
        return self._segreto

if __name__ == "__main__":
    m = Model() #creo modello
    m.reset() #lo resetto
    print(m.play(10)) #faccio serie di print
    print(m.play(20))
    print(m.play(30))
    print(m.play(70))
    print(m.play(80))
    print(m.play(60))
    print(m.play(50))
