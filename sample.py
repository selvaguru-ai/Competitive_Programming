class string:
    def __init__(self):
        self.uppercase = 0
        self.lowercase = 0
        self.vowels = 0
        self.consonants = 0
        self.spaces = 0
        self.string = ""

    def getstr(self):
        self.string = str(input("Enter a string: "))

    def count(self):
        for ch in self.string:
            if (ch.isupper()):
                self.uppercase += 1

            if (ch.islower()):
                self.lowercase += 1

            if (ch in ('A','a','e','E','I','i','o','O','u','U')):
                self.vowels += 1
            if (ch not in ('A','a','e','E','I','i','o','O','u','U')):
                self.consonants += 1

            if (ch == " "):
                self.spaces += 1

    def display(self):
        print("The given string contains..")
        print ("%d uppercase letters"%self.uppercase)
        print ("%d lowercase letters"%self.lowercase)
        print ("%d vowels letters"%self.vowels)
        print ("%d consonants"%self.consonants)
        print ("%d spaces "%self.spaces)

s = string()
s.getstr()
s.count()
s.display()