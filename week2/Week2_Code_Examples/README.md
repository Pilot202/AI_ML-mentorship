# Week 2 — Python for Data: NumPy, Pandas & Visualization

Companion code for Week 2 of the 3-Month ML Mentorship Program.
Matches the slide deck: `Week2_NumPy_Pandas_Visualization.pptx`.

## Files

| File | Session | Topic |
|---|---|---|
| `01_numpy_arrays.py` | Monday | Creating arrays, shape, dtype, indexing, reshaping |
| `02_numpy_vectorization_broadcasting.py` | Monday | Vectorized ops, speed comparison, broadcasting |
| `03_pandas_dataframes.py` | Tuesday | Series vs. DataFrame, read_csv, head/info/describe, loc/iloc |
| `04_pandas_cleaning_merging.py` | Tuesday | Missing values, duplicates, concat, merge |
| `05_pandas_groupby.py` | Tuesday | groupby, aggregation, custom functions |
| `06_visualization_matplotlib_seaborn.py` | Thursday | Bar, line, box, and scatter plots |
| `07_mini_project_dataset_explorer.py` | Thursday (practice) | Capstone project combining everything above |

## Setup

Activate your virtual environment from Week 1, then install this week's
packages:

```bash
pip install numpy pandas matplotlib seaborn
pip freeze > requirements.txt
```

## Running the examples

Each file is self-contained and runnable on its own:

```bash
python 01_numpy_arrays.py
python 02_numpy_vectorization_broadcasting.py
python 03_pandas_dataframes.py
python 04_pandas_cleaning_merging.py
python 05_pandas_groupby.py
python 06_visualization_matplotlib_seaborn.py
python 07_mini_project_dataset_explorer.py
```

`03_pandas_dataframes.py` creates `students.csv` so the `read_csv()`
example works standalone. `06_visualization...py` and
`07_mini_project...py` save `.png` chart files into the same folder —
open them after running to see the results.

## Practice project brief

`07_mini_project_dataset_explorer.py` is the Week 2 capstone: it builds
a small, deliberately messy dataset, then walks through the full data
workflow — load, clean, compute statistics, group and aggregate, and
visualize — saving a final summary chart.

Try extending it yourself:
1. Swap in a real dataset from Kaggle (e.g. Titanic or House Prices)
2. Add a second chart type (box plot or scatter) to the same script
3. Compute a "most improved subject" insight and print it
4. Push the finished project to your GitHub portfolio alongside Week 1
