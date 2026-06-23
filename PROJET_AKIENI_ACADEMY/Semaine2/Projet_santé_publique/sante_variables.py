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
# Hopital 2 — Hopital General Pointe-Noire

h2_nom = "Hopital General Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Pointe-Noire"
h2_type = "Hopital General"

h2_nb_lits = 250
h2_nb_lits_occupes = 210
h2_nb_medecins = 35
h2_nb_infirmiers = 95

h2_population_zone = 1200000


# Hopital 3 — Hopital de Dolisie

h3_nom = "Hopital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hopital Regional"

h3_nb_lits = 180
h3_nb_lits_occupes = 145
h3_nb_medecins = 22
h3_nb_infirmiers = 60

h3_population_zone = 500000

# Hopital 4 — Hopital de district Owando

h4_nom = "Hopital de district Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "District"

h4_nb_lits = 120
h4_nb_lits_occupes = 90
h4_nb_medecins = 12
h4_nb_infirmiers = 40

h4_population_zone = 250000

# Hopital 5 — Centre de sante Impfondo

h5_nom = "Centre de sante de Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de sante"

h5_nb_lits = 80
h5_nb_lits_occupes = 60
h5_nb_medecins = 8
h5_nb_infirmiers = 30

h5_population_zone = 150000

# ... (completer pour les 4 autres hopitaux)
# === SECTION C : VARIABLES DES 5 MEDICAMENTS ================
# TODO : Declarer les 5 medicaments essentiels
# Medicament 1

med1_nom = "Artemether-Lumefantrine"
med1_quantite_disponible = 5000
med1_seuil_rupture = 1000
med1_cout_unitaire = 2500.0

# Medicament 2

med2_nom = "Amoxicilline"
med2_quantite_disponible = 8000
med2_seuil_rupture = 1500
med2_cout_unitaire = 1200.0

# Medicament 3

med3_nom = "Paracetamol"
med3_quantite_disponible = 12000
med3_seuil_rupture = 3000
med3_cout_unitaire = 500.0

# Medicament 4

med4_nom = "SRO"
med4_quantite_disponible = 6000
med4_seuil_rupture = 1000
med4_cout_unitaire = 700.0

# Medicament 5

med5_nom = "Vaccin antipaludeen"
med5_quantite_disponible = 3000
med5_seuil_rupture = 500
med5_cout_unitaire = 8500.0

# === SECTION D : CALCULS D'INITIALISATION ===================
# TODO : Calculer les KPIs globaux initiaux

# Population totale couverte
population_totale = (
    h1_population_zone +
    h2_population_zone +
    h3_population_zone +
    h4_population_zone +
    h5_population_zone)

# Nombre total médecins
total_medecins = (
    h1_nb_medecins +
    h2_nb_medecins +
    h3_nb_medecins +
    h4_nb_medecins +
    h5_nb_medecins)

# Densité médicale nationale
densite_medicale = (total_medecins / population_totale) * 1000

# Taux occupation moyen
total_lits = (
    h1_nb_lits +
    h2_nb_lits +
    h3_nb_lits +
    h4_nb_lits +
    h5_nb_lits)

total_lits_occupes = (
    h1_nb_lits_occupes +
    h2_nb_lits_occupes +
    h3_nb_lits_occupes +
    h4_nb_lits_occupes +
    h5_nb_lits_occupes)

taux_occupation_moyen = (total_lits_occupes / total_lits) * 100

# Valeur totale stock médicaments
valeur_stock_total = (
    med1_quantite_disponible * med1_cout_unitaire +
    med2_quantite_disponible * med2_cout_unitaire +
    med3_quantite_disponible * med3_cout_unitaire +
    med4_quantite_disponible * med4_cout_unitaire +
    med5_quantite_disponible * med5_cout_unitaire)
# === SECTION E : RAPPORT D'INVENTAIRE =======================

print("="*60)
print(" RAPPORT INITIAL SYSTEME DE SANTE - CONGO ")
print("="*60)

print("KPI NATIONAUX")

print(f"Densite medicale               : {densite_medicale:.2f} medecins / 1000 habitants")

print(f"Taux occupation moyen          : {taux_occupation_moyen:.2f}%")

print(f"Valeur totale stock medicaments: {valeur_stock_total:,.2f} FCFA")

print("="*60)
print("ETAT DES HOPITAUX")
print("="*60)

print(f"{h1_nom}\t\n  Lits: {h1_nb_lits}  Occupes: {h1_nb_lits_occupes}  Medecins: {h1_nb_medecins}")

print(f"{h2_nom}\t\n  Lits: {h2_nb_lits}  Occupes: {h2_nb_lits_occupes}  Medecins: {h2_nb_medecins}")

print(f"{h3_nom}\t\n  Lits: {h3_nb_lits}  Occupes: {h3_nb_lits_occupes}  Medecins: {h3_nb_medecins}")

print(f"{h4_nom}\t\n  Lits: {h4_nb_lits}  Occupes: {h4_nb_lits_occupes}  Medecins: {h4_nb_medecins}")

print(f"{h5_nom}\t\n  Lits: {h5_nb_lits}  Occupes: {h5_nb_lits_occupes}  Medecins: {h5_nb_medecins}")

print("="*60)
print("INVENTAIRE MEDICAMENTS")
print("="*60)

medicaments = [(med1_nom, med1_quantite_disponible, med1_seuil_rupture),
    (med2_nom, med2_quantite_disponible, med2_seuil_rupture),
    (med3_nom, med3_quantite_disponible, med3_seuil_rupture),
    (med4_nom, med4_quantite_disponible, med4_seuil_rupture),
    (med5_nom, med5_quantite_disponible, med5_seuil_rupture)]


for nom, stock, seuil in medicaments:
    etat = "OK"
    if stock <= seuil:
        etat = "ALERTE RUPTURE"
    print(f"{nom}\t\n  Stock: {stock} Seuil: {seuil} Etat: {etat}")
    
print("="*60)