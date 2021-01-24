from numpy import random as rn

Mambres = {
    1: "Zouhair Elhadiq",
    2: "Youssef Hakiki",
    3: "Ilyas zitouna",
    4: "Hamza laaydi",
    5: "Salah echorfy",
    6: "Abdelkarim",
    7: "Omar"
}
afectations = set(rn.randint(2, 8, size=20))
while len(afectations) < 6:
    r = rn.randint(2, 8)
    afectations.add(r)
