import flet as ft
from datetime import datetime
from dateutil.relativedelta import relativedelta
from utils.image_share import *

def main(page: ft.Page):
    # Material You theme configuration
    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.DEEP_PURPLE,
        use_material3=True
    )
    page.title = "Age Calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 600
    page.window_resizable = False
    page.auto_scroll = True
    page.scroll = True

    #Image generation variables
    result_text = ft.Text(value="", size=16)
    img_preview = ft.Image(width=400, fit= ft.ImageFit.CONTAIN)
    name_field = ft.TextField(label="Your Name", width= 300)

    # State variables
    selected_date = datetime.now()
    age_years = ft.Text("--", size=48, weight=ft.FontWeight.BOLD)
    age_months = ft.Text("--", size=32)
    age_days = ft.Text("--", size=32)

    def update_age(birth_date):
        today = datetime.now()
        delta = relativedelta(today, birth_date)
        
        age_years.value = f"{delta.years}"
        age_months.value = f"{delta.months} months"
        age_days.value = f"{delta.days} days"
        page.update()

    def handle_date_pick(e):
        nonlocal selected_date
        if date_picker.value:
            selected_date = datetime(
                date_picker.value.year,
                date_picker.value.month,
                date_picker.value.day,
            )
            selected_date_display.value = selected_date.strftime("%B %d, %Y")
            date_picker.open = False  # Close the picker after selection
            update_age(selected_date)
        page.update()

    def on_generate(e):
        result_text.value = "Generating..."
        page.update()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = generate_age_card_image(name_field.value, date_picker.value, output_path=f"src/assets/age_cards/age_card_{timestamp}.png")
        result_text.value = f"Generated: {out_path}"
        img_preview.src = out_path
        page.open(image_display)
        page.update()

    def on_share(e):
        if not os.path.exists("src/assets/age_cards/age_card.png"):
            result_text.value = "Please generate the image first."
            page.update()
            return
        share_image(page, "src/assets/age_cards/age_card.png")

    # Date picker configuration
    date_picker = ft.DatePicker(on_change=handle_date_pick)
    page.overlay.append(date_picker)

    def open_date_picker(e):
        date_picker.open = True
        page.update()

    # UI Components
    selected_date_display = ft.Text(
        "Select your birth date", 
        size=18,
        weight=ft.FontWeight.W_500
    )

    age_display = ft.Card(
        elevation=8,
        content=ft.Container(
            width=300,
            padding=30,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Text("AGE", size=18),
                    age_years,
                    ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                    age_months,
                    age_days,
                ]
            )
        )
    )

    image_display = ft.AlertDialog(
        modal= True,
        title= ft.Text("Age Card"),
        content= img_preview,
        actions= [
            ft.IconButton(icon= ft.Icons.SHARE_OUTLINED, on_click = on_share, tooltip= "Share"),
            ft.IconButton(icon= ft.Icons.CLOSE , on_click = lambda e: page.close(image_display), tooltip= "Close")
        ]
        )

    # GitHub button
    github_button = ft.FloatingActionButton(
        icon=ft.Icons.CODE,
        shape=ft.CircleBorder(),
        tooltip="View GitHub Repository",
        mini=True,
        on_click=lambda _: page.launch_url("https://github.com/virendracarpenter")
    )

    # Image capture button
    capture_button = ft.FloatingActionButton(
        icon=ft.Icons.PHOTO_CAMERA_ROUNDED,
        shape=ft.CircleBorder(),
        tooltip="Generate Card",
        mini=True,
        on_click= on_generate)
    

    # Main layout
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
            controls=[
                ft.Icon(ft.Icons.CAKE, size=40),
                selected_date_display,
                age_display,
                name_field,
                ft.ElevatedButton(
                    "Select Birth Date",
                    icon=ft.Icons.CALENDAR_MONTH,
                    on_click=open_date_picker,
                ),
            ]
        ),
        ft.Container(
            alignment=ft.alignment.center,
            margin=ft.margin.only(bottom=30),
            content=ft.Row([github_button, capture_button], alignment= ft.MainAxisAlignment.CENTER)
        ),
    )

ft.app(target=main, assets_dir= "src/assets")
