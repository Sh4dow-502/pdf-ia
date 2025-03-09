import reflex as rx
from views import MainView


@rx.page(route="/", title="Home")
def index() -> rx.Component:

    view = MainView()
    return view.show_view()


app = rx.App(
    stylesheets=["/custom_violet.css", "/fonts/myfont.css"],
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        accent_color="violet",
    ),
)
