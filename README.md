# PD2

## Przygotowanie środowiska (system Windows)

Upewnij się, że na twoim systemie można uruchamiać skrypty: [guide](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system)

Stworzenie virual environment
```
python -m venv venv
```

Aktywacja virual environment
```
.\venv\Scripts\activate.ps1
```

Zainstalowanie zależności w wirtualnym środowisku
```
pip install -r requirements.txt
```

Wyjście ze środowiska

```
deactivate
```

## Uruchamianie serwera przez internet

```
python app.py
```

## Testowanie API

Aby testy działały API musi być uruchomione

```
pytest -v
```
