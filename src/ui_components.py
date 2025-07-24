"""UI components module for Pymath calculator."""

import tkinter as tk
from PIL import Image, ImageTk
from .config import (
    COLORS, BUTTON_STYLE, BUTTON_LAYOUT, SPECIAL_BUTTONS, 
    ICON_PATH, ICON_SIZES
)


class UIComponents:
    """Manages UI components for the calculator."""
    
    def __init__(self, root):
        """Initialize UI components.
        
        Args:
            root: The main tkinter window
        """
        self.root = root
        self._icons = []
        self._setup_window()
        self._setup_icon()
    
    def _setup_window(self):
        """Setup main window properties."""
        self.root.title("Pymath")
        self.root.configure(bg=COLORS['background'])
        self.root.resizable(False, False)
    
    def _setup_icon(self):
        """Setup window icon with multiple resolutions."""
        try:
            img = Image.open(ICON_PATH)
            for size in ICON_SIZES:
                resized = img.resize(size, Image.Resampling.LANCZOS)
                icon = ImageTk.PhotoImage(resized)
                self._icons.append(icon)
            self.root.iconphoto(True, *self._icons)
        except Exception as e:
            print(f"Could not load icon: {e}")
    
    def create_entry(self):
        """Create and return the calculator entry widget."""
        entry = tk.Entry(
            self.root,
            width=20,
            font=("Consolas", 22),
            justify="right",
            bg=COLORS['entry_bg'],
            fg=COLORS['entry_fg'],
            relief="flat"
        )
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        return entry
    
    def create_result_label(self):
        """Create and return the result label widget."""
        label = tk.Label(
            self.root,
            text="Resultado: ",
            font=("Consolas", 16),
            bg=COLORS['label_bg'],
            fg=COLORS['label_fg']
        )
        label.grid(row=1, column=0, columnspan=4, pady=5)
        return label
    
    def create_buttons(self, button_callback):
        """Create calculator buttons.
        
        Args:
            button_callback: Function to call when button is clicked
        """
        for text, row, col in BUTTON_LAYOUT:
            self._create_single_button(text, row, col, button_callback)
    
    def _create_single_button(self, text, row, col, callback):
        """Create a single calculator button.
        
        Args:
            text: Button text
            row: Grid row position
            col: Grid column position
            callback: Function to call when clicked
        """
        # Determine button color based on button type
        if text in SPECIAL_BUTTONS:
            bg_color = COLORS['button_secondary']
            fg_color = "black"
        else:
            bg_color = COLORS['button_primary']
            fg_color = "white"
        
        button = tk.Button(
            self.root,
            text=text,
            bg=bg_color,
            fg=fg_color,
            command=lambda: callback(text),
            **BUTTON_STYLE
        )
        
        button.grid(row=row, column=col, padx=5, pady=5)