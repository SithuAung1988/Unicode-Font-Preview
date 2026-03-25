# Copyright (C) <2026>  <Sithu Aung> <https://github.com/SithuAung1988/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import flet as ft
from pathlib import Path


async def main(page: ft.Page):
    page.title = "Unicode Font Preview"
    page.width = 800
    page.height = 600

    page.window_resizable = False
    page.theme_mode = ft.ThemeMode.SYSTEM

    page.update()

    page.fonts = {}

    state = {
        "folder_path": None,
        "active_item": None,
    }

    sample_text = (
        "သီဟိုဠ်မှ ဉာဏ်ကြီးရှင်သည် အာယုဝဍ္ဎနဆေးညွှန်းစာကို ဇလွန်ဈေးဘေး ဗာဒံပင်ထက် အဓိဋ္ဌာန်လျက် ဂဃနဏဖတ်ခဲ့သည်။"
    )

    preview_text = ft.Text(value=sample_text, size=14, style=ft.TextStyle(height=1.8))

    dir_label = ft.Text(
        value="No folder selected...",
        size=16,
        color=ft.Colors.INVERSE_PRIMARY,
        no_wrap=True,
        margin=5,
        width=180,
    )

    theme_icon = ft.Icon(ft.Icons.BRIGHTNESS_AUTO_ROUNDED, size=30)

    def update_size(e):
        preview_text.size = e.control.value
        page.update()

    def update_text(e):
        preview_text.value = e.control.value
        page.update()

    file_list = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        expand=True,
    )

    async def handle_click(e):
        target_text = e.control.content.controls[1]

        if state["active_item"]:
            prev_text = state["active_item"].content.controls[1]
            prev_text.weight = None
            prev_text.italic = False
            prev_text.color = None

        target_text.weight = "bold"
        target_text.color = ft.Colors.PRIMARY

        state["active_item"] = e.control

        filename = target_text.value
        font_path = state["folder_path"] / filename
        font_id = f"f_{hash(str(font_path))}"
        page.fonts[font_id] = str(font_path.absolute())
        preview_text.font_family = font_id

        page.update()

    async def pick_folder(e):
        result = await ft.FilePicker().get_directory_path()
        if result:
            folder = Path(result)
            state["folder_path"] = folder
            state["active_item"] = None

            parent_name = folder.name
            if len(parent_name) > 15:
                dir_label.value = str(f"...{parent_name[-12:]}")
            else:
                dir_label.value = str(parent_name)

            dir_label.color = ft.Colors.PRIMARY

            file_list.controls.clear()

            font_files = [
                f
                for f in folder.iterdir()
                if f.is_file() and f.suffix.lower() in {".ttf", ".otf"}
            ]

            for f in sorted(font_files, key=lambda x: x.name):
                file_list.controls.append(
                    ft.Container(
                        on_click=handle_click,
                        padding=ft.Padding(left=10, top=2, bottom=2, right=10),
                        content=ft.Row(
                            [
                                ft.Icon(ft.Icons.FONT_DOWNLOAD_OUTLINED, size=18),
                                ft.Text(
                                    value=f.name,
                                    size=14,
                                    no_wrap=True,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=10,
                        ),
                    )
                )
        page.update()

    async def exit_app(e):
        await page.window.close()

    async def close_dlg(e):
        license_dialog.open = False
        page.update()

    async def show_license(e):
        license_dialog.open = True
        page.update()

    license_dialog = ft.AlertDialog(
        modal=False,
        title=ft.Text("Unicode Font Preview"),
        content=ft.Text(
            "Version : 0.0.1 (22032026)\n"
            "Build : Nuitka - AppleSilicon - 01\n"
            "Github: https://github.com/SithuAung1988/\n\n\n"
            "© 2024 Sithu Aung\n<https://github.com/SithuAung1988/>\n\n"
            "This software is licensed under the GPLv3 License.\n"
            "<https://www.gnu.org/licenses/gpl-3.0.html#license-text>\n",
            size=14,
        ),
        actions=[ft.TextButton("Close", on_click=close_dlg)],
    )
    page.overlay.append(license_dialog)

    def check_current_theme():
        # Check explicit settings first
        if page.theme_mode == ft.ThemeMode.LIGHT:
            return "light"
        elif page.theme_mode == ft.ThemeMode.DARK:
            return "dark"

        # If it's SYSTEM, use the platform brightness value
        # We add a fallback just in case platform_brightness is None
        try:
            return page.platform_brightness.value
        except AttributeError:
            return "light"

    async def toggle_theme_mode(e):
        # 1. Determine the CURRENT effective theme
        current = check_current_theme()

        # 2. Determine new settings
        if current == "light":
            page.theme_mode = ft.ThemeMode.DARK
            new_icon_name = ft.Icons.LIGHT_MODE_ROUNDED
            new_tooltip = "Switch to Light Mode"
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            new_icon_name = ft.Icons.DARK_MODE_ROUNDED
            new_tooltip = "Switch to Dark Mode"

        # 3. FIX: Replace the entire content with a NEW Icon object
        # This forces Flet to redraw the button's center
        e.control.content = ft.Icon(new_icon_name, size=30)
        e.control.tooltip = new_tooltip

        # 4. Refresh the UI (Standard sync update for your version)
        page.update()

    theme_button = ft.Button(
        content=theme_icon,
        style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=15),
        on_click=toggle_theme_mode,
        tooltip="Theme: System (Click to toggle)",
    )

    sidebar = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        dir_label,
                        ft.Button(
                            content=ft.Icon(ft.CupertinoIcons.FOLDER, size=30),
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=15),
                            on_click=pick_folder,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Divider(),
                file_list,
            ]
        ),
        width=250,
        padding=0,
        margin=ft.Margin.only(left=5, top=0, bottom=0, right=20),
    )

    preview_box = ft.Container(
        content=ft.Column(
            [preview_text],
            scroll=ft.ScrollMode.AUTO,
        ),
        padding=5,
        border_radius=5,
    )
    preview_box.height = 270

    main_content = ft.Container(
        content=ft.Column(
            [
                ft.CupertinoTextField(
                    value=sample_text,
                    on_change=update_text,
                    text_size=14,
                    multiline=True,
                    height=180,
                    width=480,
                    text_style=ft.TextStyle(height=2),
                ),
                ft.Row(
                    [
                        ft.Text(value="Font Size:", size=16),
                        ft.CupertinoSlider(
                            width=400,
                            min=8,
                            max=28,
                            value=14,
                            on_change=update_size,
                        ),
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                preview_box,
                ft.Row(
                    [
                        theme_button,
                        ft.Button(
                            content=ft.Icon(ft.Icons.INFO_OUTLINE_ROUNDED, size=30),
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=15),
                            on_click=show_license,
                            tooltip="About",
                        ),
                        ft.Button(
                            content=ft.Icon(ft.Icons.EXIT_TO_APP_OUTLINED, size=30),
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=15),
                            on_click=exit_app,
                            tooltip="Exit Application",
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.END,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=20,
                ),
            ]
        ),
        expand=True,
        padding=ft.Padding.only(left=10, top=0, bottom=0, right=10),
    )

    page.add(
        ft.Column(
            [
                ft.Row(
                    [sidebar, ft.VerticalDivider(width=1), main_content],
                    expand=True,
                    spacing=0,
                ),
            ],
            expand=True,
            spacing=0,
        )
    )


if __name__ == "__main__":
    ft.run(main, name="Unicode Font Preview")
