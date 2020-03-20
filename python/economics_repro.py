#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:46:45 2020

@author: laura, sarah
"""
#Idee: Heterogene Agenten mit unterschiedlichem Nutzen

import numpy as np

#Hier Teil 0 des Modells: Institutionen?!
 
 # TODO CG: Die meisten Programme erlauben es automatisch nach TODOs zu suchen; hierzu einfach einen Kommentar anfangen und TODO schreiben; danach vielleicht ein Namenskürzel und die Aufgaben; ich habe alle Kommentare von mir mit TODO CG: begonnen
 # TODO CG: Ich würde mir angewöhnen nach 80 ZEichen einen Zeilenumbruch zu machen, dann ist der Code, insb. auf dem Laptop, besser lesbar (Ausnahme: TODOs)
 
class Scientific_Institutions: 
    """Governs academit power and produces network value # TODO CG: Immer gut die erste Zeile ganz kurz, und dann eine genauere Beschreibung im nächsten Absatz zu haben; das macht es neuen Leser*innen deutlich einfacher
    
    The class in which academic power and thus the network value is produced 
    and assigned to each paradigm
    
    Attributes
    ----------
    n_economists : int
        The number of economists within the Scientific_Institutions.
        
    n_paradigm : int
        The number of paradigms within the Scientific_Institutions.
    
    Methods
    --------
    academic_power
        assigns a value of academic power to each paradigm according to the 
        share of economists associated with this paradigm. For example:
        the more economists have paradigm a as current paradigm, 
        the higher is the academic power of this paradigm a.
        
    network_value
        is a square function of academic power. assigns each paradigm a network_value
    """
    def __init__(self, n_economists, n_paradigm): 
        self.n_economists = n_economists
        self.n_paradigm = n_paradigm
        self.economists = [Economists(k) for k in range(n_economists)]
        self.paradigm = [Paradigm(j) for j in range(n_paradigm)] # TODO CG würde ich anders benennen, siehe zeile 50
    
    def academic_power(self):
        #loop über paradigma/dann über Agenten 
        for paradigm in self.paradigm:  # TODO CG: um verwirrung zu vermeiden würde ich hier immer unterschiedliche Namen verwenden, also eher: for paradigm in self.paradigms (und das dann natürlich in zeile 46 auch anders nennen)
            counter = 0  
            for economist in self.economists: 
                if Economists.current_paradigm == paradigm.name: 
                    counter +=1 
            share = counter/self.n_economists
            paradigm.set_academic_power(share)      
        
    def network_value(self):
        for t in self.paradigm: 
            t.network_value = t.academic_power**4
       

#Hier Teil 1 des Modells: Die Agentenklasse
class Economists: # TODO Das wäre ein klassisches Beispiel für Code, den man in ein eigenes File packt; würde ich übrigens "Economist" nennen, ist dann einfacher Mehrzahl (bei Listen von Instanzen) und Einzahl (bei einer einzelnen Instanz) getrettn zu halten, siehe z.B. Zeile 45
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
    
    def __init__(self, name, intrinsic_value_list, n_paradigm): 
        self.name = name
        self.current_paradigm = None 
        self.intrinsic_value_list = self.set_intrinsic_value_list() # TODO CG: Siehe Kommentar unten: der Name der Funktion darf nicht gleich dem Namen des Atributs sein; streng genommen bräuchte es hier keine Methode, aber ich habe sie nur mal umbenannt damit es geht (siehe Kommentar unten); wenn ihr es aber als Funktion lassen woll, dann solltet ihr es in init als Argument rausnehmen!
        self.individul_utility_list = np.zeros(n_paradigm)

    # TODO CG: Achtung, ihr dürft eine Methode nicht so nennen wie ein Attribut. Bei euch gibt es ein Attribut "self.instrinsic_value_list" und eine Funktion mit dem gleichen Namen. Das geht nicht. Zudem solltet ihr alle Attribue möglichst schon in __init__ erstellen und dann später ändern, dann weiß man durch Blick in __init__ was die Klasse alles für Attribute hat
    # TODO CG: Damit es geht habe ich die Funktion in set_intrinsic_value_list umbenannt
    def set_intrinsic_value_list(self):
        self.instrinsic_value_list = np.random.uniform(0,1)
        
    def choose_paradigm(self):
        maximal_utility = np.argmax(self.individul_utility_list)
        self.current_paradigm = maximal_utility
    
    def get_paradigm(self):
        return self.current_paradigm

class Career(Economists): # TODO CG Solche 'Kinder' einer Klasse können entweder in das File von Economists, oder in ein separates; bei solchen kleinen Definitionen würde ich es erstmal in das gleiche File packen
    def __init__(self,carrierists, name, intrinsic_value_list, n_paradigm):
        super().__init__(self, name, intrinsic_value_list, n_paradigm)
        assert isinstance(carrierists, list)
        for m in carrierists: 
            assert isinstance(m, Economists)
            
    def utility(self, network_value_list): # TODO CG: Würde hier immer einen kurzen Docstring schreiben und das Ergebnis der Funktion explizit mit return() zurückgeben
        for i in range(len(self.individul_utility_list)): # TODO CG: hier hat die range() Funktion gefehlt; len() gibt nur eine einzige Zal aus, darüber kann man nicht loopen
            self.individul_utility_list[i] = (self.intrinsic_value_list[i])*0 + (network_value_list[i])*1 # TODO CG: was soll das Multiplizieren mit Null? Warum steht es da überhaupt?        
            
            
class Idealism(Economists): 
    def __init__(self,idealists, name, intrinsic_value_list, n_paradigm):
        super().__init__(self, name, intrinsic_value_list, n_paradigm)
        assert isinstance(idealists, list)
        for m in idealists: 
            assert isinstance(m, Economists)
            
    def utility(self, network_value_list):
        for i in range(len(self.individul_utility_list)): # TODO CG: hier wieder range() vergessen
            self.individul_utility_list[i] = (self.intrinsic_value_list[i])*1 + (network_value_list[i])*0


class The_mass(Economists): 
    def __init__(self,normals, name, intrinsic_value_list, n_paradigm):
        super().__init__(self, name, intrinsic_value_list, n_paradigm)
        assert isinstance(normals, list)
        for m in normals: 
            assert isinstance(m, Economists)
            
    def utility(self, network_value_list):
        for i in range(len(self.individul_utility_list)):  # TODO CG: hier wieder range() vergessen
            self.individul_utility_list[i] = (self.intrinsic_value_list[i])*0.4 + (network_value_list[i])*0.6
            
            
class Paradigm: # paradigmatic dominance mit network value verbinden?
    def __init__(self, name, network_value, paradigmatic_dominance): 
        self.name = name 
        #self.intrinsic_value = intrinsic_value
        self.network_value = 0 
        self.paradigmatic_dominance = 0
        
    def set_network_value(self, network_value): 
        self.network_value = network_value
    
    def set_paradigmatic_dominance(self, paradigmatic_dominance): #TODO CG: Hier wieder ein Attibut und Methode mit gleichem Namen; es ist auch noch unklar was diese Funktion machen soll
        self.paradigmatic_dominance = paradigmatic_dominance # TODO Hier ist mir nicht klar, was paradigmatic_dominance sein soll
            

##Hier beginnt Teil zwei des Codes: Das Modell - noch sehr unvollständig, viel übernommen aus tech choice model
        
class Model:
    
    """The blueprint for a single model instance.
    Attributes
    ----------
    identifier : int
        A unique identifier for this model instance.
        
    economistslist : list
        A list of the economist instances associated with the model
    
    time : int
        Current time in the model
        
    subscripts_p0 : list
        Current subscritpions for paradigm 0
        
    subscripts_p1 : list
        Current subscriptions for paradigm 1
            
    
    Methods
    --------
    
    choose_paradigm
        Economists choose one paradigm according to their individual utility
    
    run
        Runs the model, i.e. all Economists choose their paradigm sequentially.
        
    return_results
        Returns the results as a `dict`
            """
     
    def __init__(self, n_economists, identifier):
        """The __init__ method.
        Creates a list of agents and sets up the neighborhood structure.
        Parameters
        ----------
        n_economists : int
            Number of economists.
       
        identifier: int
            An identifier that uniquely identifies the model instance.
            Will be reported in the results.
        """
        self.identifier = identifier
        self.economistlist = [economist.Economist() for i in range(n_economists)] # TODO CG: da ihr das nicht über verschiedene Files gelöst habt, funktioniert das so nicht. Dazu müsstet ihr oben das Modul economist importiert haben (und dazu eine Datei economist.py in eurem Arbeitsverzeichnis haben)
        self.time = 0
        self.subscripts_p0 = [0]
        self.subscripts_p1 = [0]

            
    def run(self):
        """Runs the model.
        Shuffles the list of economists, then one economist after the other
        chooses her paradigm.
        """
        print("Start running the model!")
        np.random.shuffle(self.economistlist)
        for a in self.economistlist:
            self.time += 1
            # print(self.time, end=" ")
            a.p_choice()
            if a.get_p() == 0:
                self.subscripts_p0.append(self.subscripts_p0[-1]+1)
                self.subscripts_p1.append(self.subscripts_p1[-1])
            elif a.get_p() == 1:
                self.subscripts_p1.append(self.subscripts_p1[-1]+1)
                self.subscripts_p0.append(self.subscripts_p0[-1])
            else:
                raise SyntaxError("Something is wrong, economist does not return \
                                  paradigm!")
                
    def return_results(self):
        """Returns the results of the model as a dictionary.
        """
        result_dict = {}
        result_dict["id"] = [self.identifier] * len(self.subscripts_p0)
        result_dict["time"] = np.arange(0, len(self.subscripts_p0), 1)
        result_dict["neighborhood"] = [self.neighborhood] * len(self.subscripts_p0)
        
        result_dict["share_p0"] = [0.0] + [self.subscripts_p0[i] \
                    / (self.subscripts_p0[i] + self.subscripts_p1[i]) for \
                    i in range(1, len(self.subscripts_p0))]
        
        result_dict["share_p1"] = [0.0] + [self.subscripts_p1[i] \
                    / (self.subscripts_p0[i] + self.subscripts_p1[i]) for \
                    i in range(1, len(self.subscripts_p1))]
        return(result_dict)