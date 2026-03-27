from great_tables import GT


def tableau_propre(dataframe, par_dep=False):
    """
    Formatage en tableaux propre des dataframes

    par_dep=False : tableau national
    par_dep=True : tableau par département

    """

    if par_dep:
        subtitle = "Résultats des votes du premier tour par département"
        labels = dict(
            code_departement="Code departement",
            candidat="Candidat",
            voix="Nombre de votes (total)",
            pourcentage="Score (% votes exprimés)"
        )
    else:
        subtitle = "Résultats des votes du premier tour"
        labels = dict(
            candidat="Candidat",
            voix="Nombre de votes (total)",
            pourcentage="Score (% votes exprimés)"
        )

    table = (
        GT(dataframe)
        .fmt_number(columns="voix", decimals=0, sep_mark=" ")
        .fmt_percent(columns="pourcentage", decimals=2, dec_mark=",")
        .tab_header(
            title="Élections",
            subtitle=subtitle
        )
        .cols_label(**labels)
    )

    return table


def tableau_propre_2(dataframe):
    """
    Formatage en tableaux propre du df pour l'aude

    """
    table_aude2 = (
        GT(dataframe)
        .fmt_number(columns="voix_dep", decimals=0, sep_mark=" ")
        .fmt_percent(columns="pourcentage_dep", decimals=2, dec_mark=",")
        .fmt_number(columns="voix_nat", decimals=0, sep_mark=" ")
        .fmt_percent(columns="pourcentage_nat", decimals=2, dec_mark=",")
        .tab_header(
            title="Élections",
            subtitle="Résultats des votes du premier tour pour l'Aude"
        )
        .cols_label(
            code_departement="Code departement",
            candidat="Candidat",
            voix_dep="Votes par département (total)",
            pourcentage_dep="Score par departement (% votes exprimés)",
            voix_nat="Votes national (total)",
            pourcentage_nat="Score national (% votes exprimés)"
        )
    )

    return table_aude2
