import tkinter as tk

###############################################################################
#
# In this module, all of the _todo_ items will be in one comment because you
# will be modifying the same block of code as you go.
#
# TODO: 1. (1 pt)
#
#   First, create a tkinter window called window.
#
#   Make sure you call window's mainloop() method so your window will show up
#   when you run this module.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# TODO: 2. (4 pts)
#
#   Now, we are going to practice all of our widgets.
#
#   First, create two different frames.
#
#   Next, place widgets in both frames. Your frames should have these widgets
#   in them:
#
#       - Frame 1
#           - Label
#           - Button
#           - Single Line Text Entry
#       - Frame 2
#           - Label
#           - Multi Line Text Entry
#
#   You choose what text to have in the labels and button.
#
#   Make sure you call the pack method on all your widgets and that each widget
#   is in the proper frame.
#   
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

import tkinter as tk

window = tk.Tk()

frm_a=tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)
frm_b=tk.Frame(master=window, relief=tk.GROOVE, borderwidth=5)

lbl_a=tk.Label(master=frm_a, text="Frame A", bg="red")
lbl_a.pack()
button1 = tk.Button(
    master=frm_a, 
    text="Click here!"
)
button1.pack()
entry1=tk.Entry(master=frm_a,)
entry1.pack()

lbl_b=tk.Label(master=frm_b, text="Frame B", bg="purple")
lbl_b.pack()
text_box=tk.Text(master=frm_b)
text_box.pack()

frm_a.pack()
frm_b.pack()

border_effects={
    "flat":tk.FLAT, 
    "sunken":tk.SUNKEN, 
    "raised":tk.RAISED,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE
}

window.mainloop()

