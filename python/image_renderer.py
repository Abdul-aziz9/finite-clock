import os
from PIL import Image

FULL  = "█"
TOP   = "▀"
BOT   = "▄"
EMPTY = " "

# Shared content width — image and box are both rendered at this many columns.
CONTENT_WIDTH = 60


def term_width() -> int:
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80


def margin(tw: int) -> int:
    """Left-padding so CONTENT_WIDTH block sits centered in the terminal."""
    return max(0, (tw - CONTENT_WIDTH) // 2)


def image_to_blocks(image_path: str) -> list[str]:
    """
    Load a BMP, scale to CONTENT_WIDTH columns, convert to block-char lines.
    Returns lines of exactly CONTENT_WIDTH characters (no padding).
    """
    img = Image.open(image_path).convert("L")

    orig_w, orig_h = img.size
    aspect = orig_h / orig_w
    target_w = CONTENT_WIDTH
    target_h = int(target_w * aspect * 0.55) * 2
    if target_h % 2 != 0:
        target_h += 1

    img = img.resize((target_w, target_h), Image.LANCZOS)
    pixels = img.load()

    threshold = 128
    lines = []

    for row in range(0, target_h, 2):
        line = ""
        for col in range(target_w):
            top_dark = pixels[col, row] < threshold
            bot_dark = pixels[col, row + 1] < threshold if (row + 1) < target_h else False

            if top_dark and bot_dark:
                line += FULL
            elif top_dark:
                line += TOP
            elif bot_dark:
                line += BOT
            else:
                line += EMPTY
        lines.append(line)

    return lines


def print_image(image_path: str):
    """Print the block-art image centered in the terminal."""
    try:
        pad = " " * margin(term_width())
        for line in image_to_blocks(image_path):
            print(pad + line)
    except Exception as e:
        print(f"  [image error: {e}]")