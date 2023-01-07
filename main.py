import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors, AlertDialog, TextButton, MainAxisAlignment
from Catalogs import Catalogs
from Test import Test


def main(page: Page):
    page.title = "Routes Example"
    
    dlg = AlertDialog(
        title=Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
    )

    def close_dlg(e):
        dlg_modal.open = False
        Page.update()

    dlg_modal = AlertDialog(
        modal=True,
        title=Text("Please confirm"),
        content=Text("Do you really want to delete all those files?"),
        actions=[
            TextButton("Yes", on_click=close_dlg),
            TextButton("No", on_click=close_dlg),
        ],
        actions_alignment=MainAxisAlignment.END,
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

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(title=Text("Flet app")),
                    ElevatedButton("Catalog", on_click=open_catalogs),
                    ElevatedButton("Test", on_click=open_test),
                    ElevatedButton("Open dialog", on_click=open_dlg),
                    ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
                    
                    
                ],
            )
        )
        if page.route == "/settings" or page.route == "/settings/mail":
            page.views.append(
                View(
                    "/settings",
                    [
                        AppBar(title=Text("Settings"), bgcolor=colors.SURFACE_VARIANT),
                        Text("Settings!", style="bodyMedium"),
                        ElevatedButton(
                            "Go to mail settings", on_click=open_test
                        ),
                    ],
                )
            )
        if page.route == "/test":
            return Test(page)
        if page.route == '/catalogs':
            return Catalogs(page)
        page.update()
           
        
    def setting_mail(e):
        return page.views.append(
                View(
                    "/settings/mail",
                    [
                        AppBar(
                            title=Text("Mail Settings"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Mail settings!"),
                    ],
                )
            )
        

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop


    def open_catalogs(e):
        page.go("/catalogs")
    
    def open_test(e):
        page.go("/test")

    page.go(page.route)


flet.app(target=main, view=flet.WEB_BROWSER)