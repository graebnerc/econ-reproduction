import numpy as np

class Economist: # TODO Das wäre ein klassisches Beispiel für Code, den man in ein eigenes File packt; würde ich übrigens "Economist" nennen, ist dann einfacher Mehrzahl (bei Listen von Instanzen) und Einzahl (bei einer einzelnen Instanz) getrettn zu halten, siehe z.B. Zeile 45
    """A single economist
    
    Chooses a paradigm, depending on own preferences and academic power expressed in network value.
    
    Attributes
    ----------
    academic power : set
        Academic power of a paradigm relevant for the technology choice of this agent.
        
    current_paradigm : int
        The paradigm chosen by the agent. `None` in the beginning, then 0 or 1
    
    network_value : set
        correlates with academic power of a paradigm
        
    paradigmatic_dominance : set
        assigns a value to a paradigm according to its academic power- in relation to other's paradigms' academic power
    
    individul_utility : list
        
    
    Methods
    --------
    intrinsic_value_list
        assigns randomly generated values as intrinsic values to a paradigm for each economist
        
    choose_paradigm
        Chooses a technology based on own preferences and academic power of a paradigm (and association to a certain 
        subclass of economists)
        
    get_paradigm
        Returns the chosen paradigm.
    
    utility
        calculates the individual utility for each subclass of Economists as a sum = k*intrinsic_value + l*network value.
        Each subclass has a specified k and j.
    """
    
    def __init__(self, name, intrinsic_value_list, n_paradigm, paradigms_given): 
        self.name = name
        self.current_paradigm = None 
        self.intrinsic_value_list = {} # TODO Ist ein dict, evtl. also umbenennen
        for p in paradigms_given:
            self.intrinsic_value_list[str(p.name)] = np.random.uniform(0,1)
        self.individul_utility_list = np.zeros(n_paradigm)
       
    def choose_paradigm(self):
        maximal_utility = np.argmax(self.individul_utility_list)
        self.current_paradigm = maximal_utility
    
    def get_paradigm(self):
        return self.current_paradigm

class Career(Economist): # TODO CG Solche 'Kinder' einer Klasse können entweder in das File von Economists, oder in ein separates; bei solchen kleinen Definitionen würde ich es erstmal in das gleiche File packen
    def __init__(self,carrierists, name, intrinsic_value_list, n_paradigm):
        super().__init__(self, name, intrinsic_value_list, n_paradigm)
        assert isinstance(carrierists, list)
        for m in carrierists: 
            assert isinstance(m, Economists)
            
    def utility(self, network_value_list): # TODO CG: Würde hier immer einen kurzen Docstring schreiben und das Ergebnis der Funktion explizit mit return() zurückgeben
        for i in range(len(self.individul_utility_list)): # TODO CG: hier hat die range() Funktion gefehlt; len() gibt nur eine einzige Zal aus, darüber kann man nicht loopen
            self.individul_utility_list[i] = (self.intrinsic_value_list[i])*0 + (network_value_list[i])*1 # TODO CG: was soll das Multiplizieren mit Null? Warum steht es da überhaupt?        
            
            
class Idealism(Economist): 
    def __init__(self,idealists, name, intrinsic_value_list, n_paradigm):
        super().__init__(self, name, intrinsic_value_list, n_paradigm)
        assert isinstance(idealists, list)
        for m in idealists: 
            assert isinstance(m, Economists)
            
    def utility(self, network_value_list):
        for i in range(len(self.individul_utility_list)): # TODO CG: hier wieder range() vergessen
            self.individul_utility_list[i] = (self.intrinsic_value_list[i])*1 + (network_value_list[i])*0


class The_mass(Economist): 
    def __init__(self,normals, name, intrinsic_value_list, n_paradigm):
        super().__init__(self, name, intrinsic_value_list, n_paradigm)
        assert isinstance(normals, list)
        for m in normals: 
            assert isinstance(m, Economists)
            
    def utility(self, network_value_list):
        for i in range(len(self.individul_utility_list)):  # TODO CG: hier wieder range() vergessen
            self.individul_utility_list[i] = (self.intrinsic_value_list[i])*0.4 + (network_value_list[i])*0.6
            