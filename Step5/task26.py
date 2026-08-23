with open("context_test.txt", "w", encoding="utf-8") as file:
        file.write("Python is awesome")

print("File closed:", file.closed)
with open("context_test.txt","r",encoding="utf-8") as file:
    reader = file.read()
    print(reader)