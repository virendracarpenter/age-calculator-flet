import flet as ft
from datetime import datetime
from dateutil.relativedelta import relativedelta

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

    # Date picker configuration
    date_picker = ft.DatePicker(on_change=handle_date_pick)
    page.overlay.append(date_picker)

    def share_action(e):
        page.update()
    
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

    # GitHub button
    github_button = ft.FloatingActionButton(
        icon=ft.Icons.CODE,
        shape=ft.CircleBorder(),
        tooltip="View GitHub Repository",
        mini=True,
        on_click=lambda _: page.launch_url("https://github.com/virendracarpenter")
    )

    # Main layout
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.END,
            controls=[
                ft.Button(
                    "Share with others",
                    icon=ft.Icons.SHARE,
                    tooltip="Share",
                    on_click=share_action
                )
            ]
        ),
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=40,
            controls=[
                ft.Icon(ft.Icons.CAKE, size=40),
                selected_date_display,
                age_display,
                ft.ElevatedButton(
                    "Select Birth Date",
                    icon=ft.Icons.CALENDAR_MONTH,
                    on_click=open_date_picker,
                ),
            ]
        ),
        ft.Container(
            alignment=ft.alignment.bottom_center,
            margin=ft.margin.only(bottom=50),
            content=github_button
        )
    )

ft.app(target=main)
