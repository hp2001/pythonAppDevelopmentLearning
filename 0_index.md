# Python Learning Progress

## ✅ Already Covered

- Variables and basic syntax
- Conditions
- Loops
- Lists
- Sets
- Dictionaries
- List of dictionaries
- Functions
- Return values
- `__name__ == "__main__"`
- Text file reading/writing
- CSV reading/writing
- JSON reading/writing
- `try/except`
- Modules
- Importing your own modules
- `pip`
- Installing packages

---

## 🟡 Still Need to Learn

### 1. Python Data Structures — Deeper Usage

- Tuple
- List/set/dictionary comprehensions
- `enumerate()`
- `zip()`
- `sorted()` with `key`
- `lambda`
- `any()` / `all()`
- `collections` module
- `Counter`
- `defaultdict`
- `deque`

### 2. Functions — Deeper Concepts

- Default arguments
- Keyword arguments
- `*args`
- `**kwargs`
- Scope
- Closures
- Type hints

### 3. Error Handling

- Multiple `except`
- `else`
- `finally`
- `raise`
- Creating custom exceptions

> You've started this section but haven't covered all of it.

### 4. File & Directory Handling

- `pathlib`
- Creating directories
- Checking whether files exist
- Moving/copying files
- Finding files by extension
- Working with timestamps
- `os` vs `pathlib`

> This will be particularly useful for scripts.

### 5. Packages & Environments

- Package structure
- `__init__.py`
- Virtual environments (`venv`)
- `requirements.txt`
- Installing/uninstalling/upgrading packages
- Dependency management
- Why virtual environments matter

### 6. External Libraries

- Reading library documentation
- `requests`
- HTTP basics
- GET/POST
- Query parameters
- Headers
- JSON responses
- Status codes
- API authentication

> This is where we'll start building API-based scripts.

### 7. Command-Line Applications

- `input()`
- `sys.argv`
- `argparse`
- Command-line flags

Build scripts such as:

`bash`
`python process.py --input employees.csv --output result.csv`

### 8. Configuration

- Configuration files
- Environment variables
- `.env`
- `python-dotenv`
- Separating configuration from code
- Secrets/API keys

### 9. Logging

- `logging`
- Log levels
- Log files
- Useful logging patterns
- Replacing `print()` with proper logging

### 10. Databases

- SQLite
- SQL from Python
- Connections
- Queries
- Parameters
- Transactions
- CRUD
- Later: SQL Server/PostgreSQL

> This should be particularly useful given your Data Engineering background.

### 11. Object-Oriented Programming

We haven't needed it yet, but applications eventually benefit from it.

- Classes
- Objects
- `__init__`
- Instance attributes/methods
- Class attributes
- Inheritance
- Composition
- Properties
- `dataclasses`

> I don't want to spend weeks on theoretical OOP. We'll learn it through a small application.

### 12. Testing

- `pytest`
- Unit tests
- Assertions
- Fixtures
- Testing functions
- Mocking external APIs/files

### 13. Debugging

- Reading tracebacks
- Debugger
- Breakpoints
- Inspecting variables
- Debugging systematically

### 14. Working with APIs

Build actual scripts such as:

```text
API
 ↓
JSON
 ↓
Python
 ↓
Transform
 ↓
CSV / JSON / database
```

### 15. Concurrency / Parallelism

Later, after you've built several scripts:

- `threading`
- `multiprocessing`
- `concurrent.futures`
- `asyncio`
- When each one is appropriate

### 16. Application Architecture

Once the fundamentals are solid:

``` text 
main.py
   ↓
configuration
   ↓
business logic
   ↓
utilities
   ↓
data access
   ↓
logging
   ↓
error handling
```