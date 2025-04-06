def annee_temperature_minimale(t_moy, annees):
    min_t = t_moy[0]
    min_a = 0
    for t, a in zip(t_moy, annees):
        if t <= min_t:
            min_t = t
            min_a = a

    return (min_t, min_a)

t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]

print(annee_temperature_minimale(t_moy, annees))
