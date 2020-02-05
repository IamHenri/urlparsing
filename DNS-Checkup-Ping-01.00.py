import subprocess
import os 											#librairie nécessaire
i = 0  												  #indice pour boucler sur le fichier
n = 0											    	#nombre de lignes du fichier initialisé
result = []											#création d'une liste vide pour stocker temporairement les urls ligne à ligne
fichier = open("domains.txt", 'r')					#stockage du contenu du fichier dans une variable en mode lecture
bilan = open("result.txt", "w")						  #valorisation des ping dans le fichier mode écriture
urls = fichier.readlines()						    	#stockage des lignes du fichier dans une variable type string
n = len(urls)	
status = 0 											            #stockage de la longueur de la liste
statustrg = str(status)
for i in range(0,n): 						        		#initialisation de la boucle
	url = urls[i]							            		#stockage un a un des urls du fichier
	status = os.system("ping " + " -n 2 " + url  )	  #ping de l'url
	if status == 0: 
		Status = "ok"
	else:
		Status = "ko"
	a = url+str(Status)+"\n"
	bilan.write(a)									          #écriture de la valeur du status dans le fichier
	i = i+1										              	#incrémentation
	print(Status, url)					        			#print du statut 
bilan.close()
