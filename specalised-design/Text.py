class Text:
    def __init__(self):
        self._text = ''
        # for specialised design, we want to have the cursor as its own separate class
        self._cursor_position = 0

    def add_char(self, char):
        self._text += char

    def backspace(self):
        # deletes position immediately to the left of the cursor
        if self._cursor_position <= len(self._text):
            self._text.pop(self._cursor_position)

    def delete(self):
        # deletes position immediately to the right of the cursor
        if self._cursor_position < len(self._text):
            self._text.pop(self._cursor_position + 1)

    def get_text(self):
        # outputs text in lines of length ...
        # interesting interplay between info hiding and gen purp
        # should I specify line length in the interface, or have it as an attribute in this class (better for info hiding)
        # or, to keep module general purpose, should I handle multiple lines in UI (ie just return one long string)? 
        # To answer, consider 3 guiding questions in README
        pass