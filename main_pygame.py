import pygame
import sys
import time
from game import TicTacToe, HUMAN, AI, EMPTY
import minimax
import alphabeta

# Settings
WIDTH, HEIGHT = 600, 700
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = 200
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (84, 84, 84)
BUTTON_HOVER = (120, 120, 120)
WINNER_BG = (50, 50, 50)

# Game states
STATE_START = 0
STATE_PLAYING = 1
STATE_GAME_OVER = 2

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe AI')
font_large = pygame.font.Font(None, 60)
font_medium = pygame.font.Font(None, 40)
font_small = pygame.font.Font(None, 30)
font_tiny = pygame.font.Font(None, 24)

game = None
game_state = STATE_START
selected_algorithm = None  # 'minimax' or 'alphabeta'
winner = None
last_move_stats = None  # {'nodes': 0, 'time': 0.0}

class Button:
    def __init__(self, x, y, width, height, text, action):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.hovered = False
    
    def draw(self, screen):
        color = BUTTON_HOVER if self.hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, TEXT_COLOR, self.rect, 3, border_radius=10)
        
        text_surface = font_medium.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()
                return True
        return False

def start_minimax():
    global game_state, selected_algorithm, game, last_move_stats
    selected_algorithm = 'minimax'
    game_state = STATE_PLAYING
    game = TicTacToe()
    last_move_stats = None

def start_alphabeta():
    global game_state, selected_algorithm, game, last_move_stats
    selected_algorithm = 'alphabeta'
    game_state = STATE_PLAYING
    game = TicTacToe()
    last_move_stats = None

def play_again():
    global game_state, last_move_stats
    game_state = STATE_START
    last_move_stats = None

# Buttons
minimax_button = Button(100, 250, 400, 80, "Minimax Algorithm", start_minimax)
alphabeta_button = Button(100, 370, 400, 80, "Alpha-Beta Pruning", start_alphabeta)
play_again_button = Button(150, 500, 300, 70, "Play Again", play_again)

def draw_start_screen():
    screen.fill(BG_COLOR)
    
    # Title
    title = font_large.render("Tic Tac Toe AI", True, TEXT_COLOR)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 80))
    
    # Subtitle
    subtitle = font_small.render("Select Algorithm", True, TEXT_COLOR)
    screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 170))
    
    # Buttons
    minimax_button.draw(screen)
    alphabeta_button.draw(screen)
    
    # Info
    info = font_small.render("Click to choose your AI opponent", True, TEXT_COLOR)
    screen.blit(info, (WIDTH // 2 - info.get_width() // 2, 520))

def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, 600), LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if game.board[row][col] == AI:
                # Circle for AI
                pygame.draw.circle(
                    screen,
                    CIRCLE_COLOR,
                    (int(col * SQUARE_SIZE + SQUARE_SIZE // 2),
                     int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                    CIRCLE_RADIUS,
                    CIRCLE_WIDTH
                )
            elif game.board[row][col] == HUMAN:
                # Cross for Human
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE),
                    CROSS_WIDTH
                )
                pygame.draw.line(
                    screen,
                    CROSS_COLOR,
                    (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                    (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                    CROSS_WIDTH
                )

def draw_game_screen():
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    
    # Display algorithm name
    algo_name = "Minimax" if selected_algorithm == 'minimax' else "Alpha-Beta Pruning"
    algo_text = font_small.render(f"Algorithm: {algo_name}", True, TEXT_COLOR)
    
    # Draw bottom bar
    pygame.draw.rect(screen, LINE_COLOR, (0, 600, WIDTH, 100))
    screen.blit(algo_text, (WIDTH // 2 - algo_text.get_width() // 2, 610))
    
    # Display stats if available
    if last_move_stats:
        stats_text = font_tiny.render(
            f"AI Move: {last_move_stats['nodes']} nodes visited in {last_move_stats['time']:.4f}s",
            True,
            TEXT_COLOR
        )
        screen.blit(stats_text, (WIDTH // 2 - stats_text.get_width() // 2, 645))
        
        status_text = font_small.render("Your turn - Click to play", True, TEXT_COLOR)
        screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, 670))
    else:
        status_text = font_small.render("Your turn - Click to play", True, TEXT_COLOR)
        screen.blit(status_text, (WIDTH // 2 - status_text.get_width() // 2, 655))

def draw_game_over_screen():
    # Draw semi-transparent overlay
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(WINNER_BG)
    screen.blit(overlay, (0, 0))
    
    # Winner text
    if winner == HUMAN:
        winner_text = "You Win!"
        color = (100, 255, 100)
    elif winner == AI:
        winner_text = "AI Wins!"
        color = (255, 100, 100)
    else:
        winner_text = "Draw!"
        color = (255, 255, 100)
    
    text = font_large.render(winner_text, True, color)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 200))
    
    # Show final stats if available
    if last_move_stats:
        final_stats = font_small.render(
            f"Last AI move: {last_move_stats['nodes']} nodes, {last_move_stats['time']:.4f}s",
            True,
            TEXT_COLOR
        )
        screen.blit(final_stats, (WIDTH // 2 - final_stats.get_width() // 2, 350))
    
    # Draw play again button
    play_again_button.draw(screen)

def check_win():
    global winner, game_state
    
    if game.is_winner(HUMAN):
        winner = HUMAN
        game_state = STATE_GAME_OVER
        return True
    elif game.is_winner(AI):
        winner = AI
        game_state = STATE_GAME_OVER
        return True
    elif game.is_draw():
        winner = None
        game_state = STATE_GAME_OVER
        return True
    
    return False

def ai_move():
    global last_move_stats
    
    start = time.time()
    
    if selected_algorithm == 'alphabeta':
        alphabeta.nodes_visited = 0
        _, move = alphabeta.alphabeta(game, 0, -1, 1, True)
        nodes = alphabeta.nodes_visited
        algo = "Alpha-Beta"
    else:
        minimax.nodes_visited = 0
        _, move = minimax.minimax(game, 0, True)
        nodes = minimax.nodes_visited
        algo = "Minimax"
    
    elapsed = time.time() - start
    
    # Store stats for display
    last_move_stats = {
        'nodes': nodes,
        'time': elapsed
    }
    
    print(f"{algo} - Nodes visited: {nodes}, Time: {elapsed:.4f}s")
    
    if move:
        game.make_move(*move, AI)

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if game_state == STATE_START:
            minimax_button.handle_event(event)
            alphabeta_button.handle_event(event)
        
        elif game_state == STATE_PLAYING:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                
                if mouseY < 600:  # Click on board
                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)
                    
                    if game.board[clicked_row][clicked_col] is EMPTY:
                        game.make_move(clicked_row, clicked_col, HUMAN)
                        
                        draw_game_screen()
                        pygame.display.update()
                        
                        if not check_win():
                            pygame.time.wait(300)
                            ai_move()
                            check_win()
        
        elif game_state == STATE_GAME_OVER:
            play_again_button.handle_event(event)
    
    # Draw based on state
    if game_state == STATE_START:
        draw_start_screen()
    elif game_state == STATE_PLAYING:
        draw_game_screen()
    elif game_state == STATE_GAME_OVER:
        draw_game_screen()
        draw_game_over_screen()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()