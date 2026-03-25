from view import View
from model import Model
import flet as ft
class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()
#metodi che interagiscono con view e modello

    def reset(self, e): #e è l'evento che ha generato la pressione del pulsante
        self._model.reset() #resetta lo stato del gioco lato modello
        self._view._txtT.value = self._model.T #interfaccia tra view e modello
        #resettare interfaccia grafica
        #per pulire la finestra
        self._view._lvOut.controls.clear()
        self._view._lvOut.controls.append(ft.Text("Inizia il gioco! Indovina a quale numero sto pensando..."))
        #queste righe settano l'inizio del gioco
        self._view.update()

    def play(self,e):
        #legge il tentaivo del giocatore, lo passsa al modello, prende il valore return del metodo play del modello e aggiorna l'int grafica
        tentativoStr = self._view._txtInTentativo.value
        try:
            tentativo = int(tentativoStr)
        except ValueError:
            #diciamo all'utente che ha sbaglato
            self._view._lvOut.controls.append(ft.Text("Errore, devi inserire un valore numerico"))
            self._view.update()
            return
        #se supero il try ha inserito un val numerico
        res = self._model.play(tentativo)  # in base al valore di res faccio qualcosa
        if res == 0:
            """Ho vinto"""
            self._view._lvOut.controls.append(ft.Text(f"Hai vinto. Il valore corretto era: {tentativo}", color="green"))
            self._view.update()
            return
        elif res==2:
            """Non ho piu vite """
            self._view._lvOut.controls.append(ft.Text(f"Hai perso. Il valore corretto era {self._model.segreto}"))#recuperiamo il segreto dal modello
            self._view.update() #aggiorniamo la pag
            return

        elif res==-1:
            """Allora il segreto è piu piccolo del tentativo.."""
            self._view._lvOut.controls.append(ft.Text(f"Ritenta. Il segreto è piu piccolo di {tentativo}"))
            self._view.update()
            return
        else: #res ==1
            """Allora il segreto è piu grande di tentativo"""
            self._view._lvOut.controls.append(ft.Text(f"Ritenta. Il segreto è piu grande di {tentativo}"))
            self._view.update()
            return




    def getNmax(self):
        return self._model.Nmax  #prende Nmax dal model

    def getTmax(self):
        return self._model.Tmax