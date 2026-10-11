# Superstore Sales Dashboard

An interactive dashboard built on a real public retail dataset (Superstore, from Kaggle).
A Python script (pandas) cleans the raw CSV, and a plain HTML/CSS/JavaScript page (Chart.js) shows it with filters.

**Live demo:** https://osamamohamedgamal57-star.github.io/sales-dashboard/

**Data source:** Superstore Dataset on Kaggle (vivek468/superstore-dataset-final)

## Features
- Filter by year, region and category; KPIs and charts update instantly
- Revenue by month (line), by region (doughnut) and by category (bar)
- Counts unique orders (not order lines) for orders and average order value
- Responsive layout and automatic dark mode
- Clear message when no data matches the filters

## What the data pipeline does (`prepare_data.py`)
1. Loads the CSV (falls back to latin-1 encoding if needed)
2. Checks that the required columns exist and explains what to fix if not
3. Removes duplicate rows and fixes inconsistent text
4. Converts dates and numbers, and drops rows with missing values
5. Adds year and month columns and writes `data.js`

## Tech stack
Python, pandas, JavaScript (ES6), Chart.js, HTML5, CSS3 (Grid and Flexbox)

## Run it locally
1. Download the dataset from Kaggle and save it as `data/superstore.csv`
2. In a terminal inside this folder:
```bash
pip install pandas
python prepare_data.py
```
3. Open `index.html` in your browser. No server needed.

## What I learned
I learned how to clean a real dataset with pandas, including removing duplicates and fixing dates. I connected a Python data pipeline to a JavaScript page that updates charts when filters change. I also published the project online with GitHub Pages.
