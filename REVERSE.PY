class Reverse:
    vowels=['a','e','i','o','u']
    sentence=" "
    reverse=" "
    vc=0

    def __init__(self,sentence):
        self.sentence=sentence
        self.reverseSentence()
    def reverseSentence(self):
        self.reverse=" ".join(reversed(self.sentence.split()))
        return self.reverse
    def vowel(self):
        self.vc=sum(s in self.vowels for s in self.sentence.lower())
        return self.vc

items=[]
for i in range(3):
    R = Reverse(input("enter string"))
    items.append(R)
    print("reversed string",R.reverse)
print("sorted in descending")
for i in sorted(items,key=lambda a: a.vowel(),reverse=True):
    print(i.reverseSentence(),"  :  ",i.vowel())

        