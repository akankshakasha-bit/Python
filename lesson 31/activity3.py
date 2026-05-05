class India():
    def capital(self):
        print("new delhi is the capital of India")
    def language(self):
        print("hindi is the most widely spoken language in india")
    def type(self):
        print("india is a developing country")

class USA():
    def capital(self):
        print("washington, D.C. is the capital of USA")
    def language(self):
        print("english is the primary lanaguage of USA")
    def type(self):
        print("USA is a developed country")
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()