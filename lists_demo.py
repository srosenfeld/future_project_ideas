# Start of lesson - compare variable "name" with list "subjects"
name = "Mr. Rosenfeld"

subjects = ["English","Math","Science","History","Spanish"]

# Print each out - demonstrate how they look different
print("Hello " + name)

#print(subjects)

# ITERATION - how we print out each item (i) in a list
for i in subjects:
    print("One of my subjects is " + i)
    

# Students make their own list - sports, shows, etc.
characters = ["Harry Potter", "Hermione", "Voldemort", "Hagrid", "Ron"]

# ITERATION + CONDITIONALS
for i in characters:
    if i == "Voldemort":
        print(i + " is the villain!")
    elif i == "Harry Potter":
        print(i + " is the protagonist of his books.")
    elif i == "Hermione" or i == "Ron":
        print(i + " is one of Harry's friends.")
    else:
        print("One great character in Harry Potter is " + i)


# LOOP + ITERATION

movies = []

while True:
    print("What's one of your favorite movies? Type 'end' to quit.")
    answer = input()
    if answer == "end":
        break
    else:
        movies.append(answer)

for i in movies:
    print("One of your favorite movies is " + i)
    
    
    


















