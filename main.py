import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

class ShoppingCartApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shopping Cart Application")
        
        # Sample Products with details
        self.products = {
            "Laptop": {"price": 50000.0, "description": "High performance laptop with 16GB RAM and 512GB SSD.", "image": "laptop.png"},
            "Smartphone": {"price": 20000.0, "description": "Latest smartphone with a 6.5-inch display and 128GB storage.", "image": "smartphone.png"},
            "Tablet": {"price": 15000.0, "description": "Portable tablet with 10-inch display and 64GB storage.", "image": "tablet.png"},
            "Headphones": {"price": 3000.0, "description": "Wireless headphones with noise cancellation.", "image": "headphones.png"},
            "Smartwatch": {"price": 8000.0, "description": "Smartwatch with fitness tracking and notifications.", "image": "smartwatch.png"},
            "Keyboard": {"price": 1500.0, "description": "Mechanical keyboard with customizable keys.", "image": "keyboard.png"},
            "Mouse": {"price": 1000.0, "description": "Ergonomic mouse with high precision.", "image": "mouse.png"},
            "Monitor": {"price": 12000.0, "description": "27-inch monitor with 4K resolution.", "image": "monitor.png"}
        }
        
        self.cart = {}
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frames for layout
        self.frame_left = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_left.pack(side=tk.LEFT, padx=10, pady=10)
        
        self.frame_right = tk.Frame(self.root, bg="#f0f0f0")
        self.frame_right.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Product List
        self.product_listbox = tk.Listbox(self.frame_left, height=15, width=50, bg="#ffffff", fg="#333", selectmode=tk.SINGLE)
        self.product_listbox.pack(pady=10)
        
        for product in self.products.keys():
            self.product_listbox.insert(tk.END, product)
        
        self.product_listbox.bind('<<ListboxSelect>>', self.show_product_details)
        
        # Cart List
        self.cart_listbox = tk.Listbox(self.frame_right, height=15, width=50, bg="#ffffff", fg="#333")
        self.cart_listbox.pack(pady=10)
        
        # Add to Cart Button
        self.add_to_cart_button = tk.Button(self.frame_right, text="Add to Cart", command=self.add_to_cart, bg="#4CAF50", fg="white")
        self.add_to_cart_button.pack(pady=5)
        
        # Checkout Button
        self.checkout_button = tk.Button(self.frame_right, text="Checkout", command=self.checkout, bg="#FF5722", fg="white")
        self.checkout_button.pack(pady=5)
        
        # Product Detail Labels
        self.product_image = tk.Label(self.frame_left)
        self.product_image.pack(pady=10)
        
        self.product_name_label = tk.Label(self.frame_left, font=("Arial", 16, "bold"))
        self.product_name_label.pack(pady=5)
        
        self.product_price_label = tk.Label(self.frame_left, font=("Arial", 14))
        self.product_price_label.pack(pady=5)
        
        self.product_description_label = tk.Label(self.frame_left, wraplength=400, justify="left")
        self.product_description_label.pack(pady=5)
    
    def show_product_details(self, event):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            details = self.products[selected_product]
            self.product_name_label.config(text=selected_product)
            self.product_price_label.config(text=f"Price: ₹{details['price']:.2f}")
            self.product_description_label.config(text=details['description'])
            
            # Load and display product image with resizing
            image_path = details['image']
            if os.path.exists(image_path):
                try:
                    # Open and resize the image
                    img = Image.open(image_path)
                    img = img.resize((200, 200), Image.Resampling.LANCZOS)  # Resize image to 200x200 pixels
                    img_tk = ImageTk.PhotoImage(img)
                    
                    self.product_image.config(image=img_tk)
                    self.product_image.image = img_tk  # Keep a reference to avoid garbage collection
                except Exception as e:
                    print(f"Error loading image: {e}")
                    self.product_image.config(image="")
            else:
                print(f"Image file not found: {image_path}")
                self.product_image.config(image="")
    
    def add_to_cart(self):
        selected_product = self.product_listbox.get(tk.ACTIVE)
        if selected_product:
            if selected_product in self.cart:
                self.cart[selected_product] += 1
            else:
                self.cart[selected_product] = 1
            
            self.update_cart()
    
    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for product, quantity in self.cart.items():
            self.cart_listbox.insert(tk.END, f"{product} x{quantity}")
    
    def checkout(self):
        total = 0
        receipt = "Receipt:\n"
        
        for product, quantity in self.cart.items():
            price = self.products[product]['price']
            subtotal = price * quantity
            total += subtotal
            receipt += f"{product} x{quantity} @ ₹{price:.2f} each = ₹{subtotal:.2f}\n"
        
        receipt += f"\nTotal: ₹{total:.2f}"
        
        messagebox.showinfo("Checkout", receipt)
        self.cart.clear()
        self.update_cart()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShoppingCartApp(root)
    root.mainloop()
