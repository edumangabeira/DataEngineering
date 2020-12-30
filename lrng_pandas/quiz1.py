import pandas as pd


planets = ['Earth', 'Saturn', 'Venus', 'Mars', 'Jupiter']
distance_from_sun = [149.6, 1433.5, 108.2, 227.9, 778.6]
dist_planets = pd.Series(data=distance_from_sun, index=planets)
time_light = dist_planets.values / 18
print(pd.Series(data=time_light, index=planets))


close_planets = time_light[time_light < 40]
print(close_planets)
