from Week_8.guitars import Guitar

guitars = []
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

print("These are my guitars: ")

for i, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""

    print("Guitar {}: {:>20} ({}, worth ${:10,.2f} {})".format(i + 1, guitar.name, guitar.year, guitar.price,
                                                               vintage_string))
