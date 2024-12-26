

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

travel_log = {
    "France" : {
        "cities" : ['paris', 'lyon','Marseille'],
        "times_visited" : 8,
    },
    "Germany" : {
        "cities" : ['Berlin', 'Hamburg', 'Frankfurt'],
        "times_visited" : 5,
    },
}

print(travel_log["France"]["cities"][1])