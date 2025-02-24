import seaborn as sns

def filter_by_criteria(taxis, boroughs_of_interest = ['Brooklyn', 'Bronx'], favorite_color = 'yellow', distance_min = 1, distance_max = 3, total_stop = 10):
    
    
    return taxis[taxis['pickup_borough'].isin(boroughs_of_interest) 
                            & (taxis.color == favorite_color) 
                            & (taxis.total < total_stop) 
                            & (taxis.distance <= distance_max) 
                            & (taxis.distance>= distance_min) ]
    
    

taxis = sns.load_dataset('taxis')    
stats = {'max_dist': taxis['distance'].max(), 'min_dist': taxis['distance'].min()}
slice_sophisticated = filter_by_criteria(taxis)
#print(slice_sophisticated)

print(taxis['dropoff_zone'].unique())