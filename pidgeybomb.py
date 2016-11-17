#This program calculates how many Pokemons you need to catch in order to do
# a chosen number of evolutions based on how many candy and Pokemon you
# currently have.
#It assumes that all Pokemon caught after you've caught the number you want to
# evolve will be transferred.

#This section gathers input used in the calculations.
monster=str(input("Enter the name of the Pokemon you want to evolve: "))
evo_candy=int(input("Enter the number of " + str(monster) + " candy needed for one evolution: "))
candy=int(input("Enter the number of " + str(monster) + " candy you currently have: "))
poke=int(input("Enter the number of " + str(monster) + " you have: "))
evo=int(input("Enter the number of evolutions you want to do: "))

#This part is used to calculate the total number of candy you need to do however
# many evolutions you want to do.
#It takes into condsideration the candy you gain for evolving each pokemon minus
# the final evolution.
evo_bonus=evo-1
candy_needed=(evo*evo_candy)-evo_bonus

#This section is used to initialize variables in the loop.
new_catches=0
tot_poke=poke+new_catches

#This loop repeats for every Pokemon you need to catch up until the number of
# candy you have is equal to or greater than the number of candy you need
# to complete the evolutions specified.
while candy <= candy_needed:
    
#This nested loop is repeated until the number of pokemon you have is equal to
# the number you want to evolve. This means you are not transferring them and
# they are netting you three candy per catch.
    while evo > tot_poke:
        new_catches=new_catches + 1
        candy=candy + 3
        tot_poke=poke+new_catches

#The rest of the loop is repeated for every Pokemon you catch after you have
# already caught the amount you want to evolve. It assumed that these excess
# Pokemons are all being transferred and net you 4 candy.
    new_catches=new_catches + 1
    candy=candy + 4

print ("You need to catch", new_catches, "more " +str(monster) + " to do", evo, "evolutions.")

