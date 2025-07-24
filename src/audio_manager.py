"""Audio management module for Pymath calculator."""

import pygame
import threading
import time
from .config import (
    MUSIC_PATH, CLICK_SOUND_PATH, DEVIL_SOUND_PATH, SOUNDTRACK_PATH
)


class AudioManager:
    """Manages all audio functionality for the calculator."""
    
    def __init__(self):
        """Initialize the audio manager."""
        self.should_play_background = True
        self._initialize_pygame()
        self._load_sounds()
    
    def _initialize_pygame(self):
        """Initialize pygame mixer."""
        try:
            pygame.mixer.init()
        except Exception as e:
            print(f"Error initializing pygame mixer: {e}")
    
    def _load_sounds(self):
        """Load all sound files."""
        try:
            self.click_sound = pygame.mixer.Sound(CLICK_SOUND_PATH)
            self.click_sound.set_volume(1.0)
            
            self.devil_sound = pygame.mixer.Sound(DEVIL_SOUND_PATH)
            self.devil_sound.set_volume(1.0)
            
            self.soundtrack = pygame.mixer.Sound(SOUNDTRACK_PATH)
            self.soundtrack.set_volume(1.0)
            
            self.devil_channel = pygame.mixer.Channel(1)
            self.soundtrack_channel = pygame.mixer.Channel(2)
            
        except Exception as e:
            print(f"Error loading sounds: {e}")
            self._set_sounds_to_none()
    
    def _set_sounds_to_none(self):
        """Set all sound objects to None if loading fails."""
        self.click_sound = None
        self.devil_sound = None
        self.soundtrack = None
        self.devil_channel = None
        self.soundtrack_channel = None
    
    def play_click_sound(self):
        """Play button click sound."""
        try:
            if self.click_sound:
                self.click_sound.play()
        except Exception as e:
            print(f"Error playing click sound: {e}")
    
    def play_devil_sound(self):
        """Play devil sound effect."""
        try:
            if self.devil_sound and self.devil_channel:
                self.devil_channel.play(self.devil_sound)
        except Exception as e:
            print(f"Error playing devil sound: {e}")
    
    def play_soundtrack_loop(self):
        """Play soundtrack in loop."""
        try:
            if self.soundtrack and self.soundtrack_channel:
                self.soundtrack_channel.play(self.soundtrack, loops=-1)
        except Exception as e:
            print(f"Error playing soundtrack: {e}")
    
    def play_background_music(self):
        """Play background music for 10 seconds."""
        try:
            if not pygame.mixer.get_init():
                return
                
            pygame.mixer.music.load(MUSIC_PATH)
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
            
            time.sleep(10)
            pygame.mixer.music.stop()
            
        except Exception as e:
            print(f"Error playing background music: {e}")
    
    def start_background_music_loop(self):
        """Start background music loop in a separate thread."""
        music_thread = threading.Thread(target=self._music_loop, daemon=True)
        music_thread.start()
    
    def _music_loop(self):
        """Background music loop."""
        while self.should_play_background:
            self.play_background_music()
            time.sleep(1)
    
    def stop_background_music(self):
        """Stop background music."""
        self.should_play_background = False
        try:
            pygame.mixer.music.stop()
        except Exception as e:
            print(f"Error stopping background music: {e}")