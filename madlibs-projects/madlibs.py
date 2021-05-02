# string concatination
## we're going to create a string that says "subscribe to _______"
# youtuber = "Kylie Ying" # some variable

# there are a few ways to do this:
## print ("subscribe to " + youtuber)
## print ("subscribe to {}".format(youtuber))
## print (f"subscribe to {youtuber}")

adj = input("adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
i love to {verb1} . Stay Hydrated and {verb2} like you are a {famous_person}!"

print(madlib)

