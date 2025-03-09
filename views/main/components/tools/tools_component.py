import reflex as rx


class ToolsComponent:
    def show(self):

        return rx.box(
            rx.center(
                rx.box(
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "Herramientas",
                                font_family="Nunito Bold",
                                font_size="18px",
                            ),
                            width="100%",
                        ),
                        rx.hstack(
                            rx.card(
                                rx.vstack(
                                    rx.image(
                                        "svg/pdf.svg",
                                        width="55px",
                                        height="auto",
                                    ),
                                    rx.text("Traductor", font_family="Poppins Bold"),
                                    spacing="1",
                                    align="center",
                                ),
                                width="125px",
                                height="125px",
                                background_color="#9292c259",
                                cursor="pointer",
                                border_radius="20px",
                            ),
                            rx.foreach(
                                ["Optimizar", "Chat", "Convertir", "Other"],
                                lambda txt: rx.card(
                                    rx.vstack(
                                        rx.text(txt, font_family="Poppins Bold"),
                                        spacing="1",
                                        align="center",
                                        height="100%",
                                    ),
                                    width="125px",
                                    height="125px",
                                    background_color="#9292c259",
                                    cursor="pointer",
                                    border_radius="20px",
                                    opacity="0.4",
                                ),
                            ),
                            wrap="wrap",
                        ),
                        align="center",
                    ),
                    width="45%",
                )
            ),
            width="100%",
        )
