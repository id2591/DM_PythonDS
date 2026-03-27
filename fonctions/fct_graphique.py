import matplotlib.pyplot as plt
from cartiflette import carti_download


# Fonction Question n°7
def top5_surrepresentation(nom_candidat, dataframe, top):
    """
    Fonction pour créer un graphique sur les surreprésentations
    principales d'un candidat

    nom_candidat : le nom du candidat
    top : le nombre de barres voulues dans le graphique
    """

    # Filtre du candidat
    df = dataframe[dataframe["candidat"].str.split().str[-1] == nom_candidat.upper()].copy()

    # Mise en valeur absolue
    df["surrep_abs"] = df["surrepresentation"].abs()

    # Sélection du top n
    df_top = df.sort_values("surrep_abs", ascending=False).head(top)

    # Graphique
    plt.figure(figsize=(8, 6))
    plt.barh(df_top["code_departement"], df_top["surrepresentation"], color="steelblue")
    plt.axvline(0, color="steelblue", linewidth=1)

    plt.title(f"Top {top} des surreprésentations de {nom_candidat.upper()}")
    plt.xlabel("Surreprésentation")
    plt.ylabel("Département")

    # Inverser l’ordre (plus fort en haut)
    plt.gca().invert_yaxis()

    plt.tight_layout()
    plt.show()


# Fonction Question n°8
def initialisation_carte():
    departement_borders = carti_download(
        values=["France"],
        crs=4326,
        borders="DEPARTEMENT",
        vectorfile_format="geojson",
        simplification=50,
        filter_by="FRANCE_ENTIERE_DROM_RAPPROCHES",
        source="EXPRESS-COG-CARTO-TERRITOIRE",
        year=2022)

    departement_borders = departement_borders.rename(columns={"INSEE_DEP": "code_departement"})
    return departement_borders


# fonction restreindre
def score_candidat(nom_candidat, dataframe):
    df = dataframe[dataframe["candidat"] == nom_candidat]
    return df


def carte(nom_candidat, df):
    """
    Fonction pour créer une carte sur les surreprésentations
    d'un candidat par departement

    nom_candidat : le nom du candidat
    """

    candidat = score_candidat(nom_candidat, df)

    carte = initialisation_carte().merge(
        candidat,
        on="code_departement",
        how="left"
    )

    # Carte
    fig, ax = plt.subplots(1, 1, figsize=(10, 10))
    carte.plot(
            column="surrepresentation",
            cmap="RdBu_r",
            legend=True,
            edgecolor="black",
            linewidth=0.5,
            ax=ax
        )

    ax.set_title(f"Surreprésentation de {nom_candidat} par département", fontsize=16)
    ax.axis("off")

    plt.show()
