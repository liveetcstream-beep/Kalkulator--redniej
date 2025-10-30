"""
Kalkulator Średniej – Demo w Pythonie
Autor: dr inż. Marta Nowak
Repo: https://github.com/liveetcstream-beep/Kalkulator--redniej
Narzędzie online: https://kalkulatorsrednich.pl/
"""

def srednia_arytmetyczna(oceny):
    """
    Oblicza średnią arytmetyczną z listy ocen.
    
    Przykład:
        oceny = [4, 5, 6, 3]
        wynik = 4.5
    """
    if not oceny:
        return 0
    return sum(oceny) / len(oceny)


def srednia_wazona(oceny, wagi):
    """
    Oblicza średnią ważoną.
    
    Przykład:
        oceny = [5, 4, 6]
        wagi  = [3, 2, 1]
        wynik = 4.833
    """
    if len(oceny) != len(wagi) or not wagi:
        return 0
    return sum(o * w for o, w in zip(oceny, wagi)) / sum(wagi)


def normalizuj_wagi(wagi):
    """
    Normalizuje wagi do 100% (procentowo).
    
    Przykład:
        wagi = [2, 3, 5]
        wynik = [20.0, 30.0, 50.0]
    """
    suma = sum(wagi)
    if suma == 0:
        return [0] * len(wagi)
    return [round((w / suma) * 100, 2) for w in wagi]


# === PRZYKŁAD UŻYCIA ===
if __name__ == "__main__":
    print("=== Kalkulator Średniej – Demo ===")
    
    oceny = [5, 4, 6, 3]
    wagi = [3, 2, 1, 2]
    
    print(f"Oceny: {oceny}")
    print(f"Wagi: {wagi}")
    
    srednia_w = srednia_wazona(oceny, wagi)
    print(f"Średnia ważona: {srednia_w:.3f}")
    
    wagi_procent = normalizuj_wagi(wagi)
    print(f"Wagi po normalizacji: {wagi_procent}%")
    
    print(f"\nŚrednia arytmetyczna: {srednia_arytmetyczna(oceny):.2f}")
    
    print("\nWypróbuj online: https://kalkulatorsrednich.pl/")
