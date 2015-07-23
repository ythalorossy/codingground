def count_not_vowels(text):
    return len(filter(lambda x: x not in "aeiou", str(text)))

print len(filter(lambda x: x not in "aeiou", "ayetihoaulro"))

print "Luanna: ", count_not_vowels("luanna")

"""
letters =  {
    "A": "Alpha",  "B": "Bravo",   "C": "Charlie",
    "D": "Delta",  "E": "Echo",    "F": "Foxtrot",
    "G": "Golf",   "H": "Hotel",   "I": "India",
    "J": "Juliett","K": "Kilo",    "L": "Lima",
    "M": "Mike",   "N": "November","O": "Oscar",
    "P": "Papa",   "Q": "Quebec",  "R": "Romeo",
    "S": "Sierra", "T": "Tango",   "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
  }
  
def nato(word):
   return " ".join(map(lambda x: letters[x.upper()], word))
   
print nato("Banana")

print " ".join(letters[c.upper()] for c in "Banana")

"""

def sort_it(list_, n):
    if list_ == None:
        return 
    else:
        list_ = list_.split(", ")
        list_.sort(key=lambda x: x[n-1])
        return ", ".join(list_)

list_ = "cat, dog, eel, bee"

print list_
print sort_it(list_, 1)



    
