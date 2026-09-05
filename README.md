# validkit

validkit ist eine kleine, eigenständige Python-Bibliothek für Prüf- und
Normalisierungsaufgaben. Sie stellt neun unabhängige, reine Funktionen bereit —
darunter Validierungen für E-Mail, Luhn, IBAN und ISBN-13 sowie Normalisierungen
für Telefonnummern, Akzente, Geheimtexte und Slugs sowie eine Clamp-Funktion.
Alle Funktionen sind sauber typannotiert, werfen klare Fehler bei ungültiger
Eingabe und lehnen überlange Eingaben vor der Verarbeitung ab.

## Tech-Stack

- **Sprache**: Python (≥ 3.9)
- **Abhängigkeiten**: keine (nur Standardbibliothek)
- **Tests**: pytest
- **Paketierung**: pyproject.toml

## Installation

```bash
pip install -e .
```

Für die Entwicklung inklusive der Test-Abhängigkeit:

```bash
pip install -e .[dev]
```

## Tests

```bash
pytest
```

## Verwendung

```python
import validkit
```

### is_valid_email

```python
>>> from validkit import is_valid_email
>>> is_valid_email("user@example.com")
True
```

### luhn_check

```python
>>> from validkit import luhn_check
>>> luhn_check("4111 1111 1111 1111")
True
```

### is_valid_iban

```python
>>> from validkit import is_valid_iban
>>> is_valid_iban("DE44 5001 0517 5407 3249 31")
True
```

### is_valid_isbn13

```python
>>> from validkit import is_valid_isbn13
>>> is_valid_isbn13("978-3-16-148410-0")
True
```

### normalize_phone

```python
>>> from validkit import normalize_phone
>>> normalize_phone("030 1234567", "49")
'+49301234567'
```

### strip_accents

```python
>>> from validkit import strip_accents
>>> strip_accents("Grüße, José — déjà vu")
'Gruesse, Jose — deja vu'
```

### mask_secret

```python
>>> from validkit import mask_secret
>>> mask_secret("geheim1234", 4)
'********1234'
```

### slugify

```python
>>> from validkit import slugify
>>> slugify("Héllo Wörld!")
'hello-world'
```

### clamp

```python
>>> from validkit import clamp
>>> clamp(5, 0, 10)
5
```

## Features

- Neun eigenständige, reine Funktionen ohne globalen Zustand oder I/O
- Keine externen Abhängigkeiten — nur Python-Standardbibliothek
- Klare Fehler bei ungültiger Eingabe (`TypeError` / `ValueError`) mit statischen Meldungen
- Schutz vor überlangen Eingaben (Maximallänge 4096 Zeichen)
- Vollständige Typannotationen und pytest-Abdeckung
