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
h1_nom = 'CHU Brazzaville'
h1_ville = 'Brazzaville'
h1_departement = 'Brazzaville'
h1_type = 'CHU'
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47

h1_nb_infirmiers = 123
h1_nb_rupture = 2
h1_nb_alertes = 2
h1_population_zone = 1800000
h1_niveau_triage_occupation = " "
h1_niveau_alerte_global = " "
# Hopital 2 — Hopital General Pointe-Noire

h2_nom = "Hopital Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Pointe-Noire"
h2_type = "Hopital General"

h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 95
h2_nb_rupture = 0
h2_nb_alertes = 1
h2_population_zone = 1200000
h2_niveau_triage_occupation = " "
h2_niveau_alerte_global = " "

# Hopital 3 — Hopital de Dolisie

h3_nom = "Hopital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hopital Regional"

h3_nb_lits = 95
h3_nb_lits_occupes = 91
h3_nb_medecins = 8
h3_nb_infirmiers = 60
h3_nb_rupture = 1
h3_nb_alertes = 2
h3_population_zone = 500000
h3_niveau_triage_occupation = " "
h3_niveau_alerte_global = " "
# Hopital 4 — Hopital de district Owando

h4_nom = "Hopital d'Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "District"

h4_nb_lits = 45
h4_nb_lits_occupes = 32
h4_nb_medecins = 3
h4_nb_infirmiers = 40
h4_nb_rupture = 3
h4_nb_alertes = 0
h4_population_zone = 250000
h4_niveau_triage_occupation = " "
h4_niveau_alerte_global = " "
# Hopital 5 — Centre de sante Impfondo

h5_nom = "CMS de Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de sante"
h5_nb_rupture = 2
h5_nb_alertes = 1
h5_nb_lits = 20
h5_nb_lits_occupes = 19
h5_nb_medecins = 1
h5_nb_infirmiers = 30

h5_population_zone = 150000
h5_niveau_triage_occupation = " "
h5_niveau_alerte_global = " "

# === SECTION D : CALCULS D'INITIALISATION ===================
# TODO : Calculer les KPIs globaux initiaux

# Population totale couverte
population_totale = (h1_population_zone + h2_population_zone + h3_population_zone + h4_population_zone + h5_population_zone)

nb_hopitaux_critiques = 0
total_ruptures = 0

# Taux occupation moyen
h1_taux_occupation =  round(h1_nb_lits_occupes / h1_nb_lits * 100, 1)
h2_taux_occupation =  round(h2_nb_lits_occupes / h2_nb_lits * 100, 1)
h3_taux_occupation =  round(h3_nb_lits_occupes / h3_nb_lits * 100, 1)
h4_taux_occupation =  round(h4_nb_lits_occupes / h4_nb_lits * 100, 1)
h5_taux_occupation =  round(h5_nb_lits_occupes / h5_nb_lits * 100, 1)


report = [(h1_nom, h1_taux_occupation, h1_niveau_triage_occupation, h1_niveau_alerte_global, h1_nb_rupture, h1_nb_alertes, h1_nb_medecins),
          (h2_nom, h2_taux_occupation, h2_niveau_triage_occupation, h2_niveau_alerte_global, h2_nb_rupture, h2_nb_alertes, h2_nb_medecins),
          (h3_nom, h3_taux_occupation, h3_niveau_triage_occupation, h3_niveau_alerte_global, h3_nb_rupture, h3_nb_alertes, h3_nb_medecins),
          (h4_nom, h4_taux_occupation, h4_niveau_triage_occupation, h4_niveau_alerte_global, h4_nb_rupture, h4_nb_alertes, h4_nb_medecins),
          (h5_nom, h5_taux_occupation, h5_niveau_triage_occupation, h5_niveau_alerte_global, h5_nb_rupture, h5_nb_alertes, h5_nb_medecins)]


#taux_occupation_moyen = (total_lits_occupes / total_lits) * 100

# === SECTION E : RAPPORT D'INVENTAIRE =======================

print("="*60)
print("TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE")
print("Date : 16 janvier 2026 | Pour le Conseil des Ministres")
print("="*60)

print(f"{'HOPITAL':<25} {'OCCUPATION':<15} {'ALERTES':<10} {'NIVEAU GLOBAL'}")
print()

for hopital, taux_occupation, niveau_triage_occupation, niveau_alerte_global, nb_rupture, nb_alertes, nb_medecins in report:
    
    # Niveau occupation
    if taux_occupation > 95:
        niveau_triage_occupation = "[CRI]"
    elif taux_occupation > 85:
        niveau_triage_occupation = "[ALT]"
    else:
        niveau_triage_occupation = "[OK ]"
        
    # Niveau global
    if nb_rupture >= 2 or taux_occupation > 95:
        niveau_alerte_global = "[CRITIQUE]"
        nb_hopitaux_critiques += 1
    elif nb_rupture >= 1 or taux_occupation > 85 or (nb_alertes >= 2 and nb_medecins < 5):
        niveau_alerte_global = "[PREOCCUPANT]"
    else:
        niveau_alerte_global = "[SATISFAISANT]"
        
    # Total national ruptures
    total_ruptures += nb_rupture
    
    print(
        f"{hopital:<26}"
        f"{taux_occupation}% "
        f"{niveau_triage_occupation:<9} "
        f"{nb_rupture}R + {nb_alertes}{'A':<4} "
        f"{niveau_alerte_global}"
    )
    
print("-"*60)

print(f"{nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
print(f"{total_ruptures} ruptures de stock identifiees a l'echelle nationale")


# Recommandation automatique

if nb_hopitaux_critiques >= 3:
    recommandation = "Mobiliser la reserve nationale PNA"
elif total_ruptures >= 5:
    recommandation = "Renforcer les commandes urgentes"
else:
    recommandation = "Surveillance reguliere"

print("RECOMMANDATION PRIORITAIRE :", recommandation)

print("="*60)

