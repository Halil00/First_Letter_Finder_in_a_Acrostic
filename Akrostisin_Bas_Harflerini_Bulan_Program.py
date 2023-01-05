class Dosya2():

    def __init__(self):

        with open("şiir.txt", "r", encoding="utf-8") as file:

            satirlar = file.readlines()

            #Bas harfler işime yarar diye koydum fakat ihtiyacım olmadı. Bununla lineları okuyup da bastırılabilir 2. bir seçenek olarak, o yüzden burada bıraktım.
            bas_harfler = file.readline()
            self.satirlar_liste = list()

            for i in satirlar:
                self.satirlar_liste.append(i)
            print(self.satirlar_liste)

            for i in self.satirlar_liste:
                print(i[0])

















            

dosya2 = Dosya2()














