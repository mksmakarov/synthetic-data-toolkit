# synthetic-data-toolkit

A lightweight commandline tool for generating synthetic text data using the `SyntheticDataGenerator` API wrapper.
This tool reads a prompt from a text file and produces one or more synthetic output files, each saved serarately.

---

## Installation (Poetry)

Install dependencies:

```bash
poetry install
```

Enter the virtual environment:
```bash
poetry shell
```

---

## Usage
```bash
pip install -e .
```

CLI usage:

```bash
synthetic-cli --prompt ./prompt.txt --output ./generated --threads 5
```