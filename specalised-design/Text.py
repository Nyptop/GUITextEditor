class Text:
    def __init__(self):
        self._text = ''
        self._cursor_position = 0

    def insert_char(self, char):
        self._text = self._text[:self._cursor_position] + char + self._text[self._cursor_position:]

    def backspace(self):
        # deletes character immediately to the left of the cursor
        self._text = self._text[:max(self._cursor_position - 1, 0)] + self._text[self._cursor_position:]
        if self._cursor_position > 0:
            self._cursor_position -= 1

    def delete(self):
        # deletes character immediately to the right of the cursor 
        self._text = self._text[:self._cursor_position] + self._text[self._cursor_position+1:]

    def cursor_left(self):
        if self._cursor_position > 0:
            self._cursor_position -= 1

    def cursor_right(self):
        if self._cursor_position <= len(self._text):
            self._cursor_position += 1

    def get_text(self):
        lines = ['']
        for index, char in enumerate(self._text):
            if index % 30 == 0:
                lines.append('')
            if self._cursor_position == index:
                char = ']' + char
            lines[-1] += char
        return lines

                

