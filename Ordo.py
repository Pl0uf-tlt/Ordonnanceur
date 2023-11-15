# Projet : Ordo
# But : Créer differents types d'ordonnanceurs
# Version : 0.3
# Date : 03/10/2023
# Historique 				Date 		Version 	Par
# Création du fichier 		27/09/2023	0.1			Cédric Toulotte
# Ajout des commentaires 	02/10/2023	0.1			Cédric Toulotte
# Création de triPrioExe	02/10/2023	0.2			Cédric Toulotte
# Amélioration de ordo		02/10/2023	0.2			Cédric Toulotte
# Création de l'affichage	03/10/2023	0.3			Cédric Toulotte

"""
Objectif : creer un ordonnaceur par priorité
déroulement : a chaque temps l'ordo regarde si le proc en cours 
a fini et si oui il classe les differents proc deja arrivés par priorité. 
il lance celui de plus haute prio. 
"""
import Processus as proces
import matplotlib.pyplot as plt
import numpy as np



# Fonction : triTpsArr(List_processus)
# But : Trier une liste de processus en fonction de l'instant d'arrivée
# Arguments	Nom					Type				Description
# IN : 		List_processus 		Liste de processus 	Liste des processus que l'ordonnanceur doit ordonner
# IN/OUT : 	neant
# OUT : 	List_proc 			Liste de processus	Liste des processus triés par ordre d'arrivée dans le système
# Historique 				Date 		Version 	Par
# Création de la fonction 	27/09/2023	0.1			Cédric Toulotte
def triTpsArr(List_processus):
	"""Cette fonction tri une liste de processus par ordre de temps d'arrivée décroissant"""
	nbProc = len(List_processus)
	TempsArr = [(List_processus[i].TpsArr,i) for i in range(nbProc)]
	TempsArr.sort(reverse=True)
	List_proc = [List_processus[TempsArr[j][1]] for j in range(nbProc)]
	return List_proc


# Fonction : triPrio(List_processus, tps, List_processus_prio)
# But : Tient à jour la liste d'attente des processus en prenant en compte tous les processus arrivés lors de l'appel
# Arguments Nom					Type							Description
# IN : 		List_processus		Liste de processus				Liste des processus que l'ordonnanceur doit encore ordonner
# 			tps 				Entier							Le temps actuel, tous les processus arrivés avant ce temps seront ajoutés à la liste d'attente
# 			List_processus_prio	Liste de liste de processus		Liste d'attente des processus, triés par priorité
# IN/OUT :	neant
# OUT :		neant
# Historique 				Date 		Version 	Par
# Création de la fonction 	27/09/2023	0.1			Cédric Toulotte
def triPrio(List_processus, tps, List_processus_prio):
	"""Cette fonction prends une liste de processus et un tps et ajoute tous les processus qui 
	sont arrivés dans une liste de liste triée par ordre de priorité"""
	tps_arr_proc = List_processus[-1].TpsArr
	while tps_arr_proc <= tps and len(List_processus) > 0: # Pas fonctionnel, pop une liste vide et pop la liste en entier de toute maniere, a corriger
		if len(List_processus) > 1:
			proc = List_processus.pop()
			prio_proc = proc.Prio 
			List_processus_prio[prio_proc].append(proc)
			tps_arr_proc = List_processus[-1].TpsArr
		elif len(List_processus) == 1:
			proc = List_processus.pop()
			prio_proc = proc.Prio 
			List_processus_prio[prio_proc].append(proc)


# Fonction : triPrioExe(List_processus_prio)
# But : Tri les listes de priorité par temps d'exec
# Arguments Nom					Type							Description
# IN :		List_processus_prio	Liste de liste de processus		Liste d'attente des processus, triés par priorité
# IN/OUT :	neant
# OUT :		neant
# Historique 				Date 		Version 	Par
# Création de la fonction 	02/10/2023	0.1			Cédric Toulotte
def triPrioExe(List_processus_prio):
	for i in range(len(List_processus_prio)):
		nbProc = len(List_processus_prio[i])
		TempsExe = [(List_processus_prio[i][j].TpsRestant,j) for j in range(nbProc)]
		TempsExe.sort(reverse=True)
		List_proc = [List_processus_prio[i][TempsExe[k][1]] for k in range(nbProc)]
		List_processus_prio[i] = List_proc



