import tkinter as tk
from PIL import Image, ImageTk

def close_window():
    root.destroy()

root = tk.Tk()
root.overrideredirect(True)  # Supprime la bordure de la fenêtre

# Charger l'image avec PIL pour la manipulation
image_path = "image.png"
img = Image.open(image_path)

# Taille de la fenêtre
window_width = 1000  # Largeur de la fenêtre
window_height = 500  # Hauteur de la fenêtre

# Redimensionner l'image pour s'adapter à la taille de la fenêtre
img = img.resize((window_width, window_height))

# Convertir l'image PIL en format ImageTk pour l'afficher dans Tkinter
img = ImageTk.PhotoImage(img)

# Créer un canvas pour afficher l'image
canvas = tk.Canvas(root, width=window_width, height=window_height, highlightthickness=0)
canvas.pack()

# Afficher l'image au centre de la fenêtre
image_display = canvas.create_image(0, 0, anchor=tk.NW, image=img)

# Créer un bouton Close en bas à droite
button_close = tk.Button(root, text="Close", command=close_window)
button_close_window = canvas.create_window(window_width - 70, window_height - 30, anchor=tk.SE, window=button_close)

root.geometry(f"{window_width}x{window_height}")  # Définit la taille de la fenêtre

root.mainloop()
