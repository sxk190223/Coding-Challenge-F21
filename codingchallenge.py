# Coding-Challenge Fall 21
# By Sashank Kannan
# Class of 2024, Sophomore, Computer Engineering
# 7 September 2021

# keywords for determining sentiment
positive = ["pleasing", "calmly", "excellent", "wisdom", "serenity", "truth", "like", "genius", "ingenious", "prettily", "skilled", "agreeable", "respect", "sensible", "excellence", "delicate", "better"]

negative = ["bad", "furious", "rage", "yelled", "no", "cried", "slippery", "watch", "fireman", "devil", "torrent", "unhappy", "murder", "shrieked", "folly", "inferior",]

exaggeration = ["!", "very", "quickly", "fast", "more", "power", "spring", "capital", "extremely"]

minimization = ["somewhat", "little", "indifferent", "observant","dreary", "convenience", "serenity"]

file = open("input.txt", "r")
line = file.read()
line = line.lower()
print("\nInput file read; string initialized... \n")

def find_sent(to_read):

  score = 0
    m = 1
    # calculate score based off keywords
    f
    or x in exaggeration:
        if x in to_read:
            m = 2
            
    for x in minimization:
        if x in to_read:
            m = 0.5
    for x in positive:
        if x in to_read:
            score += 1*m
            m = 1
    for x in negative:
        if x in to_read:
            score -= 1*m
            m = 1
    return score


  direction = ""
if (find_sent(line) > 0):
    direction = "positive"
if (find_sent(line) == 0):
    direction = "neutral"
if (find_sent(line) < 0):
    direction = "negative"
print("The final score for this complete structure is:: ", find_sent(line), "(", direction, ")")

print("\nPlease wait, we are currently scanning the rest.\n")
sentences = line.split(".")
prev_end = 0
out_index = 0
for num in range(len(sentences)):
    out_index += 1
    a = sentences[num]
    print("The final score for this sentence text ", out_index, " is:: ", find_sent(a))

print("\n Thank you! Closing file now.")
file.close()
print("\nEnding program.")
