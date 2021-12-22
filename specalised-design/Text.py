# this is the design you're more likely to implement - knowing about the GUI class where
# you need to implement, natural to design text class with the GUI in mind. 

# for specialised design, we want to have the cursor as its own separate class
# passing cursor as an argument to delete? Or actually, having cursor attribute and
# methods is just as bad?

# this design is a lot longer than for general purpose, but with what benefit? 
# the interface within the class (all the methods) is great here, and there are
# a lot more methods, but it doesn't make life that much easier for the caller
# and crucially, this class is more difficult to understand. 

# important way to think about cognitive load: our goal is to reduce the complexity 
# of the system as a whole. That means here, and with the caller. In the specialised
# design, we are decreasing complexity (only slightly) for the caller, and we are 
# increasing it substantially here. Better to increase complexity slightly for the 
# caller, but to make it substantially simpler here. 

# on change, less information leakage, design decisions contained to one place (this adds up over time).
# Also, if you wish to use the class for another purpose you can (not the main reason, 
# not as common a benefit but still worth mentioning).
# example of a change: creating a new interface operation (like space), in specialised design
# means we need to define a new method. In general purpose design, we could just use insert method.

class Text:
    def __init__(self):
        self._text = ''
        self._cursor_position = 0

    def insert_char(self, char):
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

                

