import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCreaGrafo(self,e):
        pass

    def handleCercaRaggiungibili(self,e):
        pass

    def loadFermate(self, dd: ft.Dropdown()):
        fermate = self._model.fermate

        if dd.label == "Stazione di Partenza":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(text=f.nome,
                                                     key=f.id_fermata))
            dd.on_change = self.read_DD_Partenza
        elif dd.label == "Stazione di Arrivo":
            for f in fermate:
                dd.options.append(ft.dropdown.Option(text=f.nome,
                                                     key=f.id_fermata))
            dd.on_change = self.read_DD_Arrivo

    def read_DD_Partenza(self,e):
        key = e.control.value
        self._fermataPartenza = next((f for f in self._model.fermate if f.id_fermata == key), None)
        print(f"Fermata di partenza selezionata: {self._fermataPartenza}")

    def read_DD_Arrivo(self,e):
        key = e.control.value
        self._fermataArrivo = next((f for f in self._model.fermate if f.id_fermata == key), None)
        print(f"Fermata di partenza selezionata: {self._fermataArrivo}")
