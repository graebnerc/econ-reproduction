#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 15:46:45 2020

@author: laura, sarah
"""
#Idee: Heterogene Agenten mit unterschiedlichem Nutzen
import sys; sys.path.insert(0, './python')
import numpy as np
from economists import Economist # Wenn ihr eine andere Klasse aus diesem File verwenden wollt, müsst ihr sie explizit importieren

#Hier Teil 0 des Modells: Institutionen?!
 
 # TODO CG: Die meisten Programme erlauben es automatisch nach TODOs zu suchen; hierzu einfach einen Kommentar anfangen und TODO schreiben; danach vielleicht ein Namenskürzel und die Aufgaben; ich habe alle Kommentare von mir mit TODO CG: begonnen
 # TODO CG: Ich würde mir angewöhnen nach 80 ZEichen einen Zeilenumbruch zu machen, dann ist der Code, insb. auf dem Laptop, besser lesbar (Ausnahme: TODOs)
 
class Scientific_Institutions: 
    """Governs academit power and produces network value 
    
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
        self.paradigms = [Paradigm(
            name=j, 
            network_value=0, 
            paradigmatic_dominance=0) for j in range(n_paradigm)] 
        # TODO Über Relevanz von paradigmatic_dominance reden
        self.economists = [Economist(
            name=k, 
            intrinsic_value_list=0, 
            n_paradigm=self.n_paradigm, 
            paradigms_given=self.paradigms) for k in range(n_economists)]
    
    def update_academic_power(self):
        """Sets academic power for all paradigms.
        
        [Was ist AP und wie wird es hergestellt.
        """
        #loop über paradigma/dann über Agenten 
        for p in self.paradigms:  
            counter = 0  
            for e in self.economists: 
                if e.current_paradigm == p.name: 
                    counter +=1 
            share = counter/self.n_economists
            p.set_academic_power(share)      
        
    def network_value(self):
        for t in self.paradigms: 
            t.network_value = t.academic_power**4
       

#Hier Teil 1 des Modells: Die Agentenklasse

            
class Paradigm: # paradigmatic dominance mit network value verbinden?
    def __init__(self, name, network_value, paradigmatic_dominance): 
        self.name = name 
        #self.intrinsic_value = intrinsic_value
        self.network_value = 0 
        self.paradigmatic_dominance = 0
        self.academic_power = None
        
    def set_academic_power(self, power_value):
        """Sets academic power
        
        [extended_summary]
        
        Parameters
        ----------
        power_value : float
            The power of the paradigm, depends on the share of econs
            currently affiliated with it
        """
        self.academic_power = power_value
        
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
        self.economistlist = [Economist() for i in range(n_economists)] # TODO CG: funktioniert noch nicht, siehe oben bei den Institutionen, so müssen die Econs erstellt werden
        self.time = 0
        # TODO Hier die Listen für die Statusvariablen definieren
        self.follower_paradigm_1 = [0] # Vielleicht besser als dict?
        self.follower_paradigm_2 = [0]

            
    def run(self):
        """Runs the model.
        
        Shuffles the list of economists, then one economist after the other
        chooses her paradigm.
        """
        print("Start running the model!")
        # TODO Hier sollten wohl die Timesteps eingefügt werden
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