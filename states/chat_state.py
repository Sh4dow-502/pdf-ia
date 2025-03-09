import reflex as rx
import ollama


class ChatState(rx.State):
    user_chat_index: int = 0
    answer_chat_index: int = 1
    start_chat: bool = False
    mode: int = 0
    chats: list[list] = []

    @rx.event
    def enable_chat(self):
        self.start_chat = True

    @rx.event
    def add_chat(self, question):
        self.start_chat = True
        data = [question, "", ""]
        self.chats.append(data)

        index_data = len(self.chats) - 1
        if len(self.chats) == 0:
            index_data += 1

        chat = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[
                {"role": "user", "content": question},
            ],
            stream=True,
        )

        for i in chat:
            response = i.message.content

            if self.mode == 1:
                self.chats[index_data][2] += response
                self.chats[index_data][1] = ""
            else:
                self.chats[index_data][1] += response
            if (
                response == "**"
                or response == "<answer>"
                or response == f"ANSWER{index_data}"
                or response == "</think>"
            ):
                self.mode = 1

            yield

        self.mode = 0
