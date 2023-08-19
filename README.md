# tictactoepy
Tic-Tac-Toe game

Tato dokumentace poskytuje přehled o implementaci hry Piškvorky v programovacím jazyce Python s využitím knihovny Pygame, která zahrnuje protihráče řízeného umělou inteligencí pomocí algoritmu Minimax.

Knihovny

•	pygame: Knihovna pro vytváření her a multimediálních aplikací v Pythonu.
•	sys: Knihovna poskytující funkce a proměnné specifické pro systém.
•	time: Knihovna pro manipulaci s časem.

Inicializace

Hra začíná inicializací knihovny Pygame, nastavením velikosti okna, názvu okna a vyplněním pozadí.

Barvy

•	white: Bílá barva.
•	black: Černá barva.
•	violet: Fialová barva.
•	blue: Modrá barva.
•	light_blue: Světle modrá barva.

Hlavní herní smyčka

Hlavní herní smyčka obsahuje:
•	Inicializaci herního stavu.
•	Postupně se opakující akce (události) v rámci smyčky, které reagují na interakci s hráčem nebo provádějí tahy AI.
•	Závěrečnou část, kde se hra ukončuje a ukončuje i knihovna Pygame.

Funkce pro vykreslení

•	draw_board(): Vykreslí hrací plochu s mřížkou.
•	draw_x(row, col): Vykreslí "X" na zadané pozici.
•	draw_o(row, col): Vykreslí "O" (kruh) na zadané pozici.
•	draw_winner_window(winner): Vykreslí okno s informací o vítězi.
•	draw_tie_window(): Vykreslí okno s informací o remíze.

Funkce pro kontrolu výhry/remízy

•	check_for_winner(): Zkontroluje, zda hra má vítěze a vrátí vítězné okno.
•	tie_game(): Zavolá funkci pro vykreslení okna informujícího o remíze.


Hodnocení stavu hracího pole

•	evaluate(board): Hodnotí aktuální stav hracího pole a vrací skóre podle aktuální situace.

Minimax algoritmus

•	minimax(board, depth, is_maximizing): Implementace algoritmu Minimax pro nalezení nejlepšího tahu pro AI nebo hráče.
•	ai_move(): Volá algoritmus Minimax pro rozhodnutí o tahu AI.

Hlavní herní smyčka

•	start_game(): Spouští hlavní herní smyčku, která zahrnuje interakci s hráčem, tahy AI a vyhodnocování výsledku.

Závěr

Toto je stručná dokumentace k Tictactoe hře, která popisuje implementaci různých funkcí, které tvoří hru. Přiložený kód demonstruje způsob, jakým jsou tyto funkce použity k vytvoření kompletní hry Tic-Tac-Toe s jednoduchým AI proti hráči.
