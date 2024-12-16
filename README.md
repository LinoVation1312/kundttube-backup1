# Outil interactif d'analyse acoustique

## Description

Ce projet propose un outil interactif d'analyse acoustique utilisant **Streamlit**. Il permet de comparer les courbes d'absorption acoustique à partir de données contenues dans deux fichiers Excel. L'application permet à l'utilisateur de télécharger ces fichiers, de sélectionner des paramètres (épaisseur et densité), et de visualiser les courbes d'absorption sous forme de graphiques. De plus, l'utilisateur peut télécharger le graphique généré au format PDF.

## Fonctionnalités

- **Téléchargement de fichiers Excel** : Permet de télécharger deux fichiers Excel contenant des données acoustiques.
- **Sélection de paramètres** : L'utilisateur peut choisir l'épaisseur et la densité des matériaux pour ajuster les courbes d'absorption.
- **Comparaison visuelle** : Affiche les courbes d'absorption des deux fichiers Excel dans un graphique pour comparaison.
- **Téléchargement du graphique** : Permet de télécharger le graphique comparatif au format PDF.

## Prérequis

Avant de pouvoir utiliser cette application, vous devez avoir Python et les bibliothèques nécessaires installées. Les bibliothèques nécessaires sont listées dans le fichier `requirements.txt`.

### Installation des dépendances

1. Clonez ce dépôt sur votre machine :

   ```bash
   git clone https://github.com/nom-utilisateur/nom-du-depot.git


bash
Copier le code
pip install -r requirements.txt
Lancer l'application
Assurez-vous d'être dans le répertoire du projet.

Lancez l'application Streamlit avec la commande suivante :

bash
Copier le code
streamlit run app.py
L'application s'ouvrira automatiquement dans votre navigateur par défaut.

Utilisation
Télécharger les fichiers Excel : Cliquez sur les boutons "Télécharger le premier fichier Excel" et "Télécharger le deuxième fichier Excel" pour importer les données de vos fichiers Excel.

Sélectionner les paramètres : Utilisez les menus déroulants pour choisir l'épaisseur et la densité du matériau que vous souhaitez analyser.

Voir les courbes d'absorption : Les courbes d'absorption acoustique des deux fichiers seront tracées en fonction des paramètres sélectionnés.

Télécharger le graphique : Un bouton vous permet de télécharger le graphique comparatif sous forme de fichier PDF.

Structure du code
load_data_from_excel(file) : Fonction qui charge les données depuis un fichier Excel et extrait les fréquences, les épaisseurs, les densités et les coefficients d'absorption.
save_as_pdf(fig) : Fonction qui sauvegarde le graphique généré sous forme de fichier PDF.
L'application utilise Matplotlib pour générer les graphiques et Streamlit pour l'interface utilisateur interactive.
Exemple de structure des fichiers Excel
Les fichiers Excel doivent contenir les données suivantes :

La première colonne pour les fréquences (en Hz).
Les autres colonnes pour les coefficients d'absorption pour différentes combinaisons d'épaisseur et de densité.
Exemple de données dans un fichier Excel
Fréquence (Hz)	10 mm, 75 kg/m³	10 mm, 110 kg/m³	10 mm, 150 kg/m³	20 mm, 75 kg/m³	...
100	0.2	0.25	0.3	0.3	...
500	0.4	0.45	0.5	0.5	...
1000	0.6	0.65	0.7	0.7	...
Capture d'écran
Voici une capture d'écran de l'interface de l'application :


Contributions
Les contributions sont les bienvenues ! Si vous avez des suggestions ou des améliorations à proposer, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

Licence
Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.

