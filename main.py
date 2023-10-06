import pygame

# Clase para representar un tablero de Sudoku
class Board:

    def __init__(self, grid, screen):
        self.grid = grid
        self.screen = screen
        self.selected = None
        self.possible_values = [[0 for _ in range(9)] for _ in range(9)]

    def is_valid(self, row, col, num):
        # Verifica si un número es válido en una posición específica
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False

        # Verifica en el cuadro 3x3
        row_start, col_start = 3 * (row // 3), 3 * (col // 3)
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def set_selected(self, row, col):
        self.selected = (row, col)

    def input_number(self, num):
        if self.selected:
            row, col = self.selected
            if self.grid[row][col] == 0:
                if self.is_valid(row, col, num):
                    self.grid[row][col] = num
                else:
                    # Número no válido, muestra un mensaje o realiza otra acción aquí
                    pass

    def clear_cell(self):
        if self.selected:
            row, col = self.selected
            self.grid[row][col] = 0

    def draw(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None,30)

        # Dibuja el tablero
        for row in range(9):
            for col in range(9):
                pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(col * 50, row * 50, 50, 50), 1)
                if self.grid[row][col] != 0:
                    text_surface = font.render(str(self.grid[row][col]), True, (255, 255, 255))
                    self.screen.blit(text_surface, (col * 50 + 20, row * 50 + 15))

                
                # Dibuja una línea vertical más gruesa en la columna 3
                if col == 3:
                    pygame.draw.line(self.screen, (255, 255, 255), (col * 50, 0), (col * 50, 450), 5)

                # Dibuja una línea vertical más gruesa en la columna 6
                if col == 6:
                    pygame.draw.line(self.screen, (255, 255, 255), (col * 50, 0), (col * 50, 450), 5)

                # Dibuja una línea horizontal más gruesa en la fila 3
                if row == 3:
                    pygame.draw.line(self.screen, (255, 255, 255), (0, row * 50), (500, row * 50), 5)

                # Dibuja una línea horizontal más gruesa en la fila 6
                if row == 6:
                    pygame.draw.line(self.screen, (255, 255, 255), (0, row * 50), (500, row * 50), 5)



        # Dibuja el recuadro de selección
        if self.selected:
            row, col = self.selected
            pygame.draw.rect(self.screen, (64, 224, 208), pygame.Rect(col * 50, row * 50, 50, 50), 6)


# Clase para representar una interfaz GUI para el solucionador de Sudoku
class SudokuGUI:

    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.board = Board([[0 for _ in range(9)] for _ in range(9)], self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        clicked_row = mouse_pos[1] // 50
                        clicked_col = mouse_pos[0] // 50
                        self.board.set_selected(clicked_row, clicked_col)
                elif event.type == pygame.KEYDOWN:
                    if event.unicode.isdigit():
                        num = int(event.unicode)
                        self.board.input_number(num)
                    elif event.key == pygame.K_BACKSPACE:
                        self.board.clear_cell()

            self.draw(self.screen)
            pygame.display.flip()

    def draw(self, screen):
        self.board.draw()


def main():
    screen = pygame.display.set_mode((450, 450))
    pygame.display.set_caption("Resolutor de Sudoku")
    gui = SudokuGUI(screen)
    gui.run()

if __name__ == "__main__":
    main()

