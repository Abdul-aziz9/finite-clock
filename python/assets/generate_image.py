import math
import sys

# Try to import Pillow, but provide a clear error if missing
try:
    from PIL import Image, ImageDraw
except ImportError:
    print("This script requires the Pillow library.")
    print("Please run: pip install pillow")
    sys.exit(1)

def generate_asset():
    """
    Generates a BMP file containing an infinity symbol with a horizontal strikethrough.
    Uses the Lemniscate of Bernoulli for the infinity path.
    """
    # 1. Configuration
    filename = "infinity_strike.bmp"
    width, height = 800, 400
    bg_color = (255, 255, 255)  # White
    stroke_color = (0, 0, 0)    # Black
    stroke_width = 15
    line_strike_width = 10

    # 2. Initialization
    # BMP does not support transparency in standard viewers, so we use RGB.
    img = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # 3. Math: Lemniscate of Bernoulli
    # Formula: (x^2 + y^2)^2 = 2a^2(x^2 - y^2)
    # Parametric: x = a*cos(t)/(1+sin^2(t)), y = a*sin(t)cos(t)/(1+sin^2(t))
    
    center_x, center_y = width / 2, height / 2
    scale_a = width / 3.0  # Scale factor for the loop size
    
    points = []
    steps = 2000 # High resolution for smooth curves
    
    for i in range(steps + 1):
        t = (i / steps) * 2 * math.pi
        denom = 1 + math.sin(t)**2
        
        # Calculate raw coordinates
        x = (scale_a * math.cos(t)) / denom
        y = (scale_a * math.sin(t) * math.cos(t)) / denom
        
        # Center and flip Y (since image coordinates y-down)
        points.append((center_x + x, center_y - y))

    # 4. Drawing
    # Draw Infinity Symbol
    # use line join logic implicitly handled by PIL for smooth corners
    draw.line(points, fill=stroke_color, width=stroke_width, joint='curve')

    # Draw Horizontal Line (Strike-through)
    # Spanning 90% of the width
    margin = width * 0.05
    line_start = (margin, center_y)
    line_end = (width - margin, center_y)
    
    draw.line([line_start, line_end], fill=stroke_color, width=line_strike_width)

    # 5. Output
    img.save(filename, format="BMP")
    print(f"Asset generated successfully: {filename}")

if __name__ == "__main__":
    generate_asset()