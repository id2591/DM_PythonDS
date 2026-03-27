def filtre_Aude(df):
    """
    Fonction pour filtrer sur le departement Aude
    """

    Aude = df[df["code_departement"] == "11"]
    return Aude
