import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة الرئيسية للواجهة
    page.title = "تطبيق إدارة المهام التفاعلي"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.theme_mode = ft.ThemeMode.DARK # يمكنك تحويله لـ DARK

    # حقل إدخال المهام الجديدة
    new_task_input = ft.TextField(
        hint_text="ما هي مهمتك القادمة؟",
        expand=True,
        border_color=ft.Colors.BLUE_400,
        focused_border_color=ft.Colors.BLUE_700,
    )

    # حاوية عرض قائمة المهام
    tasks_list_view = ft.ListView(
        expand=True,
        spacing=10,
        padding=20
    )

    # دالة حذف مهمة محددة
    def delete_task(task_row):
        tasks_list_view.controls.remove(task_row)
        page.update()

    # دالة إضافة مهمة جديدة
    def add_task_click(e):
        if not new_task_input.value.strip():
            return # تجنب إضافة حقول فارغة
        
        # إنشاء سطر المهمة بشكل تصريحي حديث
        task_row = ft.Row()
        task_text = ft.Checkbox(label=new_task_input.value, expand=True)
        delete_button = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            icon_color=ft.Colors.RED_400,
            on_click=lambda _: delete_task(task_row)
        )
        
        task_row.controls = [task_text, delete_button]
        
        # إضافة السطر للقائمة وإعادة تهيئة الحقل
        tasks_list_view.controls.append(task_row)
        new_task_input.value = ""
        page.update()

    # زر الإضافة الأزرق
    add_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD,
        foreground_color=ft.Colors.BLUE_600,
        focus_color=ft.Colors.WHITE,
        on_click=add_task_click
    )

    # تجميع عناصر الواجهة وهيكلتها داخل كارت مركزي
    page.add(
        ft.Container(
            width=500,
            height=600,
            margin=30,
            bgcolor=ft.Colors.BLACK_38,
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=15, color=ft.Colors.BLACK12),
            padding=20,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "قائمة المهام اليومية",
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_800
                    ),
                    ft.Divider(height=20, color=ft.Colors.BLUE_100),
                    ft.Row(
                        controls=[new_task_input, add_button],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),
                    ft.Container(height=20),
                    tasks_list_view
                ]
            )
        )
    )

# تشغيل التطبيق بنظام الويب وسطح المكتب معاً
ft.run(main)
