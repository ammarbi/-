import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "بيت النظافة - خدمات منزلية متكاملة"
    page.window_icon = "https://www.vectorstock.com/royalty-free-vector/home-repair-icon-white-background-vector-23448128"
    page.scroll = "auto"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 400
    page.window_height = 850
    page.window_resizable = False
    
    page.padding = 20
    page.fonts = {
        "Cairo": "https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&display=swap"
    }
    page.theme = ft.Theme(font_family="Cairo")

    # ألوان التطبيق
    primary_color = "#2C7A7B"
    secondary_color = "#E6FFFA"
    accent_color = "#38B2AC"

    # قائمة الخدمات
    services = [
        {"icon": "⚡", "name": "كهرباء", "desc": "إصلاح – تركيب – صيانة"},
        {"icon": "🚰", "name": "صحية", "desc": "تسربات – تمديدات – إصلاح مجاري"},
        {"icon": "🧱", "name": "بلاط ورخام", "desc": "تركيب – ترميم – تلميع"},
        {"icon": "🎨", "name": "دهان وديكورات", "desc": "داخلي/خارجي بجودة عالية"},
        {"icon": "🪑", "name": "نجارة وحدادة", "desc": "أبواب – شبابيك – درابزين"},
        {"icon": "🔲", "name": "سيراميك", "desc": "تركيب – ترميم – تصميم"},
    ]

    # مدخلات نموذج الطلب
    name = ft.TextField(
        label="الاسم بالكامل", 
        width=350, 
        border_color=primary_color,
        prefix_icon=ft.Icons.PERSON
    )
    
    phone = ft.TextField(
        label="رقم الهاتف", 
        width=350, 
        keyboard_type=ft.KeyboardType.PHONE,
        border_color=primary_color,
        prefix_icon=ft.Icons.PHONE
    )
    
    service_type = ft.Dropdown(
        label="نوع الخدمة",
        width=350,
        border_color=primary_color,
        options=[ft.dropdown.Option(s["name"]) for s in services]
    )
    
    address = ft.TextField(
        label="العنوان", 
        width=350, 
        border_color=primary_color,
        prefix_icon=ft.Icons.LOCATION_ON
    )
    
    notes = ft.TextField(
        label="تفاصيل إضافية", 
        width=350, 
        multiline=True, 
        min_lines=3, 
        max_lines=5,
        border_color=primary_color
    )

    # إرسال الطلب
    def submit_request(e):
        if not name.value or not phone.value or not service_type.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("يرجى إدخال الاسم ورقم الهاتف ونوع الخدمة 📱", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
            return
        
        # رسالة نجاح
        success_dialog = ft.AlertDialog(
            title=ft.Text("تم إرسال الطلب بنجاح ✅"),
            content=ft.Text(f"شكراً {name.value}، سنتواصل معك خلال 15 دقيقة"),
            actions=[ft.TextButton("حسناً", on_click=lambda e: close_dialog(success_dialog))]
        )
        
        page.dialog = success_dialog
        success_dialog.open = True
        
        # تفريغ الحقول بعد الإرسال
        name.value = ""
        phone.value = ""
        service_type.value = None
        address.value = ""
        notes.value = ""
        
        page.update()

    def close_dialog(dialog):
        dialog.open = False
        page.update()

    # فتح تفاصيل الخدمة
    def show_service_details(service):
        details_content = ft.Column([
            ft.Text(service["icon"] * 3, size=40, text_align="center"),
            ft.Text(service["name"], size=24, weight="bold", text_align="center"),
            ft.Text(service["desc"], size=16, text_align="center", color="gray"),
            ft.Divider(),
            ft.Text("هذه الخدمة تشمل:", size=16, weight="bold"),
            ft.Text(f"• {service['desc']}"),
            ft.Text("• استخدام أفضل المواد والأدوات"),
            ft.Text("• ضمان على العمل لمدة 6 أشهر"),
            ft.Text("• أسعار تنافسية وجودة عالية"),
        ], spacing=10)
        
        service_dialog = ft.AlertDialog(
            title=ft.Text("تفاصيل الخدمة"),
            content=details_content,
            actions=[
                ft.TextButton("طلب الخدمة", on_click=lambda e: select_service(service["name"])),
                ft.TextButton("إلغاء", on_click=lambda e: close_dialog(service_dialog))
            ]
        )
        
        page.dialog = service_dialog
        service_dialog.open = True
        page.update()

    def select_service(service_name):
        service_type.value = service_name
        page.dialog.open = False
        page.update()

    # إنشاء بطاقات الخدمات
    service_cards = []
    for service in services:
        card = ft.Card(
            elevation=3,
            content=ft.Container(
                padding=15,
                content=ft.Column([
                    ft.Text(service["icon"], size=30),
                    ft.Text(service["name"], size=18, weight="bold", text_align="center"),
                    ft.Text(service["desc"], size=12, text_align="center", color="gray")
                ], 
                alignment="center", 
                horizontal_alignment="center",
                spacing=5),
                on_click=lambda e, s=service: show_service_details(s)
            ),
            color=secondary_color
        )
        service_cards.append(card)

    # أزرار التواصل
    whatsapp_btn = ft.ElevatedButton(
        "تواصل عبر واتساب",
        icon=ft.Icons.CHAT,
        url="https://wa.me/963982988836",
        bgcolor="#25D366",
        color="white",
        width=160
    )
    
    call_btn = ft.ElevatedButton(
        "اتصال هاتفي",
        icon=ft.Icons.CALL,
        url="tel:+963982988836",
        bgcolor=primary_color,
        color="white",
        width=160
    )
    
    facebook_btn = ft.ElevatedButton(
        "صفحتنا على الفيسبوك",
        icon=ft.Icons.PUBLIC,
        url="https://n9.cl/8x5y9",
        bgcolor="#3b5998",
        color="white",
        width=160
    )

    # رأس التطبيق
    header = ft.Column([
        ft.Row([
            ft.Icon(ft.Icons.HOME_REPAIR_SERVICE, color=primary_color, size=30),
            ft.Text("بيت النظافة", size=24, weight="bold", color=primary_color)
        ], alignment="center"),
        ft.Text("خدمات منزلية متكاملة بجودة عالية", size=16, color="gray", text_align="center")
    ], spacing=10, horizontal_alignment="center")

    # قسم الخدمات
    services_section = ft.Column([
        ft.Text("خدماتنا", size=20, weight="bold", color=primary_color),
        ft.GridView(
            expand=1,
            runs_count=2,
            max_extent=170,
            child_aspect_ratio=0.9,
            spacing=10,
            run_spacing=10,
            controls=service_cards,
        )
    ], spacing=15)

    # قسم المميزات
    features_section = ft.Column([
        ft.Text("لماذا نحن؟", size=20, weight="bold", color=primary_color),
        ft.Row([
            ft.Column([
                ft.Icon(ft.Icons.ATTACH_MONEY, color=accent_color),
                ft.Text("أسعار منافسة", size=14, weight="bold"),
                ft.Text("عروضنا تناسب", size=12),
                ft.Text("جميع الميزانيات", size=12),
            ], spacing=5, horizontal_alignment="center"),
            ft.Column([
                ft.Icon(ft.Icons.SECURITY, color=accent_color),
                ft.Text("ضمان على العمل", size=14, weight="bold"),
                ft.Text("ضمان يصل إلى", size=12),
                ft.Text("6 أشهر", size=12),
            ], spacing=5, horizontal_alignment="center"),
            ft.Column([
                ft.Icon(ft.Icons.ACCESS_TIME, color=accent_color),
                ft.Text("خدمة 24/7", size=14, weight="bold"),
                ft.Text("متاحون دائماً", size=12),
                ft.Text("لخدمتكم", size=12),
            ], spacing=5, horizontal_alignment="center"),
        ], alignment="center", spacing=15)
    ], spacing=15)

    # نموذج الطلب
    request_form = ft.Column([
        ft.Text("طلب خدمة", size=20, weight="bold", color=primary_color),
        name,
        phone,
        service_type,
        address,
        notes,
        ft.ElevatedButton(
            "إرسال الطلب", 
            on_click=submit_request,
            bgcolor=accent_color,
            color="white",
            icon=ft.Icons.SEND,
            width=200
        )
    ], spacing=15, horizontal_alignment="center")

    # قسم التواصل
    contact_section = ft.Column([
        ft.Text("تواصل معنا", size=20, weight="bold", color=primary_color),
        ft.Row([whatsapp_btn, call_btn], alignment="center", spacing=10),
        ft.Container(facebook_btn, alignment=ft.alignment.center),
        ft.Text("متاحون للرد على استفساراتكم يومياً من 8 صباحاً إلى 10 مساءً", 
                size=14, color="gray", text_align="center")
    ], spacing=15, horizontal_alignment="center")

    # تذييل الصفحة
    footer = ft.Column([
        ft.Divider(),
        ft.Text("بيت النظافة © 2025", size=14, color="gray", text_align="center"),
        ft.Text("جميع الحقوق محفوظة", size=12, color="gray", text_align="center")
    ], spacing=10, horizontal_alignment="center")

    # إضافة المحتوى للصفحة
    page.add(
        ft.Column([
            header,
            ft.Divider(),
            services_section,
            ft.Divider(),
            features_section,
            ft.Divider(),
            request_form,
            ft.Divider(),
            contact_section,
            footer
        ], 
        spacing=25,
        scroll="auto")
    )

if __name__ == "__main__":
    ft.app(target=main)
