# Pakomāta Sūtījumu Sistēma
Šī Python programma modelē **pakomāta sūtījumu apstrādi**.  
Tā ļauj izveidot dažādus sūtījumu veidus (parastus, trauslus un vērtīgus), aprēķināt to cenas, salīdzināt sūtījumus un iegūt kopējo cenu.

## Funkcionalitāte
- **Abstraktā klase `Sutijums`** – definē kopīgās īpašības un metodes visiem sūtījumiem.
- **`ParastsSutijums`** – cena atkarīga tikai no izmēra.
- **`TrauslsSutijums`** – cena = pamattarifs + iepakojuma maksa.
- **`VertigsSutijums`** – cena = pamattarifs + sūtījuma vērtība.
- **`Pakomats`** – glabā sūtījumus, aprēķina kopējo cenu, filtrē trauslos sūtījumus un izvada informāciju.

## Izmantošanas piemērs
### Ievads:
```python
#Izveidot pakomatu
pakomats = Pakomats()

# Izveidot sūtijumus
s1 = ParastsSutijums("Jānis Bērziņš", 2.5, 'M')
s2 = TrauslsSutijums("Anna Kalniņa", 1.0, 'S', 2.0)
s3 = VertigsSutijums("Pēteris Ozols", 0.8, 'L', 300)

#Pievienot sūtijumus pakomātam
pakomats.pievienot_sutijumu(s1)
pakomats.pievienot_sutijumu(s2)
pakomats.pievienot_sutijumu(s3)

#Izvadīt sūtijumus
pakomats.paradit_visus()

#Izvadīt sūtijuma kopējo cenu
print("Kopējā cena:", pakomats.aprekina_kopējo_cenu(), "€")

#Salīdzināt sūtijumus
print("Vai s1 ir lētāks par s2?", s1 < s2)

#Filtrēt trauslos sūtijumus
print("Trauslie sūtījumi:")
for t in pakomats.filtre_trauslos():
    print(t, "Cena:", t.aprekinat_cenu(), "€")
```
### Izvads:
```python
Adresāts: Jānis Bērziņš, svars: 2.5 kg, izmērs: M, cena: 4.0 €
Adresāts: Anna Kalniņa, svars: 1.0 kg, izmērs: S, cena: 4.0 €
Adresāts: Pēteris Ozols, svars: 0.8 kg, izmērs: L, cena: 306.0 €
Kopējā cena: 314.0 €
Vai s1 ir lētāks par s2? False
Trauslie sūtījumi:
Adresāts: Anna Kalniņa, svars: 1.0 kg, izmērs: S, cena: 4.0 € Cena: 4.0 €
```

## Prasības
Python 3.8 vai jaunāka versija
Nav ārēju bibliotēku atkarību
