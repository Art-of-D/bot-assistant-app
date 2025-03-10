# Read me before start

## How to?

### 1. Clone the repository

```
~ git clone https://github.com/Art-of-D/bot-assistant-app.git \
~ cd <project_folder> \
```

### 2. Install poetry (if not already installed)

```
~ curl -sSL https://install.python-poetry.org | python3 -
OR
~pipx install poetry
```

### 3. Install dependencies

```
~ poetry install
```

### 4. Run the script

```
~ poetry run start
```

### 5. If you want to activate the virtual environment

```
~ poetry env use python3
~ poetry env info --path <-- get address to venv
~ source /path/to/venv/bin/activate
```

EXAMPLE --> source /Users/art/Library/Caches/pypoetry/virtualenvs/bot-j0Zsbxew-py3.13/bin/activate # For macOS/Linux \
OR \
path\to\venv\Scripts\activate # For Windows

```
~ start
```

### 6. Exit the virtual environment

```
~ exit
```

### 7. Add dependencies

```
~ poetry add <package_name> # For runtime dependencies
~ poetry add --dev <package_name> # For development dependencies
```

## Some info

Project has some folders

```
bot/
│ ├── filer/ # to store data on a local machine
│ │ ├── **init**.py
│ │ ├── filer.py
│ ├── internal/ # for all classes
│ │ ├── **init**.py
│ │ ├── manager.py # to manage commands
│ │ ├── phone.py
│ │ ├── birthday.py
│ │ ├── name.py
│ │ ├── ...
│ │ ├──note # to manage notes
│ │ │ ├──note.py
│ │ │ ├──notes.py
│ │ │ ├──tag.py
│ ├── handler/ # to handle inputs
│ │ ├──notes_handler.py
│ │ ├──...
│ ├── decorators/ # for all decorators
│ │ ├── errorhandler.py
│ ├── storage/ # to store data
│ ├── utilities/ # some instruments
│ │ ├──parser.py
│ │ ├──...
│ ├── **init**.py
│ ├── bot.py # main script
├── .gitignore
├── pyproject.toml
├── README.md
```
