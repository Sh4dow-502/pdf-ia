import reflex as rx
from states import ChatState


class UserQuestionBox(rx.Component):
    def __init__(self, text: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text

        self.children = [
            rx.box(
                rx.flex(
                    rx.box(
                        rx.text(self.text),
                        text_align="right",
                        max_width="100%",
                        padding="15px",
                        border_radius="15px",
                        background_color="var(--box-chat)",
                    ),
                ),
                width="100%",
                display="flex",
                justify_content="flex-end",
            )
        ]


class AnswerBox(rx.Component):
    def __init__(self, process_text, answer_text):
        super().__init__()
        self.process_text = process_text
        self.answer_text = answer_text

        self.children = [
            rx.box(
                rx.flex(
                    rx.box(
                        rx.text(
                            self.process_text,
                            rx.text(self.answer_text, color="white"),
                            color_scheme="gray",
                        ),
                        text_align="left",
                        max_width="100%",
                    )
                ),
                width="100%",
                display="flex",
                justify_content="flex-start",
            ),
        ]


class ChatComponent:
    user_box = UserQuestionBox
    answer_box = AnswerBox
    chats = ChatState.chats

    def show_boxs(self):
        return rx.foreach(
            ChatState.chats,
            lambda data: rx.vstack(
                self.user_box(data[0]),
                self.answer_box(data[1], data[2]),
                width="100%",
            ),
        )

    def show(self):
        return rx.scroll_area(
            rx.box(
                rx.center(
                    rx.box(
                        self.show_boxs(),
                        width="55%",
                        padding="20px 0px 20px 0",
                    )
                ),
                width="100%",
                height="100%",
            )
        )
