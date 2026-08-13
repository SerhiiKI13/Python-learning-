languages = {"Python", "Java", "Python", "C++", "Java", "Go"}
for l in languages:
        print(l)
        print("Python" in languages)
        print("Rust" in languages)
        languages.add("Rust")
        for l in languages:
            print(l)