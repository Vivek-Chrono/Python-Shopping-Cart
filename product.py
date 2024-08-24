# ecommerce_app.py
import tkinter as tk
from tkinter import messagebox
from product import Product
from cart_item import CartItem
from shopping_cart import ShoppingCart

class ECommerceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("E-commerce Shopping Cart")
        self.cart = ShoppingCart()

        # Updated product list with prices in rupees
        self.products = [
            Product(1, "Laptop", 82000.00),       # Updated prices in INR
            Product(2, "Smartphone", 50000.00),
            Product(3, "Headphones", 4000.00),
            Product(4, "Tablet", 20000.00),
            Product(5, "Smartwatch", 15000.00),
            Product(6, "Camera", 35000.00)
        ]

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Product List
        tk.Label(self.root, text="Products").grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Increase the width and height of Listbox
        self.product_listbox = tk.Listbox(self.root, width=50, height=10)
        self.product_listbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        for product in self.products:
            self.product_listbox.insert(tk.END, f"{product.get_name()} - ₹{product.get_price():,.2f}")  # Use rupee symbol here

        # Quantity Entry
        tk.Label(self.root, text="Quantity").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=3, column=0, padx=10, pady=5, sticky="w")

        # Add to Cart Button
        self.add_to_cart_button = tk.Button(self.root, text="Add to Cart", command=self.add_to_cart)
        self.add_to_cart_button.grid(row=4, column=0, padx=10, pady=5, sticky="w")

        # View Cart Button
        self.view_cart_button = tk.Button(self.root, text="View Cart", command=self.view_cart)
        self.view_cart_button.grid(row=5, column=0, padx=10, pady=5, sticky="w")

        # Checkout Button
        self.checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout)
        self.checkout_button.grid(row=6, column=0, padx=10, pady=5, sticky="w")

        # Configure row and column weights to allow resizing
        self.root.grid_rowconfigure(1, weight=1)  # Make row 1 

