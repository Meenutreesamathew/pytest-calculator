# pytest-calculator

A simple Python calculator project with unit tests powered by **pytest**.
This project demonstrates how to structure a Python package and test it using `pytest`.

---

## Project Structure

```
pytest-calculator/
│── calculator.py        # Calculator functions (add, subtract, multiply, divide)
│── tests/
│   └── test_calculator.py
│── README.md
```

---

## Installation

Clone the repository and navigate into it:

```bash
git clone https://github.com/your-username/pytest-calculator.git
cd pytest-calculator
```

It’s recommended to create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Example `requirements.txt`:

```
pytest
pytest-html
```

---

## Running Tests

Run tests with pytest:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -v
```

Run tests and generate an **HTML report**:

```bash
pytest --html=report.html --self-contained-html
```

This will generate a `report.html` file in the project directory.

---

## Example Pytest-HTML Report Screenshot

![Pytest HTML Report Example](https://raw.githubusercontent.com/pytest-dev/pytest-html/main/docs/_static/report.png)

---

## License

This project is licensed under the MIT License.
