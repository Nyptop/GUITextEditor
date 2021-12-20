class Text:
    def __init__(self):
        self._text = ''
        self._cursor_position = 0

    def insert(self, position, char):
        self._text += char

    def delete(self, start_position, end_position):
        # deletes position immediately to the right of the cursor
        self._text = self._text[:self._cursor_position] + self._text[self._cursor_position+1:]

    def cursor_left(self):
        # should I move some of this logic out as well? Cursor logic now in the user interface?
        if self._cursor_position > 0:
            self._cursor_position -= 1
            print(self._cursor_position)

    def cursor_right(self):
        if self._cursor_position <= len(self._text):
            self._cursor_position += 1
        print(self._cursor_position)

    def get_text(self):
        return self._text