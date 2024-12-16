import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from io import BytesIO
import os

# Configuration de l'application Streamlit
st.set_page_config(
    page_title="Analyse acoustique",
    page_icon=":chart_with_upwards_trend:",  # Icône choisie pour l'application
    layout="centered",
    initial_sidebar_state="expanded"
)

# Configuration du titre et du sidebar
st.title("Outil interactif d'analyse acoustique")
st.sidebar.title("Configuration des paramètres")

# Ajout d'une fonctionnalité pour charger deux fichiers Excel
uploaded_file_1 = st.sidebar.file_uploader("Télécharger le premier fichier Excel", type=["xlsx"])
uploaded_file_2 = st.sidebar.file_uploader("Télécharger le deuxième fichier Excel", type=["xlsx"])

def load_data_from_excel(file):
    """
    Charge les données depuis un fichier Excel.
    """
    # Charger le fichier Excel
    df = pd.read_excel(file, sheet_name=0, header=0)  # Lire la première feuille (avec titre à la première ligne)
    
    # Extraire les fréquences (colonne A)
    frequencies = df.iloc[:, 0].dropna().values  # Fréquences dans la première colonne, ignorer les valeurs vides
    
    # Extraire les données d'absorption (toutes les autres colonnes)
    absorption_data = df.iloc[:, 1:].dropna(axis=0, how="all").values  # Retirer les lignes où toutes les valeurs sont NaN
    
    # Définir les épaisseurs et densités (exemple, à adapter selon votre fichier)
    thicknesses = np.array([10, 20, 30])  # Épaisseurs 10, 20, 30 mm
    densities = np.array([75, 110, 150])  # Densités 75, 110, 150 kg/m³
    
    return frequencies, thicknesses, densities, absorption_data

# Vérifier si les fichiers ont été téléchargés
if uploaded_file_1 is not None and uploaded_file_2 is not None:
    # Charger les données depuis les deux fichiers Excel
    frequencies_1, thicknesses_1, densities_1, absorption_data_1 = load_data_from_excel(uploaded_file_1)
    frequencies_2, thicknesses_2, densities_2, absorption_data_2 = load_data_from_excel(uploaded_file_2)
    
    # Extraire les noms des fichiers sans l'extension '.xlsx'
    file_name_1 = os.path.splitext(uploaded_file_1.name)[0]
    file_name_2 = os.path.splitext(uploaded_file_2.name)[0]
else:
    # Utilisation des données par défaut si un ou aucun fichier n'est téléchargé
    file_name_1 = "Fichier_1"
    file_name_2 = "Fichier_2"
    frequencies_1 = frequencies_2 = np.array([100, 500, 1000, 2000])
    thicknesses_1 = thicknesses_2 = np.array([10, 20, 30])
    densities_1 = densities_2 = np.array([75, 110, 150])
    absorption_data_1 = absorption_data_2 = np.array([
        [0.2, 0.4, 0.6, 0.8],
        [0.25, 0.45, 0.65, 0.85],
        [0.3, 0.5, 0.7, 0.9]
    ])

# Paramètres personnalisés via l'interface
thickness_selected = st.sidebar.selectbox(
    "Choisissez l'épaisseur (mm)",
    options=[10, 20, 30],
    index=0
)

density_selected = st.sidebar.selectbox(
    "Choisissez la densité (kg/m³)",
    options=[75, 110, 150],
    index=0
)

# Initialisation des variables d'index seulement si les fichiers sont chargés
if uploaded_file_1 is not None:
    thickness_index_1 = np.where(thicknesses_1 == thickness_selected)[0][0]
    density_index_1 = np.where(densities_1 == density_selected)[0][0]

if uploaded_file_2 is not None:
    thickness_index_2 = np.where(thicknesses_2 == thickness_selected)[0][0]
    density_index_2 = np.where(densities_2 == density_selected)[0][0]

# Extraire les données d'absorption pour la fréquence sélectionnée et l'épaisseur et densité choisies
if uploaded_file_1 and uploaded_file_2:
    absorption_curve_1 = absorption_data_1[:, thickness_index_1 * len(densities_1) + density_index_1]
    absorption_curve_2 = absorption_data_2[:, thickness_index_2 * len(densities_2) + density_index_2]
else:
    # Si un fichier est manquant, afficher un emoji "pas content" à la place du graphique
    st.warning("Veuillez charger vos fichiers Excel. Les données 'par défaut' sont utilisées.")
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.text(0.5, 0.5, "😞\nVeuillez télécharger les fichiers Excel", fontsize=30, ha='center', va='center')
    ax.axis('off')  # Désactiver les axes
    st.pyplot(fig)

# Essayer de tracer les courbes d'absorption
try:
    if uploaded_file_1 and uploaded_file_2:
        fig, ax = plt.subplots(figsize=(10, 8))

        # Changer le fond du graphique
        fig.patch.set_facecolor('#6f6f7f')  # Fond gris foncé
        ax.set_facecolor('#3f3f4f')  # Fond gris foncé pour l'axe
        ax.tick_params(axis='both', colors='white')  # Couleur des ticks en blanc

        # Tracer les courbes
        ax.plot(frequencies_1, absorption_curve_1, label=file_name_1, color="b", marker="o", markersize=6)
        ax.plot(frequencies_2, absorption_curve_2, label=file_name_2, color="r", marker="x", markersize=6)

        # Ajouter un titre et labels
        ax.set_title(f"Courbes d'absorption pour épaisseur {thickness_selected} mm et densité {density_selected} kg/m³", color='white')
        ax.set_xlabel("Fréquence (Hz)", color='white')
        ax.set_ylabel("Absorption acoustique", color='white')
        ax.legend()

        # Activer une grille
        ax.grid(True, linestyle="--", color='white', alpha=0.6)

        # Affichage du graphique dans Streamlit
        st.pyplot(fig)

except ValueError as e:
    # Gérer l'erreur sans l'afficher de façon intrusif
    st.markdown(
        f'<p style="position: fixed; bottom: 10px; right: 10px; font-size: 12px; color: red;">Erreur de dimension : {str(e)}</p>',
        unsafe_allow_html=True
    )

# Fonction pour enregistrer le graphique en PDF
def save_as_pdf(fig):
    """
    Sauvegarde le graphique actuel en PDF et le renvoie sous forme de fichier téléchargeable.
    """
    pdf_buffer = BytesIO()
    fig.savefig(pdf_buffer, format="pdf")
    pdf_buffer.seek(0)
    return pdf_buffer

# Ajouter un bouton de téléchargement
st.download_button(
    label="Télécharger la comparaison en PDF",
    data=save_as_pdf(fig),
    file_name="comparaison_acoustique.pdf",
    mime="application/pdf"
)
