
# 10. Pet Food Recommendation

"""
Problem: Recommend a type of pet food based on the pet's species and age.
(e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).
"""

pet_species = str(input("Enter pet species here: "))
year = int(input("Enter number of years here: "))

if pet_species == "dog":
    if year <= 2:
        print("Give puppy food")
    else:
        print("do not give puppy food")

if pet_species == "cat":
    if year >= 5:
        print("Give senior cat food")
    else:
        print("Give junior cat food")



