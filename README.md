# ML Battle Outcome Prediction

> Polish version below / Wersja polska poniżej

## Project Description

The **ml-battle-outcome-prediction** project is one of two projects developed in Python as part of the **Computational Intelligence** course I took during the fourth semester of my Bachelor’s studies in **Computer Science (practical profile)**. It covered topics related to modern AI development, including classification algorithms, neural network training, generative adversarial networks (GANs), and large language models (LLMs).

The goal of the project is to compare the effectiveness of methods such as:

- Naive Bayes Classifier (`Naive Bayes`)
- K-Nearest Neighbors (`KNN`)
- Decision Tree (`Decision Tree`)
- Neural Networks (`Neural Networks`)

Additionally:

- The impact of dimensionality reduction (`PCA`) on the effectiveness of these methods
- Data normalization

The project also includes a system for generating input data (battles), storing results, and visualizing classifier performance.

## Game Concept and Data Structure for Research

> Note: The report, file names and code are in Polish, as this project was originally created for a university course.

The starting point of this project was the `bitwa.py` file, which contains a game I wrote during my first semester. It is not perfect, but as an additional challenge I decided to keep this code "untouchable" to simulate working with external code. The game is an extended version of the classic _rock, paper, scissors_, where you can deploy three types of units - _infantry_, _cavalry_, or _artillery_ - on the battlefield, one type for each wing (left wing, center, or right wing). Units have different costs and combat effectiveness against each other. After selecting the difficulty level (determining how large our budget is compared to the opponent’s), the opponent’s army is randomly generated. You can then perform reconnaissance for a fee to peek at selected wings of the opponent. Afterwards, you choose the type and number of units for each wing. The battle unfolds separately: left wing, right wing, and finally the center, where the remnants from the wings (with flanking bonuses) are considered. A pseudorandom coefficient is drawn in each fight, making outcomes not fully predictable. If you win, the final score is calculated based on the remaining units and their types. The result is saved along with the player’s name/nickname in `wynikiGraczy.txt`.

The project analyzes different classification algorithms and compares their effectiveness on prepared data. The data was generated using `generatorBitw.py` and saved in `rozgrywki.txt`. Each battle is stored in 13 columns: the first 6 represent the unit types and their counts for the “player”, the next 6 for the “opponent”. The last column is the battle outcome (0 or 1), indicating whether the player’s army would win in this configuration without the pseudorandom factors (which are part of real gameplay).

## Directory Structure

```
IO_projekt1/
├── src/                                  # Folder with whole project
│   ├── badania/                          # Folder with classifier analysis scripts
│   │   ├── BayesBadania.py               # Naive Bayes classifier performance analysis
│   │   ├── KNNBadania.py                 # KNN classifier testing
│   │   ├── drzewoDecyzyjneBadania.py     # Decision tree analysis
│   │   ├── funkcjeRobocze.py             # Helper functions (e.g., normalization, PCA)
│   │   ├── sieciNeuronoweBadania.py      # Neural network-based classifier analysis
│   │   ├── pcaBadania.py                 # PCA analysis and variance retention
│   │   └── normalizacjaBadania.py        # Data normalization
│   ├── bitwa.py                          # Single battle simulation logic
│   ├── generatorBitw.py                  # Data generator (battles) for classification
│   ├── main.py                           # Menu – play the game or generate data
│   ├── requirements.txt                  # Project dependencies
│   ├── rozgrywki.txt                     # Input data containing battle scenarios
│   └── wynikiGraczy.txt                  # Player results storage
├── wykresy/                              # Directory with classifier performance plots
├── IO1_Bitwa.pdf                         # Project documentation and research results (PDF)
└── LICENSE                               # Project license
```

## Requirements

The project requires Python 3.7 or newer and the following libraries:

- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

Installation:

```bash
pip install -r requirements.txt
```

## Running

1. Clone the repository:

```bash
git clone https://github.com/mwojciechowski653/IO_projekt1.git
cd IO_projekt1
```

