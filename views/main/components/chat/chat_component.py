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

    def __init__(self, text: str):
        super().__init__()
        self.text = text

        self.children = [
            rx.box(
                rx.flex(
                    rx.box(
                        rx.text(self.text),
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

    def show(self):
        return rx.scroll_area(
            rx.box(
                rx.center(
                    rx.box(
                        rx.foreach(
                            ChatState.chats,
                            lambda chat: rx.vstack(
                                self.user_box(chat[0]),
                                self.answer_box(chat[1]),
                                width="100%",
                            ),
                        ),
                        width="55%",
                        padding="20px 0px 20px 0",
                    )
                ),
                width="100%",
                height="100%",
            )
        )
