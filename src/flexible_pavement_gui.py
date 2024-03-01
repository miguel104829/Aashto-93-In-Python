import tkinter as tk
from tkinter import ttk
from .flexible_pavement import Flexible_Pavement

class PavimentoApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Method AASHTO")
        
        self.create_widgets()

    def create_widgets(self):
        # Create a notebook widget
        notebook = ttk.Notebook(self.master)
        notebook.pack(fill='both', expand=True)

        # Create the first tab for calculating W18
        w18_tab = ttk.Frame(notebook)
        notebook.add(w18_tab, text='Calcular W18')
        self.create_w18_widgets(w18_tab)

        # Create the second tab for calculating SN
        sn_tab = ttk.Frame(notebook)
        notebook.add(sn_tab, text='Calcular SN')
        self.create_sn_widgets(sn_tab)

    def create_w18_widgets(self, tab):
        ttk.Label(tab, text="Nivel de Confianza:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.confianza_uno_entry = ttk.Entry(tab)
        self.confianza_uno_entry.insert(0, "0.95")
        self.confianza_uno_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        
        # Etiquetas y cajas de entrada para calcular W18
        ttk.Label(tab, text="Desviación Estándar:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.desviacion_uno_entry = ttk.Entry(tab)
        self.desviacion_uno_entry.insert(0, "0.35")
        self.desviacion_uno_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(tab, text="Número Estructural:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.numero_estructural_uno_entry = ttk.Entry(tab)
        self.numero_estructural_uno_entry.insert(0, "5")
        self.numero_estructural_uno_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        ttk.Label(tab, text="ΔPSI:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.delta_psi_uno_entry = ttk.Entry(tab)
        self.delta_psi_uno_entry.insert(0, "1.9")
        self.delta_psi_uno_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(tab, text="Módulo Resiliente (MPA):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.modulo_resiliente_uno_entry = ttk.Entry(tab)
        self.modulo_resiliente_uno_entry.insert(0, "34.5")
        self.modulo_resiliente_uno_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Botón para calcular el valor de W18
        ttk.Button(tab, text="Calcular W18", command=self.calcular_w18).grid(row=5, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado de W18
        self.w18_result_label = ttk.Label(tab, text="")
        self.w18_result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def create_sn_widgets(self, tab):
        # Etiquetas y cajas de entrada para calcular SN
        ttk.Label(tab, text="Nivel de Confianza:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.confianza_entry = ttk.Entry(tab)
        self.confianza_entry.insert(0, "0.95")
        self.confianza_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(tab, text="Desviación Estándar:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.desviacion_entry = ttk.Entry(tab)
        self.desviacion_entry.insert(0, "0.35")
        self.desviacion_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(tab, text="NESE:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.W18_entry = ttk.Entry(tab)
        self.W18_entry.insert(0, "5000000")
        self.W18_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(tab, text="ΔPSI:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.delta_psi_entry = ttk.Entry(tab)
        self.delta_psi_entry.insert(0, "1.9")
        self.delta_psi_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        ttk.Label(tab, text="Módulo Resiliente (MPA):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.modulo_resiliente_entry = ttk.Entry(tab)
        self.modulo_resiliente_entry.insert(0, "34.5")
        self.modulo_resiliente_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        # Botón para calcular el valor de SN
        ttk.Button(tab, text="Calcular SN", command=self.calcular_sn).grid(row=5, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar el resultado de SN
        self.sn_result_label = ttk.Label(tab, text="")
        self.sn_result_label.grid(row=6, column=0, columnspan=2, pady=10)

    def calcular_w18(self):
        # Obtener valores de las cajas de entrada para calcular W18
        confianza = float(self.confianza_uno_entry.get())
        desviacion = float(self.desviacion_uno_entry.get())
        numero_estructural = float(self.numero_estructural_uno_entry.get())
        delta_psi = float(self.delta_psi_uno_entry.get())
        modulo_resiliente = float(self.modulo_resiliente_uno_entry.get())

         # Crear una instancia de Flexible_Pavement con los valores ingresados
        pavimento = Flexible_Pavement(Realiability=confianza,
                                      Standard_Deviation=desviacion,
                                      Structural_Number=numero_estructural,
                                      Delta_PSI=delta_psi,
                                      Mr=modulo_resiliente)
        # Calcular el valor de W18
        valor_w18 = pavimento.calcular_W18()

        # Mostrar el resultado de W18 en la interfaz
        self.w18_result_label.config(text="El valor calculado de W18 es: {:.2f}".format(valor_w18))

    def calcular_sn(self):
        # Obtener valores de las cajas de entrada para calcular SN
        confianza = float(self.confianza_entry.get())
        desviacion = float(self.desviacion_entry.get())
        delta_psi = float(self.delta_psi_entry.get())
        modulo_resiliente = float(self.modulo_resiliente_entry.get())
        W18 = float(self.W18_entry.get())

        # Crear una instancia de Flexible_Pavement con los valores ingresados
        pavimento = Flexible_Pavement(Realiability=confianza,
                                      Standard_Deviation=desviacion,
                                      W18=W18,
                                      Delta_PSI=delta_psi,
                                      Mr=modulo_resiliente)

        # Calcular el valor de SN utilizando el método Newton-Raphson
        valor_sn = pavimento.encontrar_valor_SN()

        # Mostrar el resultado de SN en la interfaz
        self.sn_result_label.config(text="El valor calculado de SN es: {:.2f}".format(valor_sn))

# Crear la aplicación
root = tk.Tk()
app = PavimentoApp(root)
root.mainloop()