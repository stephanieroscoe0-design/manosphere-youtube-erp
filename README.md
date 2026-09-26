# Mapping Weaponised Victimhood and Conspiratorial Framing in Masculinity-Focused YouTube Communities

Supporting code and materials for an MSc Data Science Extended Research Project at the University of Manchester.

This repository documents the procedures used to produce the analysis reported in the ERP. It contains the collection, preprocessing, modelling and analysis code. Comment-level source data are **not** published here; in accordance with the ERP guidance, reproduction assumes access to the original source data (see §6). Non-identifiable aggregate copies of the principal results are provided in `reference_results/` for comparison.

YouTube is a live platform. Rerunning the collection notebooks will reproduce the collection procedure, but will not recreate the exact historical corpus. The aggregate reference results included here allow reproduced outputs to be compared with the reported findings.

---

## 1. Overview

The project develops and evaluates text classifiers for three constructs in YouTube comments:

* **1A — Male grievance/victimhood**
* **1B — Weaponised victimhood**, defined as a subtype of 1A
* **2 — Conspiratorial framing**

The research has two parts:

* **RQ1 — Computational measurement:** rule-based, conventional machine-learning and transformer classifiers are developed using a manually annotated corpus. The selected classifiers are evaluated on a held-out test set.

* **RQ2 — Cross-community application:** predictions from the frozen classifiers are analysed across four selected community types. A blind manual audit assesses classifier transfer to unseen manosphere creators and comparison communities.

---

## 2. Repository structure

```text
.
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── notebooks/
│   ├── 01_collect_comments.ipynb
│   ├── 02_clean_comments.ipynb
│   ├── 03_sampling.ipynb
│   ├── 04_split.ipynb
│   ├── 05_lexicon.ipynb
│   ├── 06_naive_bayes.ipynb
│   ├── 07_logistic.ipynb
│   ├── 08_baseline_results.ipynb
│   ├── 09_RQ1_experiments.ipynb
│   ├── 10_RQ1_final_build.ipynb
│   ├── 11_RQ2_collect_comments.ipynb
│   ├── 12_RQ2_clean_comments.ipynb
│   ├── 13_RQ2_final_build.ipynb
│   ├── 14_RQ2_blind_audit.ipynb
│   ├── 15_RQ2_audit_analysis.ipynb
│   ├── 16_inter_annotator_agreement.ipynb
│   └── lexicon_rules.py
└── reference_results/
    ├── REFERENCE_RESULTS.md
    ├── cv_baseline_metrics.csv
    ├── rq1_final_test_metrics.csv
    ├── rq2_community_prevalence.csv
    ├── rq2_bootstrap_contrasts.csv
    ├── rq2_permutation_omnibus.csv
    ├── rq2_permutation_pairwise.csv
    ├── rq2_audit_metrics.csv
    └── rq2_audit_confusion_counts.csv
```

Comment-level data, analytical outputs and trained model weights are not included in this public repository (see §6). The `.env` key and these directories are excluded via `.gitignore`. The `reference_results/` directory holds non-identifiable aggregate copies of the principal results for comparison.

---

## 3. Requirements

The analysis requires:

* Python 3.10 or later;
* the packages listed in `requirements.txt`;
* a YouTube Data API v3 key for notebooks 01 and 11;
* GPU acceleration for practical execution of notebooks 09 and 10.

Install the required packages with:

```bash
pip install -r requirements.txt
```

The transformer experiments were originally run using Google Colab with an NVIDIA T4 GPU. They may be run on a CPU, but execution will be considerably slower. Small numerical differences may arise when transformer models are rebuilt using different hardware or package versions. Non-identifiable aggregate copies of the principal results are provided in `reference_results/` for comparison with a reproduced run.

---

## 4. Local setup

Clone the repository:

