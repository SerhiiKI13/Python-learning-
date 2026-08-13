languages = ["Python", "Java", "JavaScript", "Python"]
unique_languages = set(languages)
list_languages = list(unique_languages)
print(list_languages)
print("Python" in list_languages)
print("Java" in list_languages)

#Task 2
coordinate = (50.45, 30.52)
print(coordinate)

#Task 3
set_languages = {"Python","Git","SQL","Python","SQL"}
for l in set_languages:
    print(l)

    print("Python" in set_languages)

    #Task 4
person ={
        "name": "Serhii",
            "age": 23,
                "city": "Torun"
                }
for key,value in person.items():
 print(f"{key}: {value}")