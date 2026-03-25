import flet as ft

class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2024 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None

    def caricaInterfaccia(self): #dobbiamo modificare questo metodo
        #avremo tutte le definizione dei text field, pulsanti, caselle di testo...
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._txtNmax = ft.TextField(label= "Numero max",
                                     value=self._controller.getNmax(),
                                     disabled=True) # devo chiedere al controller perche view e model non possono comunicare
        #label è l'etichetta della casella di testo, disabled per rendere text field non editabile
        #nome che inizia con txt è un campo di testo

        self._txtTmax = ft.TextField(label= "Numero tentativi massimo",
                                     value= self._controller.getTmax(),
                                     disabled=True)
        self._txtT = ft.TextField(label= "Tentativi rimanenti",
                                  disabled=True)
        #i tre oggetti precedenti servono per dire lo stato del gioco all'utente

        self._row1 = ft.Row(controls = [self._txtNmax,self._txtTmax, self._txtT])

        #ora devo fare i due pulsante, uno che richiama play uno che richiama reset
        self._txtInTentativo = ft.TextField(label= "Valore")
        self._btnReset = ft.ElevatedButton(text = "Nuova partita",
                                           on_click=self._controller.reset) #reset e NON reset() perche devo passare nome del metodo e non la chiamata al metodo
        self._btnPlay = ft.ElevatedButton(text = "Indovina",
                                          on_click=self._controller.play)
        #ora scriviamo questi metodi nel controller
        #poi aggiungiamo questi pulsanti su una nuova riga

        self._row2 = ft.Row(controls = [self._txtInTentativo,self._btnReset, self._btnPlay])

        #creo contenitore all'interno del quale stamperemo diverse stringhe
        self._lvOut = ft.ListView(expand=True)

        self._page.add(self._row1, self._row2, self._lvOut) #per aggiungere e  aggioranare pagina
        #dobbaimo scrivire reset e play nel controller

        self._page.update()

    def setController(self,controller):
        #dice a view questo è il tuo controller e viceversa.
        self._controller = controller

    def update(self):
        self._page.update() #aggiorna l'interfaccia grafica