# Weather Dashboard

## Overview

This project is a terminal-based Weather Dashboard created to practice Python modules, packages, PIP, and third-party libraries.

The program retrieves live weather data for New York City using the Open-Meteo API and displays the current temperature in both Celsius and Fahrenheit.

## Project Structure

```text
weather_app
│
├── main.py
├── requirements.txt
│
└── utils
    ├── __init__.py
    ├── fetcher.py
    └── formatter.py
```

## Task 1 - Modules and Namespaces

The project started with `formatter.py`, `fetcher.py`, and `main.py` in the same directory.

Two different import styles were used:

```python
from formatter import format_temp
import fetcher
```

The `format_temp()` function can be called directly, while the `get_weather()` function is called using the module name:

```python
fetcher.get_weather()
```

## Task 2 - Creating a Package

The `formatter.py` and `fetcher.py` files were moved into a package named `utils`.

An empty `__init__.py` file was added to the `utils` folder.

The imports in `main.py` were updated to:

```python
from utils.formatter import format_temp
from utils import fetcher
```

## Task 3 - PIP and External Dependencies

The project uses the third-party `requests` library to retrieve live weather information.

Install the required package with:

```powershell
python -m pip install requests
```

Or install the dependencies from `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

## Running the Program

Run the application from the project directory:

```powershell
python main.py
```

## Example Output

```text
--- WEATHER DASHBOARD ---
Current Temperature: 13.3°C (55.9°F)
```

The temperature may be different each time because the program retrieves current weather data.

## What I Learned

In this lab, I learned how to:

- Import functions from Python modules.
- Import an entire module and use its namespace.
- Organize modules inside a Python package.
- Use `__init__.py` in a package.
- Install third-party libraries using PIP.
- Use the `requests` library.
- Retrieve data from an API.
- Access values inside nested dictionaries.
- Use a `requirements.txt` file to manage project dependencies.