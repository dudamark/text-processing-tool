import re


class TextCleaner:
    def __init__(self, text):
        self.text = text

    def remove_extra_spaces(self):
        # remove múltiplos espaços
        self.text = re.sub(r'\s+', ' ', self.text).strip()
        return self

    def to_lowercase(self):
        # normaliza para minúsculas (APENAS PARA ANÁLISE)
        self.text = self.text.lower()
        return self

    def get_text(self):
        return self.text