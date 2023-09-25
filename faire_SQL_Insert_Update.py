#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict

#=======================================================================
#Script programmé par Pascal Audet pour le LEMP  en août 2019 
#modification en octobre 2019
#Pour fabriquer un fichier SQL INSERT INTO  Ou UPDATE
#modification en novembre 2019 
#Pour ajouter la possibilité de faire les Update pour MsAcess

#a partir d'un fichier csv ayant les données dans les colonnes

# ==POUR INSERT =======
#ex: Info1	Info2	999	Infofinal
#vers INSERT INTO bidon (Info1,Info2,UnNombre,Infofinal)VALUES("Info1","Info2",999,"Infofinal");
# ======= QUOI FAIRE ?? ======
#INPUT = un fichier csv délimité par des TAB
#PARAMETRES = Nom de la table, liste de champs, 
#AJUSTEMENT DU CODE = ajuster la section dans le while pour avoir les lignes 
#             correspondantes au contenu du .csv avec les bons types de
#             données de la table  INT ou VARCHAR
#			+','+Type_Format(line[1],"INT")\
#			+','+Type_Format(line[2],"VARCHAR")\

# ==POUR UPDATE =======
#ex: ID	Similarity	Critere
#vers UPDATE cas  set Similarity="92",Critere="N/A" Where ID=454;
# ======= QUOI FAIRE ?? ======
#INPUT = un fichier csv délimité par des TAB
#PARAMETRES = Nom de la table, liste de champs, 
# il faut modifier  le dictionnaire listeChampsUpdate
# pour refléter les colonnes du fichier csv en input
# le format (key,value) est ici (Nom du champ dans la table , type du champ)
# le premier élément du Dict  sera dans le where du la ligne de Update 
# exemple de syntax :listeChampsUpdate = OrderedDict([("ID", "INT"), ("Similarity", "VARCHAR"), ("Critere", "VARCHAR") ]) 

#=======================================================================

class faireSQL:
	def __init__(self,nomfichierInput,nomfichierOutput,nomtable,listeChamps,listeChampsUpdate):
		self.nomfichier=nomfichierInput
		self.nomfichierOutput=nomfichierOutput
		self.nomtable=nomtable
		self.listeChamps=listeChamps
		self.STR_INSERT="INSERT INTO "+self.nomtable+" "+self.listeChamps+""
		#pour update
		self.STR_UPDATE="UPDATE "+self.nomtable+" "
		self.listeChampsUpdate=listeChampsUpdate



	def faire_INSERT(self):
		f=open(self.nomfichier)
		f_out=open(self.nomfichierOutput,"w+")
		#f_out.write("TRUNCATE TABLE "+self.nomtable+";\n") #commenter si non désiré
		line=f.readline() #commenter si il n'ya pas de ligne de nom de colonne dans le fichier input'
		line=f.readline()
		while line !='':
			line=line.replace("\n","")
			line=line.replace("\r","")
			line=line.replace("\"","_")
			line=line.split("	")
			LigneREQ=self.STR_INSERT+' VALUES('\
			+''+Type_Format(line[0],"VARCHAR")\
			+','+Type_Format(line[1],"VARCHAR")\
			+','+Type_Format(line[2],"INT")\
			+');'
			LigneREQ=LigneREQ.replace("\t","")
			f_out.write(LigneREQ+"\n")
			line=f.readline()
		f.close()
		f_out.close()



	# fait 2 loop imbriquées  : loop 1-dans le fichier csv de données ; loop 2-dans le dictionnaire de liste de champ
	def faire_UPDATE(self):
		f=open(self.nomfichier)
		f_out=open(self.nomfichierOutput,"w+")
		line=f.readline() #commenter si il n'ya pas de ligne de nom de colonne dans le fichier input'
		line=f.readline()
		while line !='': #loop 1
			line=line.replace("\n","")
			line=line.replace("\r","")
			line=line.replace("\"","_")
			line=line.split("	")
			LigneREQ=self.STR_UPDATE+' set '
			indexChamp=0
			separateur=","
			for  champ, tipe in self.listeChampsUpdate.items(): #loop 2
				if len(self.listeChampsUpdate)==(indexChamp+1):
					separateur=""#au dernier élément il n y a pas de séparateur
				if indexChamp==0:
					LEWHERE=" Where "+ champ+"="+Type_Format(line[0],tipe)+';'
				if indexChamp>0:
					LigneREQ=LigneREQ+champ+"="\
					+Type_Format(line[indexChamp],  tipe) + separateur
				indexChamp=indexChamp+1
			LigneREQ=LigneREQ.replace("\t","")
			LigneREQ=LigneREQ + LEWHERE
			#f_out.write(LigneREQ+"\n")#Utilisez l'autre ligne si c'est pour MsAcces
			f_out.write('sql="'+LigneREQ.replace("\"","'")+'"\nDoCmd.RunSQL sql\n')#Pour MSACCES seulement
			line=f.readline()
		f.close()
		f_out.close()

def Type_Format(champ,choix):
	if (choix=="INT"):return ''+champ+''
	if (choix=="VARCHAR"):return '"'+champ+'"' 
	return ''+champ+''
#===========================================
#         PROGRAMME PRINCIPAL
#===========================================

nomtable="lesClusters"
fichierInput="cluster_couleur.csv"

nomtable="ENTRYTABLE"
fichierInput="BDLemp_cluster_sscluster_r129.csv"

nomtable="tbl_cas"
fichierInput="BDLemp_Modif_RASPE_divulgation.csv"

FaireUn="UPDATE" #UPDATE ou INSERT

if (FaireUn=="INSERT"):
	listeChamps="(NoSeq1,NoSeq2,Similitude)"
	fichierOutput="Insert_"+nomtable+".sql"
	unSQL = faireSQL(fichierInput,fichierOutput,nomtable,listeChamps,"")
	unSQL.faire_INSERT()

if (FaireUn=="UPDATE"):
	listeChampsUpdate = OrderedDict([#(key,valeur) ici (nom du champ de la table , type de donné du champ)
	                             ("KEY", "VARCHAR"),
                                 ("IdProjetCle", "VARCHAR"), # le premier de la liste sera dans le where 
                                 ("ProjetCle", "VARCHAR"),
                                 ("DivulgationCle", "VARCHAR"),
                                 ("FlagModif", "VARCHAR")
                                ])
	fichierOutput="Update_"+nomtable+"_Modif_RASPE_divulgation.sql"
	unSQL = faireSQL(fichierInput,fichierOutput,nomtable,"",listeChampsUpdate)
	unSQL.faire_UPDATE()




