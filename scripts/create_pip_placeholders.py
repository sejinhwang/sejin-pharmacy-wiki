#!/usr/bin/env python3
"""Create local placeholder pages for PIP minor ailment topics.

This script is intentionally conservative:
- it creates only missing files;
- it does not overwrite existing drafted pages;
- it does not include patient identifiers, personal identifiers, signatures, or medicine dose tables;
- each page is marked as under construction until full reviewed content is migrated.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET_DIR = ROOT / "docs" / "pharmacy-practice" / "pip-minor-ailment"

PAGES = [
    ("Abortifacient Medical Abortion", "abortifacient-medical-abortion.md"),
    ("Abortifacient Consultation Tick List", "abortifacient-consultation-tick-list.md"),
    ("Acne Vulgaris Mild To Moderate", "acne-vulgaris-mild-to-moderate.md"),
    ("Acute Cough", "acute-cough.md"),
    ("Allergic Rhinitis", "allergic-rhinitis.md"),
    ("Backache And Neck Pain Acute", "backache-and-neck-pain-acute.md"),
    ("Calluses And Corns", "calluses-and-corns.md"),
    ("Cold Sores", "cold-sores.md"),
    ("Conjunctivitis", "conjunctivitis.md"),
    ("COVID-19 Outpatient Antiviral Assessment", "covid-19-outpatient-antiviral-assessment.md"),
    ("Dermatitis Atopic Eczema", "dermatitis-atopic-eczema.md"),
    ("Dermatitis Contact Allergic Irritant", "dermatitis-contact-allergic-irritant.md"),
    ("Diabetes Insulin Injection And CBG Supplies", "diabetes-insulin-injection-cbg-supplies.md"),
    ("Diarrhoea Acute Non-Infectious", "diarrhoea-acute-non-infectious.md"),
    ("Dry Eyes Keratoconjunctivitis Sicca", "dry-eyes-keratoconjunctivitis-sicca.md"),
    ("Emergency Contraception", "emergency-contraception.md"),
    ("Erectile Dysfunction", "erectile-dysfunction.md"),
    ("Folliculitis Shaving Rash Hot Tub Rash", "folliculitis-shaving-rash-hot-tub-rash.md"),
    ("Gastro-Oesophageal Reflux Disease", "gastro-oesophageal-reflux-disease.md"),
    ("High Altitude Illness", "high-altitude-illness.md"),
    ("Hormonal Contraception", "hormonal-contraception.md"),
    ("Impetigo", "impetigo.md"),
    ("Indigestion Dyspepsia", "indigestion-dyspepsia.md"),
    ("Infantile Colic", "infantile-colic.md"),
    ("Insect Bites And Stings", "insect-bites-and-stings.md"),
    ("Lyme Disease Post-Exposure Prophylaxis", "lyme-disease-post-exposure-prophylaxis.md"),
    ("Menopause Vasomotor Symptoms", "menopause-vasomotor-symptoms.md"),
    ("Minor Ailments Schedule 4 Eligible Drugs Ontario", "minor-ailments-schedule-4-eligible-drugs-ontario.md"),
    ("Minor Aphthous Ulcers Mouth Ulcers", "minor-aphthous-ulcers-mouth-ulcers.md"),
    ("Musculoskeletal Sprains And Strains", "musculoskeletal-sprains-and-strains.md"),
    ("Nappy Rash Nappy Dermatitis", "nappy-rash-nappy-dermatitis.md"),
    ("Nasal Congestion Acute Sinusitis", "nasal-congestion-acute-sinusitis.md"),
    ("Nausea And Vomiting", "nausea-and-vomiting.md"),
    ("Nausea And Vomiting In Pregnancy", "nausea-and-vomiting-in-pregnancy.md"),
    ("Onychomycosis", "onychomycosis.md"),
    ("Oral Thrush Candidal Stomatitis", "oral-thrush-candidal-stomatitis.md"),
    ("Osteoarthritis Joint Pain", "osteoarthritis-joint-pain.md"),
    ("Otitis Externa Swimmers Ear", "otitis-externa-swimmers-ear.md"),
    ("Pityriasis Versicolor Tinea Versicolor", "pityriasis-versicolor-tinea-versicolor.md"),
    ("Post-Procedure Pain", "post-procedure-pain.md"),
    ("Premenstrual Syndrome", "premenstrual-syndrome.md"),
    ("Primary Dysmenorrhoea", "primary-dysmenorrhoea.md"),
    ("Sleep Disorders Acute Insomnia", "sleep-disorders-acute-insomnia.md"),
    ("Sore Throat GABHS Assessment", "sore-throat-gabhs-assessment.md"),
    ("Tinea Capitis", "tinea-capitis.md"),
    ("Tinea Corporis", "tinea-corporis.md"),
    ("Tinea Cruris", "tinea-cruris.md"),
    ("Tinea Pedis", "tinea-pedis.md"),
    ("Travel Health Assessment", "travel-health-assessment.md"),
    ("Travel Health Prescribing", "travel-health-prescribing.md"),
    ("Uncomplicated Cystitis", "uncomplicated-cystitis.md"),
    ("Urticaria", "urticaria.md"),
    ("Warts And Verrucas", "warts-and-verrucas.md"),
]

TEMPLATE = """# {title}\n\n!!! warning \"Under construction\"\n    This public wiki page is a local placeholder. Full assessment, counselling, safety-netting, and review content will be added later.\n\n## Status\n\n- Local page created: yes\n- Full source content migrated: no\n- Review status: pending\n- Public-ready clinical page: no\n"""


def main() -> int:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    created = []
    skipped = []

    for title, filename in PAGES:
        path = TARGET_DIR / filename
        if path.exists():
            skipped.append(filename)
            continue
        path.write_text(TEMPLATE.format(title=title), encoding="utf-8")
        created.append(filename)

    print(f"Created {len(created)} placeholder page(s).")
    for filename in created:
        print(f"  + {filename}")

    print(f"Skipped {len(skipped)} existing page(s).")
    for filename in skipped:
        print(f"  = {filename}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
