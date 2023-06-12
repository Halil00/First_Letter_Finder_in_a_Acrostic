class Dosya2():

    def __init__(self):

        with open("example_acrostic.txt", "r", encoding="utf-8") as file:

            satirlar = file.readlines()

            
            bas_harfler = file.readline()
            self.satirlar_liste = list()

            for i in satirlar:
                self.satirlar_liste.append(i)
            print(self.satirlar_liste)

            for i in self.satirlar_liste:
                print(i[0])
            

dosya2 = Dosya2()














