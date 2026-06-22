# ============================================================
# MODULE FONDATEUR — Projet Sante Publique / Akieni Academy
# Ce fichier centralise toutes les constantes et variables metier
# Il sera enrichi chaque semaine jusqu'a S24
# ============================================================
# === SECTION A : CONSTANTES NATIONALES ET NORMES OMS ========
TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0
SEUIL_OMS_DENSITE_MEDICALE = 2.3 # medecins pour 1000 habitants
SEUIL_OMS_COUVERTURE_VACCIN = 95.0 # pourcentage minimum OMS

SEUIL_MORTALITE_ALERTE = 2.0 # % deces / hospitalisations
SEUIL_RUPTURE_STOCK_JOURS = 30 # jours minimum de stock
DEPARTEMENTS_CONGO = [ # 12 departements officiels
 'Brazzaville', 'Pointe-Noire', 'Bouenza', 'Cuvette',
 'Cuvette-Ouest', 'Kouilou', 'Lekoumou', 'Likouala',
 'Niari', 'Plateaux', 'Pool', 'Sangha'
]
# === SECTION B : VARIABLES DES 5 HOPITAUX ===================
# Hopital 1 — CHU de Brazzaville
h1_nom = 'CHU de Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1800000
#Hopital 2 

h2_nom = 'Hopital General Pointe-Noire'
h2_ville = 'Pointe-Noire'
h2_departement = 'Pointe-Noire'
h2_type = ''
h2_nb_lits = 320
h2_nb_lits_occupes = 284
h2_nb_medecins = 47
h2_nb_infirmiers = 123
h2_population_zone = 1800000

#Hopital 3

h3_nom = 'Hopital de Dolisie'
h3_ville = 'Dolisie'
h3_departement = 'Bouenza'
h3_type = ''
h3_nb_lits = 320
h3_nb_lits_occupes = 284
h3_nb_medecins = 47
h3_nb_infirmiers = 123
h3_population_zone = 1_800_000

#Hopital 4

h4_nom = 'Hopital de district Owando'
h4_ville = 'Owando'
h4_departement = 'Niari'
h4_type = ''
h4_nb_lits = 320
h4_nb_lits_occupes = 284
h4_nb_medecins = 47
h4_nb_infirmiers = 123
h4_population_zone = 1_800_000

#Hopital 5

h5_nom = 'Centre de sante de Impfondo'
h5_ville = 'Impfondo'
h5_departement = ''
h5_type = 'CHU'
h5_nb_lits = 320
h5_nb_lits_occupes = 284
h5_nb_medecins = 47
h5_nb_infirmiers = 123
h5_population_zone = 1_800_000
# ... (completer pour les 4 autres hopitaux)
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================

# TODO : Declarer les 5 medicaments essentiels
# === SECTION D : CALCULS D'INITIALISATION ===================
# TODO : Calculer les KPIs globaux initiaux
# === SECTION E : RAPPORT D'INVENTAIRE =======================