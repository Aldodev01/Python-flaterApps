import flet as ft
from flet import AppBar, ElevatedButton, Page, Text, View, colors 
import os

 
def Test(e):
    dlg = ft.AlertDialog(
        title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        Page.update()

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=close_dlg),
            ft.TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dialog dismissed!"),
    )

    def open_dlg(e):
        Page.dialog = dlg
        dlg.open = True
        Page.update()

    def open_dlg_modal(e):
        Page.dialog = dlg_modal
        dlg_modal.open = True
        Page.update()

    return e.views.append(
        View(
            "/test",
            [
                AppBar(
                    title=Text("restart"), bgcolor=colors.SURFACE_VARIANT
                    ),
                ElevatedButton("Catalog", on_click=osRestart),
                Text("test!"),
                ft.ElevatedButton("Open dialog", on_click=open_dlg),
                ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
                ],
            
            )
        )
        
def osRestart():
    os.system("shutdown /r /t 1")