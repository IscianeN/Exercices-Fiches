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

# stocker dans des variables chaque ligne de voyages de our_trips_list

our_trip1=our_trips_list[0]
our_trip2=our_trips_list[1]
our_trip3=our_trips_list[2]
our_trip4=our_trips_list[3]


# fonction qui permet de voir la compatibilité de l'heure de départ d'un voyage 2 et de l'heure d'arrivée 1
def check_compatibility(trip1, trip2):
    ended_hour_trip1=int(trip1[1])+int(trip1[2])
    start_hour_trip2=int(trip2[1])
    if start_hour_trip2 <= ended_hour_trip1:
        return False
    else : return True

#appel et test de notre fonction sur trois structures : ça marche !!
print(check_compatibility(our_trip1,our_trip4))
print(check_compatibility(our_trip1,our_trip2))




    

