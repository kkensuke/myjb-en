# Naming Conventions

## Naming Conventions in Python

[PEP 8 – Style Guide for Python Code | peps.python.org](https://peps.python.org/pep-0008/)

### Package Names

- Python packages should also have short, all-lowercase names, although the use of underscores is discouraged. Examples: `mypackage`

### Module Names

- Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Example: `module_name`

### Constants

- Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples: `MAX_OVERFLOW`, `TOTAL`.

### Variable Names

- Variable names should be lowercase, with underscores for readability.
- Variable names should be short but descriptive. Single-character variable names and meaningless variable names should be avoided. Examples: `player_name`, `score`, etc.
- Boolean variable names are typically in the form of `is + adjective`, `has + noun`, `can + verb`, `with + noun`, etc. However, the first word can be omitted if it is obvious from the context. Example: `is_active`, `has_children`, `can_swim`, `with_fins`, etc.

### Function Names

- Function names should be lowercase, with underscores for readability. They should be in the form of `verb + noun`, but either can be omitted if it is obvious from the context. Examples: `get_score`, `print_message`

### Class Names

- Class names should normally use the CapWords convention. Examples: `MyClass`

### Method Names and Instance Variables

- Use the function and variable naming rules
- Use one leading underscore only for non-public methods and instance variables.

## Naming conventions in Other programming languages

Unlike Python, `camelCase` is used for naming variables and functions in other programming languages. Examples: `playerName`, `getScore`, `printMessage`

## Abbreviations

🚫 Don’t abbreviate names unless the abbreviation is widely used and understood. Recommended abbreviations are given [here](https://github.com/abbrcode/abbreviations-in-code).