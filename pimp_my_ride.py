#notre liste qui contient quatre informations sur quatre voyages 
trips_to_parse = [
	"Roger 0 5 10",
	"Pongo 3 7 14",
	"Perdita 8 10 8",
	"Anita 16 3 7"
]

#fonction qui sépare nos données qui correspondent à un voyage par des virgules 
def parse_trip(trip):
    parsed_trip_list = list(trip.split(" "))
    return parsed_trip_list




#création de notre fonction qui sépare notre liste de voyage en plusieurs listes pour chaque voyage
def parse_trips(trips):
    trip_parsed = []
    for i in trips:
        trip_parsed.append(parse_trip(i))
    return trip_parsed

#on stocke le résultat de notre fonction dans une variable  our_trips_list
our_trips_list = parse_trips(trips_to_parse) 

#création de notre fonction qui additionne tous les prix des voyages
def get_trips_price(a_list_of_trips):
    prices_summed = 0
    for n in a_list_of_trips:
        prices_summed = prices_summed+int(n[-1])
    return prices_summed


#notre variable = somme de prix de voyages
all_prices_summed = get_trips_price(our_trips_list) 

# fonction qui permet de voir la compatibilité de l'heure de départ d'un voyage 2 et de l'heure d'arrivée 1
def check_compatibility(trip1, trip2):
    ended_hour_trip1=int(trip1[1])+int(trip1[2])
    start_hour_trip2=int(trip2[1])
    if start_hour_trip2 <= ended_hour_trip1:
        return False
    else : return True


def find_compatibilities(trips):
    compatibles_flights=[]
    for i in range(len(trips)):
        for j in range(len(trips)): 
            if check_compatibility(trips[i],trips[j]) == True :
                 compatibles_flights.append([trips[i],trips[j]])
    return compatibles_flights

our_compatibles_trips=find_compatibilities(our_trips_list)




# def get_best_price(trips):
#         each_prices = []
#         earnest_flights=0        
#         each_prices1=get_trips_price(trips[0])
#         each_prices2=get_trips_price(trips[1])
#         each_prices3=get_trips_price(trips[2])
#         each_prices.extend([each_prices1,each_prices2,each_prices3])
#         for i in each_prices:
#             for j in each_prices:
#                 if i > j:
#                     earnest_flights=i
#         return earnest_flights




def get_best_price(trips):
    #on instancie une liste
        each_prices = []
    #on passe à ta méthode get_trips_price chaque couple via une boucle range   
        for i in range(0,3):
            each_prices.append(get_trips_price(trips[i]))
    #on retourne le plus grand prix via la méthode max de Python
        return max(each_prices)


print(our_compatibles_trips)
print(get_best_price(our_compatibles_trips))