```bash
git clone https://github.com/stephanieroscoe0-design/manosphere-youtube-erp.git
cd manosphere-youtube-erp
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

To run either collection notebook, copy the API-key template:

```bash
cp .env.example .env
```

Then edit `.env` and add:

```text
YOUTUBE_API_KEY=your_key_here
```

The `.env` file is excluded through `.gitignore` and must not be committed. An API key is required only to run the collection notebooks (01 and 11).

---

## 5. Running the transformer notebooks in Google Colab

Notebooks 09 and 10 fine-tune transformer models and are intended to be run with GPU acceleration.

In Google Colab, select:

**Runtime → Change runtime type → T4 GPU**

Then run:

```python
!git clone https://github.com/stephanieroscoe0-design/manosphere-youtube-erp.git
%cd /content/manosphere-youtube-erp/notebooks
!pip install -r ../requirements.txt
```

Notebooks 09 and 10 require the RQ1 source data (the training/validation splits and the frozen held-out predictions), which are not published in this repository (see §6). Place them under `data/processed/` and `outputs/rq1/` before running. The notebooks resolve their paths relative to the repository root and use the same directory structure in VS Code and Colab.

Notebook 09 performs transformer model-selection experiments. Notebook 10 builds the selected classifiers and analyses the frozen held-out prediction file. The frozen held-out prediction file is part of the source data; exact predictions can vary slightly when the models are retrained on different hardware.

---

## 6. Data availability

Comment-level source data are not included in this public repository because
they contain identifiable user-generated content. In accordance with the ERP
guidance, reproduction assumes access to the original source data.

Notebooks 01 and 11 document the YouTube API collection procedures, while the
remaining notebooks document preprocessing, sampling, model development,
evaluation and statistical analysis.

The `reference_results/` directory contains non-identifiable aggregate copies
of the principal results reported in the ERP. These allow reproduced outputs
to be compared with the submitted findings.

YouTube is a live platform. A new API collection will reproduce the collection
procedure but will not recreate the exact historical corpus.

## 7. Analysis workflow

The notebooks are numbered according to the research workflow. However, the workflow includes manual annotation and frozen-prediction stages, so it is not a single completely automated pipeline.

A reader reproducing the reported analysis uses the completed annotation, prediction and audit files from the source data (see §6).

|  # | Notebook | Purpose |
| -: | -------- | ------- |
| 01 | `01_collect_comments.ipynb` | Collects the RQ1 corpus from 10 selected channels using the YouTube Data API |
| 02 | `02_clean_comments.ipynb` | Cleans and filters the RQ1 corpus |
| 03 | `03_sampling.ipynb` | Creates the initial channel-stratified annotation sample and supplementary keyword-enriched sample |
| 04 | `04_split.ipynb` | Deduplicates the completed labelled corpus and creates the fixed training, validation and held-out test sets |
| 05 | `05_lexicon.ipynb` | Evaluates the frozen rule-based lexicon on the development data |
| 06 | `06_naive_bayes.ipynb` | Fits and evaluates the Naïve Bayes baseline |
| 07 | `07_logistic.ipynb` | Fits and evaluates the TF–IDF logistic-regression baseline |
| 08 | `08_baseline_results.ipynb` | Performs the 5-fold cross-validation comparison of the three baseline approaches |
| 09 | `09_RQ1_experiments.ipynb` | Compares RoBERTa and DeBERTa configurations, learning rates, regularisation, thresholds and multiple seeds; also evaluates hierarchical 1B experiments |
| 10 | `10_RQ1_final_build.ipynb` | Builds the selected RQ1 classifiers and calculates held-out performance from the frozen test predictions |
| 11 | `11_RQ2_collect_comments.ipynb` | Collects the 12-month RQ2 corpus across 16 channels and 4 community groups |
| 12 | `12_RQ2_clean_comments.ipynb` | Cleans the RQ2 corpus and removes comment-level overlap with the RQ1 labelled data |
| 13 | `13_RQ2_final_build.ipynb` | Calculates prevalence estimates, hierarchical bootstrap confidence intervals and permutation tests from the frozen scored RQ2 corpus |
| 14 | `14_RQ2_blind_audit.ipynb` | Reconstructs the final 240-comment blind transfer audit and merges the completed labels with the hidden prediction key |
| 15 | `15_RQ2_audit_analysis.ipynb` | Calculates weighted audit metrics, confidence intervals, confusion counts and disagreement summaries |
| 16 | `16_inter_annotator_agreement.ipynb` | Constructs and analyses the repeated-annotation reliability sample |
|  — | `lexicon_rules.py` | Contains the frozen lexicon rules imported by notebooks 05 and 08 |

### Manual annotation stages

Notebook 03 creates unlabelled samples for manual annotation. The annotations themselves are not generated computationally. The completed annotations correspond to the source file:

```text
data/processed/labelled_comments_final.csv
```

Notebook 14 constructs the blind transfer-audit sample. The completed audit labels correspond to the source file:

```text
outputs/rq2/rq2_final_audit_240_labelled.csv
```

The files containing model predictions are labelled `KEY_DO_NOT_OPEN` because they were hidden during blind annotation.

---

## 8. Collection and modelling settings

### RQ1 collection

Notebook 01 uses the following fixed settings:

* up to 500 videos per channel;
* up to 200 comment records per video;
* a target of 40,000 comments per channel;
* relevance-ordered comment threads;
* inclusion of top-level comments and available replies;
* incremental saving and checkpointing;
* a maximum of 8 retries for transient API errors.

### RQ1 sampling and splitting

Notebook 03 uses a channel-stratified sample containing:

* 60% keyword-matched comments;
* 40% comments sampled from the remaining corpus;
* 500 candidate comments per channel;
* seed 42.

It then produces a supplementary keyword-enriched sample for the rarer 1B and construct 2 categories.

Notebook 04 removes exact-text duplication and creates the fixed training, validation and held-out test sets using seed 42.

### Transformer development

Notebook 09 evaluates:

* `roberta-base`;
* `microsoft/deberta-v3-base`;
* learning rates of 1 × 10⁻⁵, 2 × 10⁻⁵ and 3 × 10⁻⁵;
* baseline, weight-decay and weight-decay-plus-warm-up configurations;
* decision thresholds from .10 to .90;
* seeds 42, 1 and 2;
* direct and hierarchical approaches to 1B classification.

Notebook 10 uses the following selected configurations:

| Construct | Architecture | Learning rate | Weight decay | Threshold |
| --------- | --------------- | ------------: | -----------: | --------: |
| 1A | RoBERTa-base | 3 × 10⁻⁵ | 0.00 | .46 |
| 1B | DeBERTa-v3-base | 3 × 10⁻⁵ | 0.01 | .59 |
| 2 | DeBERTa-v3-base | 2 × 10⁻⁵ | 0.00 | .45 |

The three classifiers are trained independently. For the reported results, a positive 1B prediction is retained only where the corresponding 1A prediction is also positive.

### RQ2 collection

Notebook 11 uses:

* 4 community groups;
* 4 channels per community;
* videos published from 19 August 2025 up to, but not including, 19 August 2026;
* public videos of at least 5 minutes;
* up to 20 videos per channel;
* up to 200 top-level comments per video;
* comments ordered by time;
* no replies.

### RQ2 statistical analysis

Notebook 13 uses:

* equal weighting of videos within channels and channels within communities;
* 10,000 hierarchical bootstrap resamples;
* 100,000 Monte Carlo draws for the permutation analysis where applicable;
* seed 42;
* the constrained 1B prediction.

Notebook 15 uses 10,000 bootstrap resamples with seed 42 for the weighted transfer-audit confidence intervals.

---

## 9. Principal inputs and outputs

The notebooks read the source data and write their outputs locally under `data/` and `outputs/` (not published; see §6). Non-identifiable aggregate copies of the principal results are provided in `reference_results/`.

### Baseline results

| Analysis | Output |
| -------- | ------ |
| Lexicon development predictions | `data/processed/lexicon_development_predictions.csv` |
| Lexicon development metrics | `data/processed/lexicon_development_metrics.csv` |
| Naïve Bayes validation metrics | `data/processed/nb_validation_metrics.csv` |
| Naïve Bayes stop-word ablation | `data/processed/nb_validation_metrics_stopwords.csv` |
| Logistic-regression validation metrics | `data/processed/lr_validation_metrics.csv` |
| Logistic-regression stop-word ablation | `data/processed/lr_validation_metrics_stopwords.csv` |
| Baseline cross-validation comparison | `data/processed/cv_baseline_metrics.csv` |

### Transformer experiments

| Analysis | Output |
| -------- | ------ |
| RoBERTa seed-level validation results | `data/processed/results_roberta_finetuned_validation.csv` |
| RoBERTa summary | `data/processed/results_roberta_finetuned_summary.csv` |
| DeBERTa seed-level validation results | `data/processed/results_deberta_finetuned_validation.csv` |
| DeBERTa summary | `data/processed/results_deberta_finetuned_summary.csv` |
| Weighted hierarchical 1B experiment | `data/processed/results_deberta_hierarchical_1B_seed42.csv` |
| Unweighted hierarchical 1B experiment | `data/processed/results_deberta_hierarchical_1B_UNWEIGHTED_seed42.csv` |

### RQ1 held-out evaluation

Notebook 10 reads:

```text
outputs/rq1/rq1_final_test_predictions.csv
```

and writes:

```text
outputs/rq1/RQ1_ANALYSIS/rq1_final_constrained_test_predictions.csv
outputs/rq1/RQ1_ANALYSIS/rq1_final_constrained_test_metrics.csv
outputs/rq1/RQ1_ANALYSIS/rq1_analysis_settings.json
```

### RQ2 prevalence analysis

Notebook 13 reads:

```text
outputs/rq2/rq2_FINAL_primary_12mo_SCORED.csv
```

and writes:

```text
outputs/rq2/rq2_prevalence/rq2_scored.csv
outputs/rq2/rq2_prevalence/rq2_channel_results.csv
outputs/rq2/rq2_prevalence/rq2_community_results.csv
outputs/rq2/rq2_prevalence/rq2_bootstrap_community_CI.csv
outputs/rq2/rq2_prevalence/rq2_bootstrap_contrasts.csv
outputs/rq2/rq2_prevalence/rq2_permutation_omnibus.csv
outputs/rq2/rq2_prevalence/rq2_permutation_pairwise.csv
outputs/rq2/rq2_prevalence/rq2_community_prevalence.png
outputs/rq2/rq2_prevalence/rq2_community_prevalence.pdf
```

### RQ2 transfer audit

The final merged audit is written to:

```text
outputs/rq2/rq2_final_audit_240_MERGED.csv
```

The principal audit outputs are:

```text
outputs/rq2/audit_new_four/new_four_AUDIT_weighted_metrics.csv
outputs/rq2/audit_new_four_FN_FP_by_construct_community.csv
outputs/rq2/audit_confusion_table.csv
```

---

## 10. Reproducibility notes

* Random seeds are declared in the relevant notebooks. Seed 42 is used for the principal sampling, splitting, final model and RQ2 resampling procedures. Seeds 42, 1 and 2 are used for transformer stability checks.
* The frozen train, validation and test files preserve the divisions used in the ERP.
* The RQ1 held-out analysis uses the frozen test probabilities from the source data.
* The RQ2 prevalence analysis uses the frozen scored corpus from the source data.
* Rebuilding the transformer models may produce small differences across hardware and software environments.
* New YouTube API collection will differ from the historical corpus because the platform changes over time.
* The aggregate reference results in `reference_results/` provide the reference figures from the submitted report.

---

## 11. Responsible use

The classifiers were developed for the research design and corpora described in the ERP. Their predictions should not be treated as definitive judgements about individual commenters, creators or communities.

Performance varied across constructs and settings. Weaponised victimhood was the most difficult construct to classify, while transfer performance was weaker in some comparison-community settings. The RQ2 prevalence values should therefore be interpreted as estimates of **model-detected discourse**, rather than exact measurements of the underlying constructs.

---

## 12. Author

Stephanie Roscoe
MSc Data Science Extended Research Project
University of Manchester
2026
