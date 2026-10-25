def fullName (name:str, surname:str)->str:
    concat = name + " " + surname
    return(f"Cześć {name} {surname}!")


greeting = fullName ("Patryk", "Dąbek")
print(greeting)