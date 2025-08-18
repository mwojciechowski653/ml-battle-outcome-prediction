# IO_projekt1

## Opis projektu

Projekt **IO_projekt1** to jeden z dwóch projektów przygotowanych w języku Python jako zaliczenie przedmiotu **Inteligencja Obliczeniowa**, który miałem na czwartym semestrze studiów I stopnia na kierunku **Informatyka o profilu praktycznym**. Obejmował on między innymi zagadnienia związane ze współczesnym rozwojem sztucznej inteligencji, przede wszystkim: algorytmy klasyfikacyjne, trenowanie sieci neuronowych, sieci generatywne GAN oraz duże modele językowe (w skrócie z ang. LLM).

Celem projektu jest porównanie skuteczności takich metod jak:

- Naiwny klasyfikator Bayesa (`Naive Bayes`)
- K najbliższych sąsiadów (`KNN`)
- Drzewo decyzyjne (`Decision Tree`)
- Sieci neuronowe (`Neural Networks`)

Oraz dodatkowo:

- Wpływ redukcji wymiarów (`PCA`) na skuteczność ww. metod
- Przeprowadzenie normalizacji danych

Projekt zawiera również system do generowania danych wejściowych (bitew), przechowywania wyników oraz wizualizacji skuteczności klasyfikatorów.

## Koncept gry oraz struktura danych do badań

Punktem wyjścia tego projektu był plik `bitwa.py` który zawiera grę napisaną przeze mnie na pierwszym semestrze studiów. Nie jest on idealny, natomiast jako urozmaicenie (i utrudnienie) postanowiłem trzymać się zasady, aby ten kod był "nietykalny", co miało symulować scenariusz z wykorzystaniem zewnętrznego kodu. Sama gra to bardziej rozbudowana wersja klasycznego _kamień, papier, nożyce_, gdzie możemy wystawić trzy rodzaje jednostek - _piechurzy_, _konnica_ lub _artylerzysci_ na pole bitwy - po jednym rodzaju na każde skrzydło (lewe skrzydło, centrum lub prawe skrzydło). Jednostki mają różną cenę oraz różne współczynniki walki między sobą. Po określeniu poziomu trudności (wybraniu jak duży budżet mamy w porównaniu do przeciwnika) losowana jest armia przeciwnika, następnie możemy dokonać zwiadu za odpowiednią opłatą, aby podejrzeć wybrane skrzydło/a przeciwnika. Później wybieramy typ jednostek oraz ich liczebność na każde skrzydło. Walka przebiega przez roztrzyganie osobno, kolejno lewego skrzydła, prawego skrzydła, a na końcu walki w centrum, gdzie brane pod uwagę (z odpowiednim bonusem za flankowanie) są pozostałości z walk na skrzydłach. Przy każdej walce losowany jest pseudolosowy współczynnik, tak żeby wyniki nie były w pełni przewidywalne. Jeśli wygraliśmy, obliczany jest końcowa punktacja na podstawie tego, ile jednostek oraz jego typu nam zostało. Wynik zapisywany jest wraz z imieniem/nickem w pliku o nazwie `wynikiGraczy.txt`.

Projekt to analiza różnych algotytmów klasyfikacyjnych i porównanie ich skuteczności na przygotowanych przeze mnie danych. Dane zostały wygenerowane za pomocą pliku `generatorBitw.py` i zapisane w pliku `rozgrywki.txt`. Każda rozgrywka zapisana jest w 13 kolumnach, gdzie kolejno w 6 kolumnach podane są typy jednostek oraz ich liczebność dla "gracza", a później, w kolejnych 6 dla "przeciwnika". Ostatnia kolumna to wynik bitwy (jako 0 lub 1), informujące czy w takim ustawieniu armii, bez pseudolosowych współczynników (będących elementem prawdziwej rozgrywki) armia "gracza" wygrywa.

## Struktura katalogu

```
IO_projekt1/
├── wykresy/                          # Katalog z wykresami wyników klasyfikatorów
├── badania/                          # Folder zawierający pliki analizujące klasyfikatory
│   ├── BayesBadania.py               # Badanie skuteczności klasyfikatora Bayesa
│   ├── KNNBadania.py                 # Testowanie klasyfikatora KNN
│   ├── drzewoDecyzyjneBadania.py     # Badania nad drzewem decyzyjnym
│   ├── funkcjeRobocze.py             # Funkcje pomocnicze (np. normalizacja, PCA)
│   ├── sieciNeuronoweBadania.py      # Badanie klasyfikatora opartego na sieciach neuronowych
│   ├── pcaBadania.py                 # Analiza PCA i utraty % wariancji
│   └── normalizacjaBadania.py        # Normalizacja danych wejściowych
├── bitwa.py                          # Logika symulacji pojedynczej bitwy
├── generatorBitw.py                  # Generator danych (bitew) na potrzeby klasyfikacji
├── main.py                           # Menu - zagranie w grę lub wygenerowanie danych
├── rozgrywki.txt                     # Dane wejściowe zawierające scenariusze bitew
├── wynikiGraczy.txt                  # Zapis wyników uzyskanych przez graczy
├── requirements.txt                  # Wymagania i zależności potrzebne do uruchomienia projektu
├── IO1_Bitwa.pdf                     # Dokumentacja projektu i przedstawienie wyniku badań (PDF)
└── LICENSE                           # Licencja projektu

```

## Wymagania

Projekt wymaga Pythona 3.7 lub nowszego oraz następujących bibliotek:

- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

Instalacja:

```bash
pip install -r requirements.txt
```

## Uruchomienie

1. Sklonuj repozytorium:

```bash
git clone https://github.com/mwojciechowski653/IO_projekt1.git
cd IO_projekt1
```

2. Uruchom środowisko wirtualne (opcjonalnie):

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. Uruchom główny skrypt aby zagrać lub wygenerować nowe rekordy do badań:

```bash
python main.py
```

Alternatywnie, uruchamiaj konkretne badania pojedynczo:

```bash
python KNNBadania.py
python BayesBadania.py
```

Kod plików zawierających badania może zawierać zakomentowany kod analizujący inne, konkretne scenariusze. Aby zadziałał należy odkomentować odpowiedni blok kodu i zakomentować poprzedni scenariusz. Scenariusze są od siebie niezależne i można uruchamiać kilka w ramach jednego uruchomienia.

## Wizualizacja wyników

Każdy moduł badawczy tworzy wykresy, które dla podanych w repozytorium danych, zostały zapisane w katalogu `wykresy/`. Przykładowo:

- `PCA` pokazuje ile % wariancji zostaje zachowane przy liczbie `x` zachowanych kolumn.
- `PCA - drzewo decyzyjne` pokazuje wpływ redukcji liczby kolumn na precyzję klasyfikatora: drzewa decyzyjnego.

## Dokumentacja

Plik `IO1_Bitwa.pdf` zawiera opis projektu, założenia jakie określiłem przed przystąpieniem do badań oraz przedstawienie wyników i wniosków.

## Autor

- **Marcin Wojciechowski**  
  [GitHub](https://github.com/mwojciechowski653)

## Licencja

Projekt jest udostępniany na licencji **MIT**.  
Pełny tekst licencji znajdziesz w pliku [LICENSE](LICENSE).

W skrócie: możesz używać, kopiować, modyfikować i rozpowszechniać ten kod na warunkach MIT. Oprogramowanie dostarczane jest „tak jak jest”, bez żadnych gwarancji.
