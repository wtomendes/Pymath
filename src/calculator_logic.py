"""Calculator logic module for Pymath calculator."""

import webbrowser
from tkinter import messagebox
from .config import EASTER_EGGS


class CalculatorLogic:
    """Handles calculator operations and easter eggs."""
    
    def __init__(self, audio_manager, ui_effects, result_label):
        """Initialize calculator logic.
        
        Args:
            audio_manager: AudioManager instance
            ui_effects: UIEffects instance
            result_label: tkinter Label for displaying results
        """
        self.audio_manager = audio_manager
        self.ui_effects = ui_effects
        self.result_label = result_label
    
    def calculate(self, expression):
        """Calculate the result of an expression.
        
        Args:
            expression: String expression to evaluate
        """
        try:
            if expression in EASTER_EGGS:
                self._handle_easter_egg(expression)
            else:
                result = eval(expression)
                self._display_normal_result(result)
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida!")
    
    def _handle_easter_egg(self, expression):
        """Handle easter egg expressions.
        
        Args:
            expression: The easter egg expression
        """
        egg_data = EASTER_EGGS[expression]
        
        if expression == "666+666":
            self._handle_devil_easter_egg(egg_data)
        elif expression == "1+1":
            self._handle_rickroll_easter_egg(egg_data)
    
    def _handle_devil_easter_egg(self, egg_data):
        """Handle the devil easter egg (666+666)."""
        self.audio_manager.stop_background_music()
        self.audio_manager.play_soundtrack_loop()
        self.audio_manager.play_devil_sound()
        self.ui_effects.flash_red()
        
        self.result_label.config(
            text=egg_data['message'],
            fg=egg_data['color'],
            font=("Consolas", 16, "bold")
        )
        
        messagebox.showwarning("WARNING", egg_data['warning'])
        self.ui_effects.root.after(100, self.ui_effects.stop_flash_and_stay_red)
    
    def _handle_rickroll_easter_egg(self, egg_data):
        """Handle the rickroll easter egg (1+1)."""
        self.audio_manager.stop_background_music()
        webbrowser.open(egg_data['url'])
        
        self.result_label.config(
            text=egg_data['message'],
            fg=egg_data['color'],
            font=("Consolas", 16, "bold")
        )
    
    def _display_normal_result(self, result):
        """Display normal calculation result.
        
        Args:
            result: The calculation result
        """
        self.result_label.config(
            text=f"Resultado: {result}",
            fg="white",
            font=("Consolas", 16)
        )