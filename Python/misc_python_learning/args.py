def test_names_of_people(person, *people):
    print("one person name is :\n", person)
    print("more people names are as below")
    for name in people:
        print("name:",name, "\n")

test_names_of_people('abdul','rehman','ramon','eli','human','james')