2. Create a virtual environment (optional):

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```

3. Run the main script to play the game or generate new records for research:

```bash
python src/main.py
```

Alternatively, run specific research scripts individually:

```bash
python src/KNNBadania.py
python src/BayesBadania.py
```

The research scripts may contain commented-out code for analyzing specific scenarios. To enable them, uncomment the relevant block and comment out the previous one. Scenarios are independent and can be run in the same session.

## Results Visualization

Each research module generates plots, which for the provided data are saved in the `wykresy/` directory. For example:

- `PCA` shows the percentage of variance retained depending on the number of columns preserved.
- `PCA - Decision Tree` shows the impact of dimensionality reduction on decision tree precision.

## Documentation

The `IO1_Bitwa.pdf` file contains a project description, assumptions I made before starting the research, as well as results and conclusions.

## Author

- **Marcin Wojciechowski**
  [GitHub](https://github.com/mwojciechowski653)

## License

This project is licensed under the **MIT** license.
The full license text can be found in the [LICENSE](LICENSE) file.

In short: you are free to use, copy, modify, and distribute this code under the MIT terms. The software is provided “as is”, without any warranty.

---

# ML Battle Outcome Prediction wersja po polsku

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

Punktem wyjścia tego projektu był plik `bitwa.py` który zawiera grę napisaną przeze mnie na pierwszym semestrze studiów. Nie jest on idealny, natomiast jako urozmaicenie (i utrudnienie) postanowiłem trzymać się zasady, aby ten kod był "nietykalny", co miało symulować scenariusz z wykorzystaniem zewnętrznego kodu. Sama gra to bardziej rozbudowana wersja klasycznego _kamień, papier, nożyce_, gdzie możemy wystawić trzy rodzaje jednostek - _piechurzy_, _konnica_ lub _artylerzysci_ na pole bitwy - po jednym rodzaju na każde skrzydło (lewe skrzydło, centrum lub prawe skrzydło). Jednostki mają różną cenę oraz różne współczynniki walki między sobą. Po określeniu poziomu trudności (wybraniu jak duży budżet mamy w porównaniu do przeciwnika) losowana jest armia przeciwnika, następnie możemy dokonać zwiadu za odpowiednią opłatą, aby podejrzeć wybrane skrzydło/a przeciwnika. Później wybieramy typ jednostek oraz ich liczebność na każde skrzydło. Walka przebiega przez roztrzyganie osobno, kolejno lewego skrzydła, prawego skrzydła, a na końcu walki w centrum, gdzie brane pod uwagę (z odpowiednim bonusem za flankowanie) są pozostałości z walk na skrzydłach. Przy każdej walce losowany jest pseudolosowy współczynnik, tak żeby wyniki nie były w pełni przewidywalne. Jeśli wygraliśmy, obliczana jest końcowa punktacja na podstawie tego, ile jednostek oraz jakiego typu nam zostało. Wynik zapisywany jest wraz z imieniem/nickem w pliku o nazwie `wynikiGraczy.txt`.

Projekt to analiza różnych algotytmów klasyfikacyjnych i porównanie ich skuteczności na przygotowanych przeze mnie danych. Dane zostały wygenerowane za pomocą pliku `generatorBitw.py` i zapisane w pliku `rozgrywki.txt`. Każda rozgrywka zapisana jest w 13 kolumnach, gdzie kolejno w 6 kolumnach podane są typy jednostek oraz ich liczebność dla "gracza", a później, w kolejnych 6 dla "przeciwnika". Ostatnia kolumna to wynik bitwy (jako 0 lub 1), informujące czy w takim ustawieniu armii, bez pseudolosowych współczynników (będących elementem prawdziwej rozgrywki) armia "gracza" wygrywa.

## Struktura katalogu

```
IO_projekt1/
├── src/                                  # Folder zawierający caly projekt
│   ├── badania/                          # Folder zawierający pliki analizujące klasyfikatory
│   │   ├── BayesBadania.py               # Badanie skuteczności klasyfikatora Bayesa
│   │   ├── KNNBadania.py                 # Testowanie klasyfikatora KNN
│   │   ├── drzewoDecyzyjneBadania.py     # Badania nad drzewem decyzyjnym
│   │   ├── funkcjeRobocze.py             # Funkcje pomocnicze (np. normalizacja, PCA)
│   │   ├── sieciNeuronoweBadania.py      # Badanie klasyfikatora opartego na sieciach neuronowych
│   │   ├── pcaBadania.py                 # Analiza PCA i utraty % wariancji
│   │   └── normalizacjaBadania.py        # Normalizacja danych wejściowych
│   ├── bitwa.py                          # Logika symulacji pojedynczej bitwy
│   ├── generatorBitw.py                  # Generator danych (bitew) na potrzeby klasyfikacji
│   ├── main.py                           # Menu - zagranie w grę lub wygenerowanie danych
│   ├── requirements.txt                  # Wymagania i zależności potrzebne do uruchomienia projektu
│   ├── rozgrywki.txt                     # Dane wejściowe zawierające scenariusze bitew
│   └── wynikiGraczy.txt                  # Zapis wyników uzyskanych przez graczy
├── wykresy/                              # Katalog z wykresami wyników klasyfikatorów
├── IO1_Bitwa.pdf                         # Dokumentacja projektu i przedstawienie wyniku badań (PDF)
└── LICENSE                               # Licencja projektu
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
python src/main.py
```

Alternatywnie, uruchamiaj konkretne badania pojedynczo:

```bash
python src/KNNBadania.py
python src/BayesBadania.py
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
