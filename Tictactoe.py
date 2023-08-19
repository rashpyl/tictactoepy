import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set window size
size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("TicTacToe")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
violet = (255, 0, 255)
blue = (0, 0, 255)
light_blue = (0, 255, 255)

screen.fill(light_blue)

# Initialize board and fonts
board = [["" for _ in range(3)] for _ in range(3)]
game_font = pygame.font.Font(None, 30)
winner_font = pygame.font.Font(None, 40)

# Draw the game board
def draw_board():
    for i in range(1, 3):
        pygame.draw.line(screen, black, (i * 100, 0), (i * 100, 300), 2)
        pygame.draw.line(screen, black, (0, i * 100), (300, i * 100), 2)

# Draw X
def draw_x(row, col):
    pygame.draw.line(screen, violet, (col * 100, row * 100), (col * 100 + 100, row * 100 + 100), 2)
    pygame.draw.line(screen, violet, (col * 100 + 100, row * 100), (col * 100, row * 100 + 100), 2)

# Draw O
def draw_o(row, col):
    pygame.draw.circle(screen, blue, (col * 100 + 50, row * 100 + 50), 40, 2)

# Check for a winner
def check_for_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != "":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]
    return None

def draw_tie_window():
    tie_text = winner_font.render("Tie game!", True, black)
    pygame.draw.rect(screen, black, (75, 100, 150, 100))
    pygame.draw.rect(screen, white, (80, 105, 140, 90))
    screen.blit(tie_text, (150 - tie_text.get_width() // 2, 150 - tie_text.get_height() // 2))
    pygame.display.update()
    time.sleep(3)


def tie_game():
    if check_for_winner() == None:
        draw_tie_window()

# Draw winner window
def draw_winner_window(winner):
    winner_text = winner_font.render(winner + " wins!", True, black)
    pygame.draw.rect(screen, black, (75, 100, 150, 100))
    pygame.draw.rect(screen, white, (80, 105, 140, 90))
    screen.blit(winner_text, (150 - winner_text.get_width() // 2, 150 - winner_text.get_height() // 2))
    pygame.display.update()
    time.sleep(2)

    # Evaluate the current state of the board
def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == "O":
                return 10
            elif board[row][0] == "X":
                return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == "O":
                return 10
            elif board[0][col] == "X":
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "O":
            return 10
        elif board[0][0] == "X":
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "O":
            return 10
        elif board[0][2] == "X":
            return -10
    return 0

# Minimax function
def minimax(board, depth, is_maximizing):
    result = evaluate(board)

    # Base cases: If the game is over, return the evaluation of the current state
    if result == 10:
        return result - depth  # AI wins, subtracting depth to favor faster wins
    if result == -10:
        return result + depth  # Human wins, adding depth to favor slower losses
    if result == 0 and depth == 9:
        return 0  # Tie game

    if is_maximizing:
        max_eval = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "O"  # Simulate the AI's move
                    eval = minimax(board, depth + 1, False)  # Recurse with human's turn
                    board[row][col] = ""  # Undo the move
                    max_eval = max(max_eval, eval)  # Update the maximum evaluation
        return max_eval
    else:
        min_eval = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "X"  # Simulate the human's move
                    eval = minimax(board, depth + 1, True)  # Recurse with AI's turn
                    board[row][col] = ""  # Undo the move
                    min_eval = min(min_eval, eval)  # Update the minimum evaluation
        return min_eval


# AI's move
def ai_move():
    best_move = None
    best_score = -float("inf")

    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = ""  # Undo the move

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    if best_move:
        row, col = best_move
        board[row][col] = "O"
        draw_o(row, col)

# Main game loop
def start_game():
    draw_board()
    human_turn = True  # Human starts the game
    running = True
    moves = 0  # Track the number of moves made

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and human_turn:
                if event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    row = y // 100
                    col = x // 100

                    if board[row][col] == "":
                        board[row][col] = "X"
                        draw_x(row, col)
                        moves += 1  # Increment the number of moves
                        winner = check_for_winner()

                        if winner:
                            draw_winner_window(winner)
                            running = False
                        elif moves == 9:  # All cells are filled and no winner
                            tie_game()  # Call the tie_game function
                            running = False

                        if running and moves < 9:
                            ai_move()  # AI's turn
                            moves += 1
                            winner = check_for_winner()

                            if winner:
                                draw_winner_window(winner)
                                running = False
                            elif moves == 9:  # All cells are filled and no winner
                                tie_game()  # Call the tie_game function
                                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()

start_game()