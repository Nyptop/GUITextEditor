# for specialised design, we want to have the cursor as its own separate class

class Text:
    def __init__(self):
        self._text = ''
        self._cursor_position = 0

    def add_char(self, char):
        self._text += char

    def backspace(self):
        # deletes position immediately to the left of the cursor
        self._text = self._text[:max(self._cursor_position - 1, 0)] + self._text[self._cursor_position:]
        if self._cursor_position > 0:
            self._cursor_position -= 1

    def delete(self):
        # deletes position immediately to the right of the cursor
        self._text = self._text[:self._cursor_position] + self._text[self._cursor_position+1:]

    def cursor_left(self):
        if self._cursor_position > 0:
            self._cursor_position -= 1
            print(self._cursor_position)

    def cursor_right(self):
        if self._cursor_position <= len(self._text):
            self._cursor_position += 1
        print(self._cursor_position)

    def get_text(self):
        # outputs text in lines of length 30
        # interesting interplay between info hiding and gen purp
        # should I specify line length in the interface, or have it as an attribute in this class (better for info hiding)
        # or, to keep module general purpose, should I handle multiple lines in UI (ie just return one long string)? 
        # To answer, consider 3 guiding questions in README
        lines = ['']
        for index, char in enumerate(self._text):
            if index % 30 == 0:
                lines.append('')
            if self._cursor_position == index:
                char = 'a'
            lines[-1] += char
        return lines
                

