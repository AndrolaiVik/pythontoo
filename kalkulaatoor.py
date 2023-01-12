#kalkulatsioon 
class cal():
    def __init__(self,a,b):
        self.a = a # määrab ära (a)
        self.b = b

    def liitmine(self):  # Liidab kaks sisestatud arvu
        return self.a + self.b
    def lahutamine(self):  # Lahutab kaks sisestatud arvu
        return self.a - self.b
    def korrutamine(self):  # Korrutab kaks sisestatud arvu
        return self.a * self.b
    def jagamine(self):  # Jagab kaks sisestatud arvu
        return self.a / self.b
    def jaak(self):  # Leiab Jäägi kahest sisestatud arvust
        return self.a % self.b
    def ruutjuur(self):  # Leiab Ruutjuure kahest sisestatud arvust
        return self.a ** self.b
a = int(input("Sisesta esimene number: "))  # Kasutaja sisestab numbrid
b = int(input("Sisesta teine number: "))

kalk = cal(a,b) #a ja b kalkulatsioon
while True:
    def menu():
        x = ('1. Liitmine \n2. lahutamine\n3. korrutamine\n4. jagamine\n5. Jäägi leidmine\n6. Ruutjuure leidmine. ') #Valikud kasutajale
        print(x) # prindib x, ehk Valikud kasutajale
    menu()
    valik = int(input('Sisesta üks valikutest: '))  # Kasutaja sisestab ühe valikutest
    if valik == 1: # vaatab kas valik oli sama mis kasutaja sisestas
        print("Vastus: ", kalk.liitmine())  # Prindib vastuse
        break # Lõpetab
    elif valik == 2:
        print("Vastus: ", kalk.lahutamine())
        break
    elif valik == 3:
        print("Vastus: ", kalk.korrutamine())
        break
    elif valik == 4:
        print("Vastus: ", kalk.jagamine())
        break
    elif valik == 5:
        print("Vastus: ", kalk.jaak())
        break
    elif valik == 6:
        print("Vastus: ", kalk.ruutjuur())
        break
    elif valik == 0:
        print('Sisesta uuesti üks liitmise operaator') # kasutaja peab uuesti seisestama ühe valikutest
        break






