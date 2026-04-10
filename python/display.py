import os
import sys
import time
from datetime import date
from countdown import calculate_countdown, TimeLeft
from image_renderer import print_image, CONTENT_WIDTH, margin, term_width


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# ── Box helpers ────────────────────────────────────────────────────────────────
# Inner width = CONTENT_WIDTH minus 2 border chars (│ on each side)
INNER = CONTENT_WIDTH - 2
REFRESH_DELAY = 1

def _row(content: str = "") -> str:
    """Return a padded inner row, left-aligned, trimmed to INNER width."""
    return "│" + content.ljust(INNER)[:INNER] + "│"


def _center(text: str) -> str:
    """Center text within INNER columns."""
    return text.center(INNER)


def render(t: TimeLeft, life_exp: float, sex: str, image_path: str):
    clear_screen()
    tw = term_width()
    pad = " " * margin(tw)

    # ── Image ──────────────────────────────────────────────────────────
    print_image(image_path)

    # ── Box (same width as image, same left margin) ────────────────────
    top_bar    = "┌" + "─" * INNER + "┐"
    divider    = "├" + "─" * INNER + "┤"
    bottom_bar = "└" + "─" * INNER + "┘"

    def line(content: str = ""):
        print(pad + _row(content))

    print(pad + top_bar)
    line(_center("F I N I T E  C L O C K"))
    print(pad + divider)

    if t.expired:
        line(_center("You should be dead by now."))
    else:
        countdown_str = (
                        f"{t.years:>2} Yrs  "
                        f"{t.days:>3} Days  "
                        f"{t.hours:>2} Hrs  "
                        f"{t.minutes:>2} Min  "
                        f"{t.seconds:>2} Sec"
                    )
        line(_center(countdown_str))

    print(pad + divider)

    # Progress bar — fills INNER minus brackets and spaces
    bar_inner = INNER - 4           # "[ " + bar + " ]"
    if t.total_days > 0:
        life_days   = life_exp * 365.25
        elapsed     = life_days - t.total_days
        filled      = int((elapsed / life_days) * bar_inner)
    else:
        filled = bar_inner
    bar = "█" * filled + "░" * (bar_inner - filled)
    line(f"  [{bar}]")

    print(pad + divider)
    # line(f"  Life expectancy ({sex.capitalize():<3}): {life_exp:.1f} yrs")
    line(_center(f"  Updated: {date.today().isoformat()}"))
    print(pad + bottom_bar)
    print()
    print(pad + "  [Ctrl+C to exit]")
    


def run_display(birth_year: int, birth_month: int, life_exp: float, sex: str, image_path: str):
    try:
        while True:
            today = date.today()
            last_date= 0
            if today != last_date:
                last_date = today
                t = calculate_countdown(birth_year, birth_month, life_exp)
                render(t, life_exp, sex, image_path)
            time.sleep(REFRESH_DELAY)
            clear_screen()
    except KeyboardInterrupt:
        print("\n  Goodbye.\n")