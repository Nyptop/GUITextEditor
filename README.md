# GUITextEditor
Building a GUI text editor with two designs. One has a Text class that is 'specialised' to the user interface. The other has a more 'general purpose' text class. Inspiration comes from Chapter 6 of John Ousterhout's book 'A Philosophy of Software Design'.

Three guiding questions to achieve a good, general purpose design:

1. What is the simplest interface that will cover all my current needs?
2. In how many situations will this method be used?
3. Is this API easy to use for my current needs?

----

specialised is the design you're more likely to implement - knowing about the GUI class where
you need to implement, natural to design text class with the GUI in mind. 

for specialised design, we want to have the cursor as its own separate class
passing cursor as an argument to delete? Or actually, having cursor attribute and
methods is just as bad?

I would really encourage you to try to make this yourself, initially

this design is a lot longer than for general purpose, but with what benefit? 
the interface within the class (all the methods) is great here, and there are
a lot more methods, but it doesn't make life that much easier for the caller
and crucially, this class is more difficult to understand. 

important way to think about cognitive load: our goal is to reduce the complexity 
of the system as a whole. That means here, and with the caller. In the specialised
design, we are decreasing complexity (only slightly) for the caller, and we are 
increasing it substantially here. Better to increase complexity slightly for the 
caller, but to make it substantially simpler here. 

on change, less information leakage, design decisions contained to one place (this adds up over time).
Also, if you wish to use the class for another purpose you can (not the main reason, 
not as common a benefit but still worth mentioning). In specialised design, every change
you want to make to UI, you end up having to edit the text class as well. Likely you may forget
to do this and bugs creep in. You may think, what's the big deal, but complexity is incremental. 
Only a zero tolerance policy will avoid. 
example of a change: creating a new interface operation (like space), in specialised design
means we need to define a new method. In general purpose design, we could just use insert method.

cognitive load, worse in this specialised example, and if you extend to other features, (undo, redo, size, font)
you basically get a class with hundreds of very shallow methods

### on cursor left in specialised design
should displaying the cursor be done in the text class?
again, this is specialised: means that text class expects
to be used by a user interface if it has this method for cursor movement. 
this method doesn't hide much info, simply calling just as complex for caller
as it would be to update the variable. 

### on delete in specialised design
this is quite a shallow class and is also very similar to backspace

### on get text method in specialised design 
this doesn't seem especially general purpose, we have the length of the line we want in browser
also, exposes data structure of list, information leakage, if we change from list, we have problems. 

## on moving lines logic out of text class 
it makes sense to move this logic here (or into UI class) and make the text class more
general purpose. Does the text class need to have a concept of line
length? No, this is something visual, so belongs to the user 
interface. 

You could say this is bad for information hiding, but having it in text also bad for info hiding
because info has been leaked to text about the UI if we put the code below in text class. 