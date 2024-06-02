# CIPHER

1. ROT13, ROT47 (SZYFR CEZARA) -> https://pl.wikipedia.org/wiki/Szyfr_Cezara
2. Funkcjonalności
    - FileHandler odczyt, zapis do pliku, user podaje nazwe, wyjatki, Gdy chce zapisać do tego samego pliku to append (Plik Json)
    - Szyfrowanie i Odszyfrowywanie.
    - Buffer / MemoryBuffer czyli taka lista, która sobie istnieje podczas działania programu, do niej będziemy dodawać usuwać itd. Z niej zapisywać do pliku i do niej wczytywać. 
    - Menu (Menu oparte o dict, czy match case python 3.10+)
    - Manager (Facade)
    - run/main.py (Czyli jeden moment uruchomienia programu)
    - Exit
    - Testy Jednostkowe


### struktura obiekt

- Obiekt Text zaszyfrowany/odszyfrowany to dataclasss. 
- {"text"": xyz, "rot_type": rot13/rot47, "status": encrypted/decrypted}

1. Dodatkowe rzeczy:
    - FactoryMethod / AbstractFactory
   
2. Stylistyka
    - PEP 8
    - GitHubFlow
    - Czeste commity
    - Conventional commits
      - NOK -> add new way of handling files
      - OK -> feat: add new way of handling files
      - BEST OK -> feat(filehandler): add new way of handling files
      - NOK -> update .gitignore
      - OK -> chore: update .gitignore
      - BEST OK -> chore(git): update .gitignore
      - NOK -> create unit tests for file handling
      - OK -> test: create unit tests for file handling 
      - BEST OK -> test(filehandler): create unit tests for file handling
      - NOK -> update readme.md about file_handling feature
      - OK -> docs: update readme.md about file_handling feature
      - BEST -> docs(readme): update readme.md about file_handling feature
      - fix: and feat:, build:, chore:, ci:, docs:, style:, refactor:, perf:, test:,
    - Typing
    - Docstrings
    - Tools(Ze stachem)
      - Pre-commit (black, flake8) odpala lintery i formatery przy commicie (dokładnie przed)
      - *Poetry