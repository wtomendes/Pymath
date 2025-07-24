"""UI effects module for Pymath calculator."""

import tkinter as tk
from .config import COLORS


class UIEffects:
    """Manages visual effects for the calculator UI."""
    
    def __init__(self, root):
        """Initialize UI effects manager.
        
        Args:
            root: The main tkinter window
        """
        self.root = root
        self.should_flash = True
    
    def flash_red(self):
        """Start flashing the UI red."""
        self.should_flash = True
        self._toggle_red()
    
    def _toggle_red(self):
        """Toggle between red and normal colors."""
        if not self.root.winfo_exists() or not self.should_flash:
            return
            
        if self.root.cget("bg") == COLORS['red']:
            self._set_normal_colors()
        else:
            self._set_red_colors()
            
        self.root.after(500, self._toggle_red)
    
    def _set_normal_colors(self):
        """Set UI to normal colors."""
        self.root.configure(bg=COLORS['background'])
        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                if widget.cget("text") in {'C', '/', '*', '-', '+', '=', '0'}:
                    widget.configure(bg=COLORS['button_secondary'])
                else:
                    widget.configure(bg=COLORS['button_primary'])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=COLORS['entry_bg'])
            elif isinstance(widget, tk.Label):
                widget.configure(bg=COLORS['label_bg'])
    
    def _set_red_colors(self):
        """Set UI to red colors."""
        self.root.configure(bg=COLORS['red'])
        
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=COLORS['red_button'])
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=COLORS['red_entry'])
            elif isinstance(widget, tk.Label):
                widget.configure(bg=COLORS['red_label'])
    
    def stop_flash_and_stay_red(self):
        """Stop flashing and keep UI red."""
        self.should_flash = False
        self._set_red_colors()