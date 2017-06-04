#pretvaranje kilometara u milje
#milja je 0.621371 kilometara
milja = 0.621371
print "Bok"
while True:
    km=int(input("Koliko kilometara: "))
    print ("Ovo je " + str(km * milja) + " milja")
    jos= raw_input("Zelis jos? ")
    if jos != "da":
        break
print ("Kraj")





#pita korisnika zeli li jos


#ako da ponovi postupak
#ako bilo koji drugi unos prekini i zavrsi
#obavjestava korisnika da je program zavrsen
