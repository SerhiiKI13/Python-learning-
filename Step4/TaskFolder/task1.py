with open("read.txt","w") as file:
    file.write("Hello Python!")
    
with open("read.txt","r") as file:
    content = file.read()
print(content)