import tkinter as tk

root = tk.Tk()
root.title("Text-Box Input")

label1 = tk.Label(root, text="Enter value 1:")
entry1 = tk.Entry(root)

label2 = tk.Label(root, text="Enter value 2:")
entry2 = tk.Entry(root)

label3 = tk.Label(root, text="Enter value 3:")
entry3 = tk.Entry(root)

entry1.config(width=30)
entry2.config(width=30)
entry3.config(width=30)

def get_values():
    val1 = entry1.get()
    val2 = entry2.get()
    val3 = entry3.get()
    print("Value 1:", val1)
    print("Value 2:", val2)
    print("Value 3:", val3)

submit_button = tk.Button(root, text="Submit", command=get_values)

label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
entry3.pack()
submit_button.pack()

root.mainloop()