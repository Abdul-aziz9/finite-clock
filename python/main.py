"""
Life Countdown Timer
--------------------
Usage:
    python main.py

Modules:
    life_expectancy.py  — looks up CDC life expectancy from CSV
    countdown.py        — calculates years/days(to the second) remaining
    display.py          — terminal display loop (updates daily)
    generate_image.py   — generates the infinity-strike BMP asset
"""

import sys
import subprocess
import os
from life_expectancy import get_life_expectancy
from display import run_display

IMAGE_SCRIPT = os.path.join(os.path.dirname(__file__), "image_renderer.py")
IMAGE_OUTPUT = "infinity_strike.bmp"


def prompt_user() -> tuple[int, int, str]:
    print("\n  Life Countdown Timer\n")

    while True:
        try:
            year = int(input("  Birth year  (e.g. 1990): ").strip())
            if 1900 <= year <= 2025:
                break
            print("  Please enter a year between 1900 and 2025.")
        except ValueError:
            print("  Invalid year.")

    while True:
        try:
            month = int(input("  Birth month (1–12):      ").strip())
            if 1 <= month <= 12:
                break
            print("  Please enter a month between 1 and 12.")
        except ValueError:
            print("  Invalid month.")

    while True:
        sex = input("  Sex (male/female):       ").strip().lower()
        if sex in ("male", "female", "m", "f"):
            sex = "male" if sex in ("male", "m") else "female"
            break
        print("  Please enter 'male' or 'female'.")

    return year, month, sex


def generate_image() -> str:
    """Run generate_image.py and return the output filename."""
    result = subprocess.run([sys.executable, IMAGE_SCRIPT], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"  Warning: image generation failed.\n  {result.stderr.strip()}")
    else:
        print(f"  {result.stdout.strip()}")
    return IMAGE_OUTPUT


def main():
    birth_year, birth_month, sex = prompt_user()

    print("\n  Looking up life expectancy…")
    try:
        life_exp = get_life_expectancy(sex)
    except Exception as e:
        print(f"  Error: {e}")
        sys.exit(1)

    print(f"  Life expectancy ({sex}): {life_exp:.1f} years")
    print("\n  Generating image asset…")
    image_path = generate_image()

    print("\n  Starting countdown display. Press Ctrl+C to exit.\n")
    run_display(birth_year, birth_month, life_exp, sex, image_path)


if __name__ == "__main__":
    main()