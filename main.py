from dataclasses import dataclass

@dataclass
class Foydalanuvchi_profili:
    username: str
    email: str
    parol: str
    oxirgi_kirish_vaqti: int

    def parol_uzunlligi(self):
        return len(self.parol) >= 8


v = Foydalanuvchi_profili("baxtbek", "bjbj.gmail.com", "123456789", 18)
print(v.parol_uzunlligi())

@dataclass
class mahsulot:
    nom: str
    son: int
    narx: int

    def umumiyqiymat(self):
        return self.son * self.narx

s = mahsulot("paket", 900, 1000)
print(s.umumiyqiymat())
