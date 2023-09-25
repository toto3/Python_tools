# Python_tools
Code fait en python
Ce script Python untilise un .csv avec des données en input
Et génère en output un fichier .sql permettant de faire soit des Insert ou des Update
des données dans un table d'une base de données de type MySql
Et aussi de type MsAccess
# =======================================================================
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

# =======================================================================
