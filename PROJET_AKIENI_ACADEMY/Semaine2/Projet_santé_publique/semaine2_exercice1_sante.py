# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 1 : Fiche Patient CHU Brazzaville
# Votre nom : KOUBATIKA Elsy Fernandez
# Date : 20/06/2026
# ============================================================
# --- SECTION 1 : VARIABLES PATIENT ---
# TODO : Declarer toutes les variables patient ci-dessous
nom_patient = "MAVOUNGOU Celestin"
age_patient = 42
sexe_patient = 'F'
departement_patient = "Brazzaville"
couverture_sociale = "CNSS"
# --- SECTION 2 : VARIABLES CONSULTATION ---
# TODO : Declarer les variables consultation
type_consultation = "Urgence"
cout_consultation_fcfa = 15000.0
nb_consultations = 1
remise_cnss_pct = 30.0
diagnostic_principal = "Paludisme grave"
# --- SECTION 3 : VARIABLES HOPITAL ---
# TODO : Declarer les variables hopital
nom_hopital = "CHU de Brazzavile"
ville_hopital = "Brazzaville"
nb_lits_total = 320
nb_lits_occupes = 284
nb_medecins_actifs = 47
# --- SECTION 4 : CALCULS ---
# TODO : Calculer le cout total apres remise CNSS
cout_total_fcfa = cout_consultation_fcfa*nb_consultations*(1-remise_cnss_pct/100)
# TODO : Calculer le taux d'occupation (en pourcentage, arrondi a 1 decimale)
taux_occupation_pct =  round(nb_lits_occupes / nb_lits_total * 100, 1)
# TODO : Calculer le ratio consultations par medecin (ce jour)
# Hypothese : 120 consultations ont eu lieu ce matin dans tout l'hopital
nb_consultations_hopital = 120
ratio_consultations_medecin = round(nb_consultations_hopital / nb_medecins_actifs, 1)
# --- SECTION 5 : AFFICHAGE ---
# TODO : Afficher une fiche complete avec f-strings

print('='*60)
print(f'FICHE PATIENT — {nom_patient}')
print('='*60)
# ... completez l'affichage
print(f'Age{'         '}: {age_patient}')
print(f'Sexe{'        '}: {sexe_patient}')
print(f'Departement{' '}: {departement_patient}')
print(f'Couverture{'  '}: {couverture_sociale}')

print('-'*60)
print("CONSULTATION")
print(f'Type{'          '}: {type_consultation}')
print(f'Diagnostic{'    '}: {diagnostic_principal}')
print(f'Cout unitaire{' '}: {cout_consultation_fcfa} FCFA')
print(f'Remise CNSS{'   '}: {remise_cnss_pct}%')
print(f'COUT TOTAL{'    '}: {cout_total_fcfa}FCFA')
print('-'*60)
print(f'HOPITAL{'         '}: {nom_hopital}')
print(f'Ville{'           '}: {ville_hopital}')
print(f'Lits occupes{'    '}: {taux_occupation_pct}%')
print(f'Medecins actifs{' '}: {nb_medecins_actifs}')
print(f'Ratio Consult{'   '}: {ratio_consultations_medecin}')
print('='*60)
print(f'STATUT: Prise en charge validee')
print('='*60)