# Fonction : ordo(List_processus)
# But : Ordonne les processus fournis au système
# Arguments Nom					Type				Description
# IN : 		List_processus		Liste de processus	Liste des processus que l'ordonnanceur doit ordonner
# IN/OUT :	neant
# OUT :		neant
# Historique 				Date 		Version 	Par
# Création de la fonction 	27/09/2023	0.1			Cédric Toulotte
# On traite le cas ou tous	02/10/2023	0.2			Cédric Toulotte
# les processus en attente 
# ont ete executes mais il 
# en reste qui ne sont pas 
# arrives
def ordo(List_processus):
	"""Cette fonction permet d'ordonnancer les processus 
	selon leur ordre d'arrivé et leur prio"""
	nbProc = len(List_processus)
	nbProcFinis = 0
	List_processus_prio = [[] for i in range(proces.prioMax)] 
	List_processus_arr = triTpsArr(List_processus)
	tps = 0
	while nbProcFinis < nbProc :
		if len(List_processus_arr) > 0:
			triPrio(List_processus_arr, tps, List_processus_prio)
			triPrioExe(List_processus_prio)
		proc_en_cours = False
		i = 0 
		while not proc_en_cours:
			if len(List_processus_prio[i]) != 0:
				proc = List_processus_prio[i].pop()
				proc_en_cours = True
			else:
				i +=1
			if i == proces.prioMax:
				tps = List_processus_arr[-1].TpsArr
				triPrio(List_processus_arr, tps, List_processus_prio)
				triPrioExe(List_processus_prio)
				i = 0
		proc.TpsAtt = tps - proc.TpsArr
		tps += proc.TpsExe
		proc.TpsFin = tps 
		proc.TpsSej = proc.TpsFin - proc.TpsArr
		nbProcFinis += 1

# Fonction : ordo_preemptif(List_processus)
# But : Ordonne les processus fournis au système selon le principe d'un ordonnanceur preemptif par priorité
# Arguments Nom					Type				Description
# IN : 		List_processus		Liste de processus	Liste des processus que l'ordonnanceur doit ordonner
# IN/OUT :	neant
# OUT :		neant
# Historique 				Date 		Version 	Par
# Création de la fonction 	13/10/2023	0.1			Cédric Toulotte
def ordo_preemptif(List_processus):
	nbProc = len(List_processus)
	nbProcFinis = 0
	List_processus_prio = [[] for i in range(proces.prioMax)] 
	List_processus_arr = triTpsArr(List_processus)
	tps = 0
	while nbProcFinis < nbProc :
		if len(List_processus_arr) > 0 :
			triPrio(List_processus_arr, tps, List_processus_prio)
			triPrioExe(List_processus_prio)
		proc_en_cours = False
		i = 0
		while not proc_en_cours:
			if len(List_processus_prio[i]) != 0:
				proc = List_processus_prio[i].pop()
				proc_en_cours = True
				proc.TpsAtt += tps - proc.TpsPause	
			else:
				i +=1
				if i == proces.prioMax:
					tps = List_processus_arr[-1].TpsArr
					triPrio(List_processus_arr, tps, List_processus_prio)
					triPrioExe(List_processus_prio)
					i = 0
		if len(List_processus_arr) > 0:
			tpsArrProchainProc = List_processus_arr[-1].TpsArr
			tpsFinExeProcCourant = tps + proc.TpsRestant
			if tpsArrProchainProc < tpsFinExeProcCourant:
				tps = tpsArrProchainProc
				proc.TpsRestant = tpsFinExeProcCourant - tpsArrProchainProc
				proc.TpsPause = tps
				List_processus_prio[proc.Prio].append(proc)
			else:
				tps += proc.TpsRestant
				proc.TpsFin = tps 
				proc.TpsSej = proc.TpsFin - proc.TpsArr
				nbProcFinis += 1
		else:
			tps += proc.TpsRestant
			proc.TpsFin = tps 
			proc.TpsSej = proc.TpsFin - proc.TpsArr
			nbProcFinis += 1










