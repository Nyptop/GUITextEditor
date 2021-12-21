# for specialised design, we want to have the cursor as its own separate class
# passing cursor as an argument to delete? Or actually, having cursor attribute and
# methods is just as bad?

class Text:
    def __init__(self):
        self._text = ''
        self._cursor_position = 0

    def insert(self, char):
        # using all these self. ... feels wrong, ask about this
        self._text = self._text[:self._cursor_position] + char + self._text[self._cursor_position:]

    def backspace(self):
        # deletes position immediately to the left of the cursor
        self._text = self._text[:max(self._cursor_position - 1, 0)] + self._text[self._cursor_position:]
        if self._cursor_position > 0:
            self._cursor_position -= 1

    def delete(self):
        # this is quite a shallow class and is also very similar to backspace
        # deletes position immediately to the right of the cursor
        self._text = self._text[:self._cursor_position] + self._text[self._cursor_position+1:]

    def cursor_left(self):
        # should displaying the cursor be done in the text class
        # again, this is specialised: means that text class expects
        # to be used by a user interface if it has this method for cursor movement. 
        # this method doesn't hide much info, simply calling just as complex for caller
        # as it would be to update the variable. 
        if self._cursor_position > 0:
            self._cursor_position -= 1
            print(self._cursor_position)

    def cursor_right(self):
        if self._cursor_position <= len(self._text):
            self._cursor_position += 1
        print(self._cursor_position)

    def get_text(self):
        # this doesn't seem especially general purpose, we have the length of the line we want in browser
        # also, exposes data structure of list, information leakage, if we change from list, we have problems. 
        lines = ['']
        for index, char in enumerate(self._text):
            if index % 30 == 0:
                lines.append('')
            if self._cursor_position == index:
                char = 'a'
            lines[-1] += char
        return lines
                

