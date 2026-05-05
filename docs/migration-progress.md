# Migration Progress

This page tracks the batch migration from the Notion Index Page into this public wiki.

## Verification Gate

Each batch must pass:

| Check | Requirement | Status |
| --- | --- | --- |
| Source inventory | Notion source pages identified for the database or page group. | In progress |
| Page creation | Wiki pages created with stable slugs. | In progress |
| Anchor review | Headings converted to stable Markdown anchors. | Pending |
| Internal links | Notion page references converted to wiki links where target pages exist. | Pending |
| External/source links | Remaining Notion source links preserved when no wiki target exists yet. | Pending |
| Build validation | `mkdocs build --strict` passes. | Passing |
| Public deployment | GitHub Pages deployment succeeds. | Pending |

## Batch Table

| Batch | Source | Wiki Target | Inventory | Migrated | Links/Anchors | Build | Deploy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | Index Page shell | Home, Meta-Database, Pharmacy Practice, BPS, Other Certifications | Done | Done | Done | Pass | Pass |
| 01 | Meta-Database | `docs/meta-database.md` and child topic pages | Pending | Pending | Pending | Pending | Pending |
| 02 | Alberta Pharmacy Care Plan | `docs/pharmacy-practice/alberta-pharmacy-care-plan.md` | Done | Done | Done | Pass | Pending |
| 03 | PIP \| Pharmacist Independent Prescribing for Minor Ailment | `docs/pharmacy-practice/pip-minor-ailment.md` | Done | Inventory | Done | Pass | Pending |
| 04 | Symptom Sorter | `docs/pharmacy-practice/symptom-sorter/` | Pending | Pending | Pending | Pending | Pending |
| 05 | NHS \| Do and Don't | `docs/pharmacy-practice/nhs-do-and-dont/` | Pending | Pending | Pending | Pending | Pending |
| 06 | Patient Care Process | `docs/pharmacy-practice/patient-care-process/` | Pending | Pending | Pending | Pending | Pending |
| 07 | Hospital Pharmacy 101 | `docs/pharmacy-practice/hospital-pharmacy-101-modules/` | Done | Done | Done | Pass | Pending |
| 08 | Accident and Emergency Medicine \| BCEMP | `docs/bps/bcemp/` | Pending | Pending | Pending | Pending | Pending |
| 09 | Infectious Diseases \| BCIDP | `docs/bps/bcidp/` | Pending | Pending | Pending | Pending | Pending |
| 10 | Critical Care \| BCCCP | `docs/bps/bcccp/` | Pending | Pending | Pending | Pending | Pending |
| 11 | Pharmacotherapy \| BCPS | `docs/bps/bcps/` | Pending | Pending | Pending | Pending | Pending |
| 12 | Pharmacy Informatics | `docs/bps/pharmacy-informatics/` | Pending | Pending | Pending | Pending | Pending |
| 13 | Ambulatory Care \| BCACP/BCMTMS | `docs/bps/bcacp-bcmtms/` | Pending | Pending | Pending | Pending | Pending |
| 14 | Oncology/Haematology \| BCOP | `docs/bps/bcop/` | Pending | Pending | Pending | Pending | Pending |
| 15 | Nutrition Support \| CNSC/BCNSP | `docs/bps/cnsc-bcnsp/` | Pending | Pending | Pending | Pending | Pending |
| 16 | Psychiatry \| BCPP | `docs/bps/bcpp/` | Pending | Pending | Pending | Pending | Pending |
| 17 | Cardiology \| BCCP | `docs/bps/bccp/` | Pending | Pending | Pending | Pending | Pending |
| 18 | Paediatric Pharmacotherapy \| BCPPS | `docs/bps/bcpps/` | Pending | Pending | Pending | Pending | Pending |
| 19 | Geriatrics \| BCGP | `docs/bps/bcgp/` | Pending | Pending | Pending | Pending | Pending |
| 20 | Diabetes \| CDECB/CDCES/BC-ADM | `docs/other-certifications/diabetes/` | Pending | Pending | Pending | Pending | Pending |
| 21 | Travel and Tropical Medicine \| CTH | `docs/other-certifications/travel-tropical-medicine/` | Pending | Pending | Pending | Pending | Pending |
| 22 | Anticoagulation \| CACP | `docs/other-certifications/anticoagulation/` | Pending | Pending | Pending | Pending | Pending |

## Current Batch Notes

Batch 07 migrated the discovered Hospital Pharmacy 101 modules:

- Hospital Pharmacy Administration and Management
- Basics of Aseptic Compounding
- Intravenous Lines and Pumps
- Nutrition Support and Enteral Tubes
- Interpreting and Managing Electrolytes
- Therapeutic Drug Monitoring
- Perioperative Management
- Antimicrobials in Hospital Practice

Internal links were converted among these migrated pages where targets exist. Remaining Notion references stay as source links until their target databases are migrated.

Batch 02 migrated the Alberta Pharmacy Care Plan eligibility page and its three child lists:

- Chronic Conditions | Column A
- Risk Factors | Column B
- Other Conditions

Eligibility criteria use local anchors; source databases remain linked to Notion until condition-level pages are expanded.

Batch 03 migrated the PIP database schema and condition inventory. Condition-level pages remain linked to their Notion sources and can be expanded into local child pages in subsequent passes.
