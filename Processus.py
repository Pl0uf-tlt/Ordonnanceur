# Module : Processus
# But : Créer une classe processus pour faire un ordonnanceur
# Version : 0.1
# Date : 27/09/2023
# Historique 			Date 		Version 	Par
# Création du fichier 	27/09/2023	0.1			Cédric Toulotte

prioMax = 10

# Classe : process
# But : Une classe simulant un processus
# Atributs :	Nom					Type						Description
# 				Nom					Chaine de charactères		Nom du processus
# 				TpsExe				Entier						Le temps que mets le processus à s'executer
# 				TpsArr				Entier						L'instant auquel le processus arrive dans la liste d'attente
# 				TpsFin 				Entier 						L'instant auquel le processus se termine
# 				TpsSej				Entier 						Le temps qu'aura passé le processus dans l'ordonnanceur
# 				TpsAtt				Entier 						Le temps que le processus aura passé dans la liste d'attente 
# 				Prio				Entier 						La priorité du processus
# Historique 				Date 		Version 	Par
# Création de la fonction 	27/09/2023	0.1			Cédric Toulotte
class process:
	""" Une classe simulant un processus"""

	def __init__(self, Nom, TpsExe, Priorite, TpsArr):
		self.Nom = Nom
		self.TpsExe = TpsExe
		self.TpsArr = TpsArr
		self.TpsFin = -1
		self.TpsSej = -1
		self.TpsAtt = -1
		self.Prio = Priorite

L_proc = [process("P1",6,2,0),process("P2",2,4,2),process("P3",1,0,7),process("P4",5,0,0),process("P5",4,5,11),process("P6",4,1,13),process("P7",1,3,4),process("P8",3,1,8)] 
# Résultat (tpsFin) attendu P1:11, P2:22, P3:12, P4:5, P5:26, P6:19, P7:20, P8:15

L_proc2 = [process("P1",10,3,0),process("P2",1,1,5),process("P3",2,4,0),process("P4",5,2,3)]
# Résultat (tpsFin) attendu P1:10, P2:11, P3:18, P4:16

L_proc3 = [process("P1",10,3,0),process("P2",1,1,0),process("P3",5,4,0),process("P4",2,2,0)]
# Résultat (tpsFin) attendu P1:13, P2:1, P3:18, P4:3

L_proc4 = [process("P1",11,2,28),process("P2",15,4,4),process("P3",14,5,27),process("P4",9,5,27),process("P5",10,1,21),process("P6",7,2,8),process("P7",20,2,2),process("P8",6,1,3),process("P9",8,2,27),process("P10",4,2,25)] 
# Résultat (tpsFin) attendu P1:68, P2:83, P3:106, P4:92, P5:38, P6:49, P7:22, P8:28, P9:57, P10:42

L_proc5 = [process("A",10,3,2),process("B",6,5,0),process("C",2,2,5),process("D",4,1,5),process("E",8,4,3)]

