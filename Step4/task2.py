with open("read.txt","w") as file:
    file.write("Python")

with open("read.txt","a") as file:
    file.write("\njava")

with open("read.txt","r") as file:
    content = file.read()
print(content)