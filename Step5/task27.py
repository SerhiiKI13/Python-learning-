class MyContext:
    def __enter__(self):
        return "Python Developer"
    def __exit__(self, exc_type, exc, tb):
      pass
        
with MyContext() as role:
   print(role)