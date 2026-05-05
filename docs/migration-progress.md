# Migration Progress

This page tracks the batch migration from the Notion Index Page into this public wiki.

## Verification Gate

Each batch must pass:

| Check | Requirement | Status |
| --- | --- | --- |
| Source inventory | Notion source pages identified for the database or page group. | In progress |
| Full content import | Page body content is present in the wiki, not just a source link or summary. | Not started |
| Page creation | Wiki pages created with stable slugs. | In progress |
| Anchor review | Headings converted to stable Markdown anchors. | Pending |
| Internal links | Notion page references converted to wiki links where target pages exist. | Pending |
| Standalone review | Reader can use the page without opening Notion. | Pending |
| Build validation | `mkdocs build --strict` passes. | Passing |
| Public deployment | GitHub Pages deployment succeeds. | Pending |

## Batch Table

| Batch | Source | Wiki Target | Inventory | Migrated | Links/Anchors | Build | Deploy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | Index Page shell | Home, Meta-Database, Pharmacy Practice, BPS, Other Certifications | Done | Done | Done | Pass | Pass |
| 01 | Meta-Database | `docs/meta-database.md` and child topic pages | Pending | Pending | Pending | Pending | Pending |
| 02 | Alberta Pharmacy Care Plan | `docs/pharmacy-practice/alberta-pharmacy-care-plan.md` | Partial | Partial | Partial | Pass | Pass |
| 03 | PIP \| Pharmacist Independent Prescribing for Minor Ailment | `docs/pharmacy-practice/pip-minor-ailment.md` | Partial | Not migrated | Not started | Pass | Pass |
| 04 | Symptom Sorter | `docs/pharmacy-practice/symptom-sorter/` | Partial | 17 pages imported | Partial | Pending | Pending |
| 05 | NHS \| Do and Don't | `docs/pharmacy-practice/nhs-do-and-dont/` | Pending | Pending | Pending | Pending | Pending |
| 06 | Patient Care Process | `docs/pharmacy-practice/patient-care-process/` | Pending | Pending | Pending | Pending | Pending |
| 07 | Hospital Pharmacy 101 | `docs/pharmacy-practice/hospital-pharmacy-101-modules/` | Done | Partial summaries | Partial | Pass | Pass |
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

## Audit Notes

The earlier pass used a weaker definition of migration: source inventory, brief summaries, and source links. Under the standalone wiki standard, those pages must be treated as incomplete unless the actual page body is available locally.

Current audit:

- Batch 00 is structurally complete.
- Batch 02 is partial: core eligibility and child lists are local, but source references and condition-level detail are not fully converted.
- Batch 03 is not migrated: it is only a condition inventory with Notion links.
- Batch 04 has restarted under the standalone standard: 3 symptom pages are now local imports, and the remaining symptom pages are pending.
- Batch 07 is partial: module pages exist, but they are summaries rather than full local imports of the Notion content.

Batch 07 discovered these Hospital Pharmacy 101 modules:

- Hospital Pharmacy Administration and Management
- Basics of Aseptic Compounding
- Intravenous Lines and Pumps
- Nutrition Support and Enteral Tubes
- Interpreting and Managing Electrolytes
- Therapeutic Drug Monitoring
- Perioperative Management
- Antimicrobials in Hospital Practice

Internal links were converted among the summary pages where targets exist. Full content import remains pending.

Batch 02 migrated the Alberta Pharmacy Care Plan eligibility page and its three child lists:

- Chronic Conditions | Column A
- Risk Factors | Column B
- Other Conditions

Eligibility criteria use local anchors. Full standalone review remains pending.

Batch 03 only captured the PIP database schema and condition inventory. Condition-level pages still need local content pages.

Batch 04 standalone import now includes 17 symptom pages. Remaining symptom-level pages must be imported as local content pages, with local links and anchor checks.
