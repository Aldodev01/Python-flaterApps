import flet
from flet import AppBar, ElevatedButton, Page, Text, View, colors 
 
def Catalogs(e):
        return e.views.append(
                View(
                    "/catalogs",
                    [
                        AppBar(
                            title=Text("Catalogs"), bgcolor=colors.SURFACE_VARIANT
                        ),
                        Text("Catalogs!"),
                    ],
                )
            )