# Fonction : affichageOrdo(List_processus)
# But : Affiche les processus et leurs ordre d'execution
# Arguments Nom					Type							Description
# IN :		List_processus		Liste de liste de processus		Liste des processus à executer puis afficher
# IN/OUT :	neant
# OUT :		neant
# Historique 				Date 		Version 	Par
# Création de la fonction 	03/10/2023	0.1			Cédric Toulotte
def affichageOrdo(List_processus):
	ordo(List_processus)
	nbrProcessus = len(List_processus)
	listNomProc = []
	listYProc = []
	fig, ax = plt.subplots()
	for i in range(nbrProcessus):
		proc = List_processus[i]
		ax.broken_barh([(proc.TpsFin-proc.TpsExe, proc.TpsExe)],(10*i,0.5))
		listNomProc.append(proc.Nom)
		listYProc.append(10*i)

	ax.set_yticks(listYProc,labels=listNomProc)
	plt.show()


# Fonction : affichageOrd2(List_processus)
# But : Affiche les processus et leurs ordre d'execution d'une autre manière
# Arguments Nom					Type							Description
# IN :		List_processus		Liste de liste de processus		Liste des processus à executer puis afficher
# IN/OUT :	neant
# OUT :		neant
# Historique 				Date 		Version 	Par
# Création de la fonction 	03/10/2023	0.1			Cédric Toulotte
def affichageOrdo2(List_processus):
	ordo(List_processus)
	nbrProcessus = len(List_processus)
	listNomProc = []
	listYProc = []
	listPoint = []
	fig, ax = plt.subplots()
	for i in range(nbrProcessus):
		proc = List_processus[i]
		y = 10*i
		x1 = proc.TpsFin - proc.TpsExe
		x2 = proc.TpsFin
		listPoint.append([x1,(x1,y),(x2,y)])
		listNomProc.append(proc.Nom)
		listYProc.append(10*i)
	listPoint.sort()
	X = []
	Y = []
	for i in listPoint:
		X.append(i[1][0])
		X.append(i[2][0])
		Y.append(i[1][1])
		Y.append(i[2][1])
	plt.plot(X,Y)
	ax.set_yticks(listYProc,labels=listNomProc)
	plt.show()






List_processus = proces.L_proc 
# affichageOrdo(List_processus)
# affichageOrdo2(List_processus)
ordo_preemptif(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))


List_processus = proces.L_proc2 
#affichageOrdo(List_processus)
# affichageOrdo2(List_processus)
ordo_preemptif(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

List_processus = proces.L_proc3 
# affichageOrdo(List_processus)
# affichageOrdo2(List_processus)
ordo_preemptif(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

List_processus = proces.L_proc4
# affichageOrdo(List_processus)
# affichageOrdo2(List_processus)
ordo_preemptif(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

List_processus = proces.L_proc5
# affichageOrdo(List_processus)
# affichageOrdo2(List_processus)
ordo_preemptif(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))













List_processus = proces.L_proc 
affichageOrdo(List_processus)
affichageOrdo2(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))


List_processus = proces.L_proc2 
affichageOrdo(List_processus)
affichageOrdo2(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

List_processus = proces.L_proc3 
affichageOrdo(List_processus)
affichageOrdo2(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

List_processus = proces.L_proc4
affichageOrdo(List_processus)
affichageOrdo2(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

List_processus = proces.L_proc5
affichageOrdo(List_processus)
affichageOrdo2(List_processus)
tmpSejMoyen = 0
tmpAttMoyen = 0
for i in range(len(List_processus)):
	proc = List_processus[i]
	print(proc.Nom,proc.TpsFin, proc.TpsSej)
	tmpSejMoyen += proc.TpsSej
	tmpAttMoyen += proc.TpsAtt
print("le temps de sejour moyen est : ", tmpSejMoyen/len(List_processus))
print("Le temps d'attente moyen est : ", tmpAttMoyen/len(List_processus))

