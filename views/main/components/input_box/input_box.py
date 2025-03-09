import reflex as rx
from states import ChatState


class StateInput(rx.State):
    enable_send: bool = False
    length_text: int = 0
    value_input: str = ""

    @rx.event
    def submit_form(self, form_data: dict):
        text = form_data["input_chat"]
        self.value_input = ""
        self.length_text = 0
        return ChatState.add_chat(text)

    @rx.event
    def change_text(self, text):
        if text:
            self.enable_send = True
        else:
            self.enable_send = False
        self.value_input = text
        self.length_text = len(text)


class InputBoxComponent:
    def show(self):

        return rx.box(
            rx.center(
                rx.box(
                    rx.form(
                        rx.vstack(
                            rx.text_area(
                                id="input_chat",
                                placeholder="Escribe tu pregunta",
                                border="none",
                                outline="none",
                                max_height="300px",
                                resize="none",
                                overflow="hidden",
                                background="var(--box-chat)",
                                border_radius="10px",
                                auto_height=True,
                                variant="soft",
                                max_length=400,
                                width="100%",
                                enter_key_submit=True,
                                on_change=StateInput.change_text,
                                value=StateInput.value_input,
                            ),
                            rx.hstack(
                                rx.text(
                                    f"{StateInput.length_text}/400", color_scheme="gray"
                                ),
                                rx.button(
                                    rx.icon("send-horizontal"),
                                    width="43px",
                                    height="43px",
                                    border_radius="10px",
                                    color_scheme=rx.cond(
                                        StateInput.enable_send, "violet", "gray"
                                    ),
                                    opacity=rx.cond(StateInput.enable_send, "1", "0.3"),
                                    type="submit",
                                ),
                                justify="between",
                                width="100%",
                                align="end",
                            ),
                            justify="between",
                            height="100%",
                        ),
                        on_submit=StateInput.submit_form,
                    ),
                    width="55%",
                    background_color="var(--box-input-chat)",
                    border="1px solid #252525",
                    border_radius="15px",
                    max_height="400px",
                    padding="10px",
                    auto_height=True,
                )
            ),
            width="100%",
        )
