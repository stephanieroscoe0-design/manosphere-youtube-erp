# Reference results

Non-identifiable, aggregate copies of the principal results reported in the ERP.
They let a reproduced run be compared against the submitted findings. No comment
text, usernames, comment IDs or row-level predictions are included.

Rebuilding the transformer models may produce small numerical differences across
hardware and software environments.

## Files

| File | Contents | Notebook |
|------|----------|:--------:|
| `cv_baseline_metrics.csv` | 5-fold cross-validated F1 for the lexicon, Naïve Bayes and logistic-regression baselines | 08 |
| `rq1_final_test_metrics.csv` | RQ1 held-out test precision / recall / F1 and confusion counts (constrained 1B) | 10 |
| `rq2_community_prevalence.csv` | RQ2 predicted prevalence per community with 95% bootstrap intervals | 13 |
| `rq2_bootstrap_contrasts.csv` | Manosphere-vs-comparison prevalence differences with intervals | 13 |
| `rq2_permutation_omnibus.csv` | Omnibus permutation-test statistics and p-values | 13 |
| `rq2_permutation_pairwise.csv` | Pairwise permutation differences with exact and Holm-adjusted p-values | 13 |
| `rq2_audit_metrics.csv` | Sampling-weighted audit precision / recall / F1 with intervals (overall, manosphere, comparison) | 15 |
| `rq2_audit_confusion_counts.csv` | Weighted TP / FP / FN / TN behind the audit metrics | 15 |
| `inter_annotator_agreement.csv` | Reliability: raw agreement, Cohen's κ, positive/negative agreement | 16 |

## Headline figures

**Baselines — cross-validated F1**

| Construct | Lexicon | Naïve Bayes | Logistic regression |
|-----------|:-------:|:-----------:|:-------------------:|
| 1A | 0.312 | 0.535 | 0.564 |
| 1B | 0.169 | 0.274 | 0.382 |
| 2  | 0.278 | 0.416 | 0.480 |

**RQ1 held-out test — F1 (constrained 1B)**

| Construct | Precision | Recall | F1 |
|-----------|:---------:|:------:|:----:|
| 1A | 0.577 | 0.651 | 0.612 |
| 1B | 0.417 | 0.385 | 0.400 |
| 2  | 0.686 | 0.750 | 0.716 |

**RQ2 prevalence — % predicted positive**

| Construct | Manosphere | Wellbeing | Self-improvement | Control |
|-----------|:----------:|:---------:|:----------------:|:-------:|
| 1A | 30.8 | 7.2 | 1.5 | 0.2 |
| 1B | 6.9  | 2.1 | 0.3 | 0.1 |
| 2  | 4.0  | 0.5 | 1.5 | 0.1 |

**RQ2 blind audit — weighted F1**

| Construct | Manosphere | Comparison |
|-----------|:----------:|:----------:|
| 1A | 0.817 | 0.471 |
| 1B | 0.450 | 0.088 |
| 2  | 0.905 | 0.490 |

**Inter-annotator agreement — reliability (n = 341)**

| Construct | Raw agreement | Cohen's κ |
|-----------|:-------------:|:---------:|
| 1A | 0.859 | 0.705 |
| 1B | 0.909 | 0.685 |
| 2  | 0.924 | 0.628 |

Exact three-label agreement was 76.8%. Full figures: `inter_annotator_agreement.csv`.
