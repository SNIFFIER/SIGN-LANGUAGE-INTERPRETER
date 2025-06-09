import tkinter as tk
from PIL import Image, ImageTk

class \
        SignLanguageInterpreterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Sign Language Interpreter")

        # Set the size of the window
        master.geometry("500x400")  # Set width to 800 pixels and height to 700 pixels

        # Create a Canvas widget for the background image
        self.canvas = tk.Canvas(master, width=1000, height=5000)
        self.canvas.pack()

        # Load the background image
        self.background_image = Image.open("C:/Users/karan/Downloads/Black & White Wallpaper.png")
        self.background_image = self.background_image.resize((800, 700))  # Resize the image to fit the window
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Place the background image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        # Create labels
        self.label = tk.Label(master, text="WELCOME TO", font=("Arial", 16), bg="white")
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Create entry for user input
        #self.entry = tk.Entry(master, font=("Arial", 16))
        #self.entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        #Create space for displaying interpreted text
        self.interpretation_label = tk.Label(master, text="SIGN LANGUAGE INTERPRETER", font=("Arial", 20), bg="white")  # Increase font size
        self.interpretation_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        # Create space for displaying image
        #self.image_label = tk.Label(master, bg="white")
        #self.image_label.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        # Create four buttons

        self.button1 = tk.Button(master, text="SCAN", font=("Arial", 14), height=1, width=13, command=self.button1_clicked)
        self.button1.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

        self.button2 = tk.Button(master, text="CREATE", font=("Arial", 14), height=1, width=13, command=self.button2_clicked)
        self.button2.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

        self.button3 = tk.Button(master, text="TRAIN", font=("Arial", 14), height=1, width=13, command=self.button3_clicked)
        self.button3.place(relx=0.25, rely=0.7, anchor=tk.CENTER)

        self.button4 = tk.Button(master, text="INTERPRETER", font=("Arial", 14), height=1, width=13, command=self.button4_clicked)
        self.button4.place(relx=0.75, rely=0.7, anchor=tk.CENTER)

#for additional button
        #self.button5 = tk.Button(master, text="NEW SCAN", font=("Arial", 14), height=1, width=13, command=self.button5_clicked)
        #self.button5.place(relx=0.25, rely=0.9, anchor=tk.CENTER)
    def button1_clicked(self):
        import collect_imgs
        return collect_imgs

    def button2_clicked(self):
        import create_dataset
        return create_dataset

    def button3_clicked(self):
        import train_classifier
        return train_classifier

    def button4_clicked(self):
        import final_classifier
        return final_classifier

#add the button when asked
    #def button5_clicked(self):
     #   import error_txt
      #  return error_txt

    def display_interpretation(self, interpretation):
        text, image_path = interpretation
        self.interpretation_label.config(text=text)

        # Display image
        image = Image.open(image_path)
        image = image.resize((400, 400))  # Increase image size
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo

def main():
    root = tk.Tk()
    app = SignLanguageInterpreterGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
