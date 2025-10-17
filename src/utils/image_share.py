# age_card_share_flet.py
import flet as ft
from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta
import os
import platform
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, random

from PIL import Image, ImageDraw, ImageFont

def generate_age_card_image(name, birthdate: date, template_path="src/assets/card_bg/template.png", output_path="src/assets/age_cards/age_card.png"):
    # Load your background template
    img = Image.open(template_path).convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Try to load fonts (fallback to default)
    try:
        font_extra_large = ImageFont.truetype("arialbd.ttf", 130)
        font_large = ImageFont.truetype("arialbd.ttf", 100)
        font_medium = ImageFont.truetype("arialbd.ttf", 60)
        font_script = ImageFont.truetype("ariali.ttf", 50)
        font_small = ImageFont.truetype("ariali.ttf", 35)
    except:
        font_extra_large = ImageFont.load_default()
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_script = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Main text positions (tuned for your image layout)
    w, h = img.size

    # Age numbers (centered)
    today = datetime.now()
    delta = relativedelta(today, birthdate)
    age_text = f"{delta.years} Years"
    month_text = f"{delta.months} Months"
    day_text = f"{delta.days} Days"

    # Compute approximate positions manually tuned for your template (768x768 base)
    center_x = w // 2

    # Draw text with light shadow for depth
    def draw_shadow_text(text, pos, font, fill, shadow_color=(50, 50, 50, 80), shadow_offset=(2, 2)):
        x, y = pos
        # shadow
        draw.text((x + shadow_offset[0], y + shadow_offset[1]), text, font=font, fill=shadow_color)
        # main text
        draw.text((x, y), text, font=font, fill=fill)

    # Year, Month, Day
    draw_shadow_text(age_text, (center_x - 170, 180), font_large, fill=(230, 210, 255))
    draw_shadow_text(month_text, (center_x - 120, 310), font_medium, fill=(255, 190, 210))
    draw_shadow_text(day_text, (center_x - 80, 400), font_script, fill=(230, 210, 255))

    # Label section below
    draw_shadow_text(f"{name}'s journey continues...", (center_x - 240, 650), font=font_small, fill=(60, 60, 60))

    img.save(output_path)
    print(f"✅ Card saved as {output_path}")

    return output_path[10:]


# ======================================================
# 2️⃣ FUNCTION — Share image (Works on Web & Android)
# ======================================================
def share_image(page: ft.Page, image_path: str):
    """
    For Web → uses navigator.share()
    For Android → uses Intent via shell command
    For Desktop → opens image location
    """
    system = platform.system().lower()

    if page.web:  # Flet Web build
        js_code = f"""
        if (navigator.canShare) {{
            fetch("{page.origin}/{image_path}")
              .then(r => r.blob())
              .then(blob => {{
                const file = new File([blob], "age_card.png", {{type: "image/png"}});
                navigator.share({{
                    files: [file],
                    title: "My Age Card",
                    text: "Check out my Age Card!",
                }});
              }})
              .catch(err => alert("Sharing failed: " + err));
        }} else {{
            alert("Your browser does not support direct sharing.");
        }}
        """
        page.eval_js(js_code)

    elif "android" in system:
        try:
            os.system(f'am start -a android.intent.action.SEND -t "image/png" -e android.intent.extra.STREAM "file://{os.path.abspath(image_path)}"')
        except Exception as e:
            print("Error launching share intent:", e)

    else:
        # For Windows/macOS/Linux — open folder
        path = os.path.abspath(image_path)
        if system == "windows":
            os.startfile(path)
        elif system == "darwin":
            os.system(f"open {os.path.dirname(path)}")
        else:
            os.system(f"xdg-open {os.path.dirname(path)}")

