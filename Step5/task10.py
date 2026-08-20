user = {
    "name": "Serhii",
    "age": 24,
    "city": "Torun"
}

extra = {
    "job": "Python Developer",
    "country": "Poland"
}
profile = {**user, **extra}
print(profile)