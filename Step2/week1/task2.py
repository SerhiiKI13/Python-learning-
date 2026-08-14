def create_user(name,age,city):
        return f"Name: {name}, Age: {age}, City: {city}"
result = create_user(
                     name="Serhii",
                         age=23,
                             city="Torun"    
            )
print(result)


def calculate_sum(*args):
            sum = 0
            for a in args:
                sum = sum + a
            return sum


print(calculate_sum(1, 2, 3))#6
print(calculate_sum(10, 20, 30, 40))#100

def create_profile(**kwargs):
            for k,v in kwargs.items():
                            print(f"{k}: {v}")

                            create_profile(
                                    name="Serhii",
                                                age=23,
                                                                city="Torun"
                                                                                )

def calculate_area(width:float,height:float) -> float:
            """Calculate the area of a rectangle."""
            return width * height
print(calculate_area(5, 10))
print(calculate_area.__doc__)
