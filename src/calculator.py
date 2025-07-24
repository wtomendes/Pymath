"""Main calculator module for Pymath."""

import tkinter as tk
from .audio_manager import AudioManager
from .ui_effects import UIEffects
from .calculator_logic import CalculatorLogic
from .ui_components import UIComponents


class PymathCalculator:
    """Main calculator class that coordinates all components."""
    
    def __init__(self):
        """Initialize the calculator application."""
        self.root = tk.Tk()
        
        # Initialize components
        self.audio_manager = AudioManager()
        self.ui_effects = UIEffects(self.root)
        self.ui_components = UIComponents(self.root)
        
        # Create UI elements
        self.entry = self.ui_components.create_entry()
        self.result_label = self.ui_components.create_result_label()
        
        # Initialize calculator logic
        self.calculator_logic = CalculatorLogic(
            self.audio_manager,
            self.ui_effects,
            self.result_label
        )
        
        # Create buttons
        self.ui_components.create_buttons(self.handle_button_click)
        
        # Start background music
        self.audio_manager.start_background_music_loop()
    
    def handle_button_click(self, value):
        """Handle calculator button clicks.
        
        Args:
            value: The button value that was clicked
        """
        self.audio_manager.play_click_sound()
        
        if value == 'C':
            self.entry.delete(0, tk.END)
        elif value == '=':
            expression = self.entry.get()
            self.calculator_logic.calculate(expression)
        else:
            self.entry.insert(tk.END, value)
    
    def run(self):
        """Start the calculator application."""
        self.root.mainloop()