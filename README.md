# AmazonHelp AI Support Agent — Hiver SDE Take-Home

Runnable implementation using the Customer Support on Twitter (TWCS) dataset and the **AmazonHelp** brand. A prepared 50,000-pair subset and 198-example gold-set seed are included so the project can run without downloading the 500+ MB raw CSV.

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.run_experiment --gold data/gold_set.csv
python -m src.agent --message "Where is my Amazon package?"
```

Optional review UI:
```powershell
streamlit run src/annotator.py
```

## Important evaluation note
The included 198 `gold_intent` values are deterministic seed labels and are marked `SEED_REVIEW_REQUIRED`. The Hiver assignment asks for 150–250 **hand-labelled** examples. A human must review/correct these before claiming the final gold set is hand-labelled.

## Structure
- `data/amazon_pairs.csv` — prepared AmazonHelp customer→response pairs
- `data/gold_set.csv` — 198 seed gold-set candidates
- `src/` — classifier, retrieval agent, annotation UI, evaluation
- `reports/results/` — generated metrics
