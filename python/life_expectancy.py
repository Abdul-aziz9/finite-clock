import csv
import os

CSV_PATH = os.path.join(os.path.dirname(__file__), "file/raw/life_expectancy.csv")

SEX_ALIASES = {
    "m": "Male",
    "male": "Male",
    "f": "Female",
    "female": "Female",
}


def get_life_expectancy(sex: str, csv_path: str = CSV_PATH) -> float:
    """
    Return the most recent 'All Races' average life expectancy (years)
    for the given sex from the CDC dataset.
    """
    normalized = SEX_ALIASES.get(sex.strip().lower())
    if normalized is None:
        raise ValueError(f"Unknown sex '{sex}'. Use 'male' or 'female'.")

    best_year = -1
    best_value = None

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Race"].strip() != "All Races":
                continue
            if row["Sex"].strip() != normalized:
                continue
            year = int(row["Year"])
            if year > best_year:
                best_year = year
                best_value = float(row["Average Life Expectancy (Years)"])

    if best_value is None:
        raise ValueError(f"No data found for sex='{normalized}' in {csv_path}")

    return best_value