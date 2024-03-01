import math
import scipy.stats as st
from .UNITS import convert

class Flexible_Pavement:

    def __init__(self, 
                 Realiability: float = 0.95, 
                 Standard_Deviation: float = 0.35, 
                 Structural_Number: float = 5, 
                 Delta_PSI: float = 1.9, 
                 Mr: float= 34.5,
                 W18: float = 5000000):
        """
        Pavimento Flexible según AASTHOO 93'
        Realiability: Nivel de Confianza del diseño por defecto es 95%
        Standar Deviation o S0: Desviación Estandar, para felxibles entre 0.45 para pavimento nuevo y 0.49 para rerehabilitación
        Structural Number o SN: Número Estructural
        Delta_PSI: Diferencia de los indices de serviciabilidad final e inicial del diseño
        Mr: Modulo resiliente de la Subrasante en MPA
        """
        self.Zr = -st.norm.ppf(Realiability)
        self.S0 = Standard_Deviation
        self.SN = Structural_Number
        self.Delta_PSI = Delta_PSI
        self.Mr = convert.MPAtoPSI(Mr)
        self.W18 = W18

    def calcular_W18(self):
        return math.pow(10,(self.Zr*self.S0+9.36*math.log10(self.SN+1)-0.20+((math.log10(((self.Delta_PSI)/(4.2-1.5))))/(0.40+(1094/math.pow(self.SN+1,5.19))))+2.32*math.log10(self.Mr)-8.07))

    def encontrar_valor_SN(self):
        # Definir la función f(SN) que quieres resolver
        def f(SN):
            return (math.pow(10, (self.Zr * self.S0 + 9.36 * math.log10(SN + 1) - 0.20 +
                                (math.log10((self.Delta_PSI) / (4.2 - 1.5))) / (0.40 + 1094 / math.pow(SN + 1, 5.19)) +
                                2.32 * math.log10(self.Mr) - 8.07)) - self.W18)

        # Definir la derivada de la función f(SN)
        def df(SN):
            h = 1e-8  # Pequeño incremento para calcular la derivada numéricamente
            return (f(SN + h) - f(SN)) / h

        # Valor inicial para el método de Newton-Raphson
        SN_inicial = 1.0  # Puedes elegir otro valor inicial según tu conocimiento del problema

        # Número máximo de iteraciones
        max_iter = 1000

        # Tolerancia para la convergencia
        tol = 1e-6

        # Método de Newton-Raphson
        for _ in range(max_iter):
            SN_nuevo = SN_inicial - f(SN_inicial) / df(SN_inicial)

            # Verificar la convergencia
            if abs(f(SN_nuevo)) < tol:
                return SN_nuevo

            SN_inicial = SN_nuevo

        # Manejo de errores si no converge
        raise ValueError("El método no converge después de {} iteraciones.".format(max_iter))




