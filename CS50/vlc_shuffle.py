import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VLC Shuffle Simulation")

# Colors
BACKGROUND = (30, 30, 40)
TEXT = (220, 220, 220)
BUTTON = (70, 130, 180)
BUTTON_HOVER = (90, 150, 200)
HIGHLIGHT = (100, 200, 100)
PLAYING = (240, 100, 100)
PREVIOUS = (240, 180, 80)

# Fonts
font = pygame.font.SysFont("Arial", 20)
title_font = pygame.font.SysFont("Arial", 28, bold=True)

class Song:
    def __init__(self, title):
        self.title = title
        self.played = False
        
    def __str__(self):
        return self.title

class ShuffleSimulator:
    def __init__(self):
        self.songs = [Song(f"Song {i+1}") for i in range(10)]
        self.shuffled_order = []
        self.current_index = 0
        self.playback_history = []
        self.shuffle_mode = False
        
    def shuffle_songs(self):
        # Create a copy of the original songs and shuffle them
        self.shuffled_order = self.songs.copy()
        random.shuffle(self.shuffled_order)
        self.current_index = 0
        self.playback_history = []
        self.shuffle_mode = True
        
        # Mark all songs as not played
        for song in self.songs:
            song.played = False
            
    def play_next(self):
        if not self.shuffle_mode or not self.shuffled_order:
            return None
            
        if self.current_index < len(self.shuffled_order):
            current_song = self.shuffled_order[self.current_index]
            current_song.played = True
            self.playback_history.append(self.current_index)
            self.current_index += 1
            return current_song
            
        return None
        
    def play_previous(self):
        if not self.shuffle_mode or not self.playback_history:
            return None
            
        # VLC doesn't go back in playback history, but goes to the previous song in the shuffled list
        if self.current_index > 0:
            self.current_index -= 1
            return self.shuffled_order[self.current_index]
            
        return None
        
    def reset(self):
        self.shuffled_order = []
        self.current_index = 0
        self.playback_history = []
        self.shuffle_mode = False
        for song in self.songs:
            song.played = False

def draw_button(screen, x, y, width, height, text, hover=False):
    color = BUTTON_HOVER if hover else BUTTON
    pygame.draw.rect(screen, color, (x, y, width, height), border_radius=8)
    pygame.draw.rect(screen, (120, 120, 120), (x, y, width, height), 2, border_radius=8)
    
    text_surf = font.render(text, True, TEXT)
    text_rect = text_surf.get_rect(center=(x + width/2, y + height/2))
    screen.blit(text_surf, text_rect)
    
    return pygame.Rect(x, y, width, height)

def main():
    simulator = ShuffleSimulator()
    clock = pygame.time.Clock()
    
    # Button rectangles
    shuffle_btn_rect = pygame.Rect(50, 500, 150, 50)
    next_btn_rect = pygame.Rect(250, 500, 150, 50)
    prev_btn_rect = pygame.Rect(450, 500, 150, 50)
    reset_btn_rect = pygame.Rect(650, 500, 100, 50)
    
    current_song = None
    previous_song = None
    
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if shuffle_btn_rect.collidepoint(mouse_pos):
                    simulator.shuffle_songs()
                    current_song = None
                    previous_song = None
                    
                elif next_btn_rect.collidepoint(mouse_pos) and simulator.shuffle_mode:
                    previous_song = current_song
                    current_song = simulator.play_next()
                    
                elif prev_btn_rect.collidepoint(mouse_pos) and simulator.shuffle_mode:
                    previous_song = current_song
                    current_song = simulator.play_previous()
                    
                elif reset_btn_rect.collidepoint(mouse_pos):
                    simulator.reset()
                    current_song = None
                    previous_song = None
        
        # Draw background
        screen.fill(BACKGROUND)
        
        # Draw title
        title = title_font.render("VLC Shuffle Behavior Simulation", True, TEXT)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 20))
        
        # Draw description
        desc1 = font.render("This simulation demonstrates how VLC's shuffle creates a fixed random order,", True, TEXT)
        desc2 = font.render("and the 'Previous' button goes to the prior song in the shuffled list, not playback history.", True, TEXT)
        screen.blit(desc1, (WIDTH//2 - desc1.get_width()//2, 70))
        screen.blit(desc2, (WIDTH//2 - desc2.get_width()//2, 100))
        
        # Draw original playlist
        pygame.draw.rect(screen, (50, 50, 60), (50, 150, 300, 300), border_radius=10)
        title_orig = font.render("Original Playlist", True, TEXT)
        screen.blit(title_orig, (200 - title_orig.get_width()//2, 130))
        
        for i, song in enumerate(simulator.songs):
            color = TEXT
            if simulator.shuffle_mode and song.played:
                color = HIGHLIGHT
            text = font.render(f"{i+1}. {song.title}", True, color)
            screen.blit(text, (70, 170 + i*30))
        
        # Draw shuffled playlist
        pygame.draw.rect(screen, (50, 50, 60), (450, 150, 300, 300), border_radius=10)
        title_shuffled = font.render("Shuffled Playlist", True, TEXT)
        screen.blit(title_shuffled, (600 - title_shuffled.get_width()//2, 130))
        
        if simulator.shuffle_mode:
            for i, song in enumerate(simulator.shuffled_order):
                color = TEXT
                if song.played:
                    color = HIGHLIGHT
                if i == simulator.current_index - 1 and current_song == song:
                    color = PLAYING
                elif i == simulator.current_index - 1 and previous_song == song:
                    color = PREVIOUS
                    
                text = font.render(f"{i+1}. {song.title}", True, color)
                screen.blit(text, (470, 170 + i*30))
        
        # Draw playback info
        pygame.draw.rect(screen, (50, 50, 60), (200, 470, 400, 80), border_radius=10)
        
        if current_song:
            now_playing = font.render(f"Now Playing: {current_song.title}", True, PLAYING)
            screen.blit(now_playing, (WIDTH//2 - now_playing.get_width()//2, 480))
        
        if previous_song and current_song != previous_song:
            previous_text = font.render(f"Previous in playback: {previous_song.title}", True, PREVIOUS)
            screen.blit(previous_text, (WIDTH//2 - previous_text.get_width()//2, 510))
        
        # Draw buttons
        shuffle_hover = shuffle_btn_rect.collidepoint(mouse_pos)
        next_hover = next_btn_rect.collidepoint(mouse_pos) and simulator.shuffle_mode
        prev_hover = prev_btn_rect.collidepoint(mouse_pos) and simulator.shuffle_mode
        reset_hover = reset_btn_rect.collidepoint(mouse_pos)
        
        shuffle_btn_rect = draw_button(screen, 50, 500, 150, 50, "Shuffle", shuffle_hover)
        next_btn_rect = draw_button(screen, 250, 500, 150, 50, "Next", next_hover)
        prev_btn_rect = draw_button(screen, 450, 500, 150, 50, "Previous", prev_hover)
        reset_btn_rect = draw_button(screen, 650, 500, 100, 50, "Reset", reset_hover)
        
        # Draw explanation
        explanation = [
            "How VLC Shuffle Works:",
            "1. Creates a fixed random order of songs when shuffle is enabled",
            "2. 'Next' plays the next song in the shuffled list",
            "3. 'Previous' goes to the prior song in the shuffled list, not playback history",
            "4. This is why 'Previous' often plays a different song than expected"
        ]
        
        for i, line in enumerate(explanation):
            text = font.render(line, True, TEXT)
            screen.blit(text, (50, 570 + i*25))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()