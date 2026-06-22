# ============================================================
# PROJET SANTE PUBLIQUE - ANALYSE DES HOPITAUX DU POOL
# ============================================================


# ============================================================
# CONSTANTES METIER
# ============================================================

COUT_MEDECIN_TRIMESTRE = 1200000.0

SEUIL_MORTALITE_ALERTE = 2.0      # %
SEUIL_DENSITE_ALERTE = 0.05       # medecins pour 1000 habitants



# ============================================================
# DONNEES HOPITAL DISTRICT KINKALA

h1_nom = "Hopital District Kinkala"

h1_budget = 12500000.0
h1_consultations = 1847
h1_hospitalisations = 312
h1_deces = 8

h1_lits_totaux = 45
h1_lits_occupes = 41

h1_medecins = 3
h1_population = 85000



# ============================================================
# DONNEES CMS VINDZA

h2_nom = "CMS de Vindza"

h2_budget = 6800000.0
h2_consultations = 923
h2_hospitalisations = 87
h2_deces = 2

h2_lits_totaux = 20
h2_lits_occupes = 14

h2_medecins = 1
h2_population = 42000



# ============================================================
# DONNEES HOPITAL KINDAMBA

h3_nom = "Hopital de Kindamba"

h3_budget = 9200000.0
h3_consultations = 1234
h3_hospitalisations = 201
h3_deces = 11

h3_lits_totaux = 35
h3_lits_occupes = 33

h3_medecins = 2
h3_population = 67000



# ============================================================
# FONCTION DE CALCUL DES INDICATEURS


def calculer_kpi(budget, consultations, hospitalisations, deces, lits_totaux, lits_occupes, medecins, population):
    
    patients_total = consultations + hospitalisations
    cout_moyen_patient = budget / patients_total
    taux_occupation = (lits_occupes / lits_totaux) * 100


    densite_medicale = (medecins / population) * 1000
    taux_mortalite = (deces / hospitalisations) * 100


    return (round(cout_moyen_patient, 2), round(taux_occupation, 2), round(densite_medicale, 2), round(taux_mortalite, 2))



# ============================================================
# CALCUL KPI POUR CHAQUE STRUCTURE


h1_cout_patient, h1_occupation, h1_densite, h1_mortalite = calculer_kpi(
    h1_budget,
    h1_consultations,
    h1_hospitalisations,
    h1_deces,
    h1_lits_totaux,
    h1_lits_occupes,
    h1_medecins,
    h1_population
)

h2_cout_patient, h2_occupation, h2_densite, h2_mortalite = calculer_kpi(
    h2_budget,
    h2_consultations,
    h2_hospitalisations,
    h2_deces,
    h2_lits_totaux,
    h2_lits_occupes,
    h2_medecins,
    h2_population
)


h3_cout_patient, h3_occupation, h3_densite, h3_mortalite = calculer_kpi(
    h3_budget,
    h3_consultations,
    h3_hospitalisations,
    h3_deces,
    h3_lits_totaux,
    h3_lits_occupes,
    h3_medecins,
    h3_population
)



# ============================================================
# DETECTION HOPITAL CRITIQUE
# ============================================================


hopitaux = [

   (
        h1_nom,
        h1_mortalite,
        h1_densite
    ),

    (
        h2_nom,
        h2_mortalite,
        h2_densite
    ),

    (
        h3_nom,
        h3_mortalite,
        h3_densite
    )

]

hopitaux_critiques = []

for nom, mortalite, densite in hopitaux:

    if (mortalite > SEUIL_MORTALITE_ALERTE or densite < SEUIL_DENSITE_ALERTE):
        hopitaux_critiques.append(nom)

# ============================================================
# BONUS : ANALYSE BUDGET MEDECINS
# ============================================================

budget_total = (h1_budget + h2_budget + h3_budget)
medecins_actuels = (h1_medecins + h2_medecins + h3_medecins)
objectif_medecins = 5 * 3
medecins_a_recruter = (objectif_medecins - medecins_actuels)
cout_recrutement = (medecins_a_recruter *COUT_MEDECIN_TRIMESTRE)
budget_suffisant = budget_total >= cout_recrutement



# ============================================================
# RAPPORT CONSOLIDE MINISTRE
# ============================================================


print("=" * 65)
print("RAPPORT CONSOLIDE - SYSTEME DE SANTE DU POOL")
print("=" * 65)

def afficher_hopital(nom, cout, occupation, densite, mortalite ):
    print(f"""{nom}Cout moyen par patient : {cout:,.2f} FCFA
        Taux occupation lits    : {occupation:.2f} %
        Densite medicale        : {densite:.2f} medecin / 1000 habitants
        Taux mortalite          : {mortalite:.2f} % """)


afficher_hopital(h1_nom, h1_cout_patient, h1_occupation, h1_densite, h1_mortalite)
afficher_hopital(h2_nom,h2_cout_patient,h2_occupation,h2_densite,h2_mortalite)
afficher_hopital(h3_nom,h3_cout_patient,h3_occupation,h3_densite,h3_mortalite)



print("=" * 65)

if len(hopitaux_critiques) > 0:
    print("ALERTE : Hopitaux en situation critique")
    for hopital in hopitaux_critiques:
        print(f"- {hopital}")
else:
    print("Aucun hopital n'est en situation critique.")


print("=" * 65)
print("ANALYSE RENFORCEMENT MEDICAL")
print("=" * 65)

print(f"Budget total disponible                    : {budget_total:,.2f} FCFA")
print(f"Cout pour atteindre 5 medecins par hopital : {cout_recrutement:,.2f} FCFA")



if budget_suffisant:
    print("Le budget permet de recruter les medecins necessaires.")
else:
    print("Le budget actuel est insuffisant pour atteindre l'objectif.")

print("=" * 65)