# Coding-Challenge Fall 21
# By Sashank Kannan
# Class of 2024, Sophomore, Computer Engineering
# 7 September 2021


exaggeration = ["!", "very", "quickly", "fast", "more", "power", "spring", "capital", "extremely"]

minimization = ["somewhat", "little", "indifferent","dreary", "convenience", "serenity"]

positive = [ "respect", "sensible", "excellence", "delicate", "better","pleasing", "calmly", "excellent", "wisdom", "serenity", "truth", "like", "genius", "ingenious", "prettily", "skilled", "agreeable"

negative = ["bad", "furious", "rage", "yelled", "no", "cried", "slippery", "watch", "fireman", "devil", "torrent", "unhappy", "murder", "shrieked", "folly", "inferior",]

file = open("input.txt", "r")
            
print("\nReading your input file now, Please Wait!\n")

def find_sent(to_read):

  score = 0
   finmod=1
            
            
   or x in exaggeration:
            
        if x in to_read:
            
            finmod = 2
            
            
    for x in minimization:
            
        if x in to_read:
            
            finmod = 0.5
            
            
    for x in positive:
            
        if x in to_read:
            
            score += 1*finmod
            
            finmod = 1
            
            
    for x in negative:
            
        if x in to_read:
            
            score -= 1*finmod
            
            finmod = 1
            
            
    return score

            

  wordSent = ""
            
if (find_sent(line) > 0):
            
    wordSent = "positive"
            
if (find_sent(line) == 0):
            
    wordSent = "neutral"
            
if (find_sent(line) < 0):
            
    wordSent = "negative"
            
            
print("The final score for this complete structure is:: ", find_sent(line), "(", wordSent, ")")

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
