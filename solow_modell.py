import matplotlib.pyplot as plt
# Ökonomische Parameter 
s = 0.25
delta = 0.05
alpha = 0.33
n = 0.02 

def produktionsfunktion(k):
    y = k ** alpha 
    return y 

#startbedingungen 
k_aktuell = 1.0
zeitperioden = 50

#Das Gedächtnis: Eine Liste für den historischen Verlauf
kapital_historie = [k_aktuell]

# Die Zeitschleife (Simulation über 50 Perioden)
for jahr in range(zeitperioden):
    # 1. Aktuellen Output berechnen
    y_aktuell = produktionsfunktion(k_aktuell)

    # 2.Investitionen und effektive Abschreibungen berechnen
    investitionen = s* y_aktuell 
    effektive_abschreibungen = (delta + n) * k_aktuell

    # 3. Kapital für die nächste Periode berechnen
    k_neu = k_aktuell + investitionen - effektive_abschreibungen 
    
    # 4. Den neuen Wert im "Gedächtnis" (der Liste) speichern
    kapital_historie.append(k_neu)
    # 5. Das neue Kapital wird zur Basis für die nächste Runde 
    k_aktuell = k_neu

# analytischen steady state berechnen (Formel nach k aufgelöst)
k_steady_state = (s/(delta + n)) ** (1/(1-alpha))

# Das Ergebnis im Terminal ausgeben
print("Der berechnete Steady State liegt bei k =", k_steady_state)

# 1. Ein leeres Diagrammfenster erstellen
plt.figure(figsize=(10, 6))
# 2. Die simulierte Kurve einzeichnen (unsere Liste)
plt.plot(kapital_historie, label="Kapital pro Kopf (k)", color="blue", linewidth=2)
# 3. Den Steady State als rote, gestrichgelte Linie einzeichnen
plt.axhline(y=k_steady_state, color="red", linestyle="--", label=f"Steady State (k*)")
#4. Achsenbeschriftungen und Titel hinzufügen 
plt.title("Solow-Wachstumsmodell: Transitionspfad zum Steady State", fontsize=14)
plt.xlabel("Zeit (Jahre)", fontsize=12)
plt.ylabel("Kapital pro Kopf (k)", fontsize=12)
plt.grid(True)
plt.legend()
# 5. Das fertige Diagramm auf dem Bildschirm anzeigen
plt.show()

