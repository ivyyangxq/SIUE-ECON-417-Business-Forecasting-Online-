# ECON 417 — Business Forecasting

Current student materials for Lectures 1–6. The repository has three material collections:

- **Lecture_Notes/** — numbered lecture notes in PDF.
- **Slides/** — the matching lecture slides in PDF.
- **Coding_Notes/** — complete classroom Jupyter notebooks, including the data and drawing helper needed by their examples.

## Lecture materials

| Lecture | Topic | Notes | Slides | Coding Note |
|---|---|---|---|---|
| 1 | Data Structure and Baseline Forecasts | [PDF](Lecture_Notes/Lecture_01_Notes.pdf) | [PDF](Slides/Lecture_01_Slides.pdf) | [Notebook](Coding_Notes/Lecture_01_Coding_Note.ipynb) |
| 2 | Validation, Overfitting, and Forecast Failure | [PDF](Lecture_Notes/Lecture_02_Notes.pdf) | [PDF](Slides/Lecture_02_Slides.pdf) | [Notebook](Coding_Notes/Lecture_02_Coding_Note.ipynb) |
| 3 | Regularization and Model Stability | [PDF](Lecture_Notes/Lecture_03_Notes.pdf) | [PDF](Slides/Lecture_03_Slides.pdf) | [Notebook](Coding_Notes/Lecture_03_Coding_Note.ipynb) |
| 4 | Nonlinearity and Risk Control | [PDF](Lecture_Notes/Lecture_04_Notes.pdf) | [PDF](Slides/Lecture_04_Slides.pdf) | [Notebook](Coding_Notes/Lecture_04_Coding_Note.ipynb) |
| 5 | Model Limits and Decision Context | [PDF](Lecture_Notes/Lecture_05_Notes.pdf) | [PDF](Slides/Lecture_05_Slides.pdf) | [Notebook](Coding_Notes/Lecture_05_Coding_Note.ipynb) |
| 6 | From Gradients to Neural Networks | [PDF](Lecture_Notes/Lecture_06_Notes.pdf) | [PDF](Slides/Lecture_06_Slides.pdf) | [Notebook](Coding_Notes/Lecture_06_Coding_Note.ipynb) |

## Open and run

1. Fork this repository into your own GitHub account. Download the fork as a ZIP and extract it, or clone your fork.
2. Open the whole extracted/cloned course folder in VS Code.
3. Install Python and the VS Code Python and Jupyter extensions. In the selected Python environment, run `python -m pip install -r requirements.txt` from this folder.
4. Open a notebook inside `Coding_Notes`, select that Python kernel, and run cells from top to bottom. Restart and Run All checks that the notebook works from a fresh session.

Notebooks are editable programs; PDFs are reading materials. The complete classroom demonstrations are reference examples. For practice, keep a separate notebook beside the reference and explain what each line changes before adapting it.

Lectures 1–3 may retrieve historical market data through yfinance. Internet access and data-provider availability affect these downloads; Lectures 2–3 label their constructed fallback data when used. Lectures 4–5 use the supplied synthetic classroom CSVs. Lecture 6 uses explicitly constructed examples and adds no new homework or project model requirement. Generated Lecture 4–6 figures/tables go into the ignored `Coding_Notes/outputs` folder.

Lecture 6 is an intuitive introduction. Its detailed gradient and network calculations are optional reference. The earlier numbered examples explain the code behind each method and figure.

Only current notes, slides and classroom Coding Notes are distributed here. The previous root-level teaching files have been replaced; Git history retains earlier versions.

Official setup references: [VS Code](https://code.visualstudio.com/docs/getstarted/overview), [Jupyter notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks), [forking a GitHub repository](https://docs.github.com/en/pull-requests/how-tos/work-with-forks/fork-a-repo).
