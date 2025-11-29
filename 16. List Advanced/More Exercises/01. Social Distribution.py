population = [int(person) for person in input().split(", ")]
min_wealth = int(input())

for person in population:
    wealthiest = population.index(max(population))
    if person < min_wealth:
        index = population.index(person)
        difference = min_wealth - person
        population[index] += difference
        population[wealthiest] -= difference

if any(person < min_wealth for person in population):
    print("No equal distribution possible")
else:
    print(population)
