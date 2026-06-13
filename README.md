# CSV-data-analyser
A basic Python tool for analyzing CSV files

- Analyses either a single or multiple columns
- Summarises statistics built into the CSV
- Prints and writes results into a .txt file

## Setup instructions
1. clone the repo using bash command:
```
git clone https://github.com/DAC2792/CSV-data-analyser.git
```

2. Create a virtual environment to work from, Use bash command:
```
python -m venv venv
```

3. Bash install the required libraries from requirements file using:
```
pip install -r requirements.txt
```

4. Run program:
```
python analyser.py
```
You will be prompted to enter your CSV filepath for analysis, along with a column(s) name(s) for max/min values, separated with commas if using multiple column names
