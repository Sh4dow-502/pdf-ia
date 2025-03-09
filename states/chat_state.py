import reflex as rx


class ChatState(rx.State):
    user_chat_index: int = 0
    answer_chat_index: int = 1
    start_chat: bool = False

    chats: list[tuple[str, str]] = []

    @rx.event
    def enable_chat(self):
        self.start_chat = True

    @rx.event
    def add_chat(self, data: tuple[str, str]):
        if data[0]:
            self.chats.append(data)
            self.start_chat = True
