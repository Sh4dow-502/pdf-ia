import reflex as rx

from .components import ToolsComponent
from .components import InputBoxComponent
from .components import ChatComponent
from states import ChatState


class Info:
    @classmethod
    def title_page(cls):
        return rx.box(
            rx.center(
                rx.text(
                    "FIUSAC-X",
                    font_size="2em",
                    font_family="Montserrat Bold",
                )
            ),
            width="100%",
        )


class MainView:
    title_page = Info.title_page()
    tools_component = ToolsComponent().show()
    input_box = InputBoxComponent().show()
    chat_component = ChatComponent().show()

    def show_view(self) -> rx.Component:
        return rx.box(
            rx.center(
                rx.vstack(
                    self.title_page,
                    rx.cond(
                        ChatState.start_chat,
                        self.chat_component,
                        self.tools_component,
                    ),
                    self.input_box,
                    justify="between",
                    align="center",
                    height="100%",
                    width="100%",
                ),
                height="100%",
                width="100%",
            ),
            background="linear-gradient(to bottom, #211F4E 0%, #1D1C3F 10%, #191830 22%, #151520 40%, #131319 57%, #111111 80%)",
            height="100vh",
            width="100%",
            padding="18px 0px 18px 0px",
        )
