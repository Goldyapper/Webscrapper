# Doctor Who Webscraper

A Python-based web scraper that extracts  data about Doctor Who episodes from (https://tardis.wiki). The project parses information like episode title, season, doctor, companions, villains, writers, director, and air dates — and stores the output into an SQLite database.

---

## Features

- Scrapes episode data from the TARDIS Wiki.
- Cleans and formats raw data (e.g., removes `[nb x]` notes).
- Stores episode data into a local SQLite database.
- Supports batch loading from a `.txt` list of episode titles.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Goldyapper/Webscrapper.git
cd Webscrapper
```

### 2. Install Dependencies

```pip install -r requirements.txt```

### 3. Prepare Your Input File

Add episode titles (one per line) to input.txt:
(See current inout file as an example)

### 4. Run the scraper

```python main.py```
