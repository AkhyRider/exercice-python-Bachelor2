def covertir_note(texte):
    try:
        texte_propre = texte.strip().replace(",", ".")
        return float(texte_propre)
    except ValueError:
        return None
        def moyenne(valeurs):
            return sum(valeurs)/len(valeurs)
            def mention(moyenne):
                if moyenne >= 16:
                    return "excellent"
                elif moyenne >= 14:
                    return "bien"
                elif moyenne >= 12:
                    return "assez bien"
                elif moyenne >= 10:
                    return "moyen"
                else:
                    return "insuffisant"
                    

