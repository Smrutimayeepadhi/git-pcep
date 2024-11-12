"""travel_log = {
    "france": ["paris", "Dijon","lille"],
    "germany": ["su","berlin"],
}
print(travel_log["france"][2])"""

"""nested_list = ["a","b",["c","d"]]
print(nested_list[2][1])

nested_dictionary = {
    "France":{
        "cities_visited": ["paris", "Dijon","lille"],
        "total_visits":12
    },
"germany": {"cities_visited":["su","berlin"],
            "total_visits":7
            }
}
print(nested_dictionary["germany"]["cities_visited"][1])"""

"""Question 1:
Which line of code will change the starting_dictionary to the final_dictionary?

starting_dictionary = {
    "a": 9,
    "b": 8,
}
final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

starting_dictionary["c"] = 7
print(starting_dictionary)
Question 2:
Which line of code will produce an error?"""

dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
dict["c"] = [1,2,3]
print(dict)
dict[1] =4
print(dict)
