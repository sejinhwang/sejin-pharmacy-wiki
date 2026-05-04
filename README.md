# Sejin Pharmacy Wiki

A clinical pharmacy knowledge base for medicines optimisation, Epic / Connect Care documentation templates, POMR workflows, and hospital/LTC pharmacy practice.

## Scope

This repository is intended for:

- medicines optimisation workflows
- Admission MedRec and discharge MedRec templates
- Epic / Connect Care note templates and i-Vents
- POMR-based pharmacist documentation
- renal dosing and monitoring guides
- anticoagulation, AMS, geriatrics, and LTC review notes

## Local development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Preview locally at:

```text
http://127.0.0.1:8000
```

## Build

```bash
mkdocs build
```

## Safety

Do not commit PHI, patient identifiers, local exports, API keys, PDFs, or proprietary source material. Use this wiki as clinical decision support and documentation support only; verify recommendations against local policy, product monographs, and current clinical guidelines.
