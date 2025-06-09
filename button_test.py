import tkinter as tk

# Create a tkinter window
root = tk.Tk()

# Set the size of the window using geometry method
root.geometry("400x300")  # Width x Height

# Add a background image
background_image = tk.PhotoImage(file="C:/Users/karan/OneDrive/Desktop/download.png")  # Change "background_image.png" to your image file
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Expand to fill the window

# Add a heading
heading_label = tk.Label(root, text="My GUI Application", font=("Helvetica", 20))desi49 masa malu shraddhas_pr, preetir9838,11pm live .adult_ritu, im_maya_aa,nudeart110
heading_label.pack(pady=20)  # Add space around the heading

# Define functions to be called when buttons are clicked
# Define functions to be called when buttons are clicked
def button1_click():
    import collect_imgs
    return collect_imgs

def button2_click():
    import create_dataset
    return create_dataset

def button3_click():
    import train_classifier
    return train_classifier

def button4_click():
    import final_classifier
    return final_classifier

# Create buttons
button1 = tk.Button(root, text="collect", command=button1_click)
button2 = tk.Button(root, text="create", command=button2_click)
button3 = tk.Button(root, text="train", command=button3_click)
button4 = tk.Button(root, text="final", command=button4_click)

# Arrange buttons on the window using grid layout
button1.grid(row=1, column=2, padx=20, pady=10)
button2.grid(row=2, column=2, padx=20, pady=10)
button3.grid(row=3, column=2, padx=20, pady=10)
button4.grid(row=4, column=2, padx=20, pady=10)

# Start the tkinter event loop
root.mainloop()
