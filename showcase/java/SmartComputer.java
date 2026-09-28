public class SmartComputer extends Computer{
    private final String symbol;
    public SmartComputer(String sym) {
        super(sym);
        symbol = sym;
    }

    /**
     * Computer überlegt seinen Zug mithilfe des Minimax-Algorithmus
     * @param board Das aktuelle Spielfeld
     * @return : int, der intelligent gewählte Zug
     */
    public int getPlayersChoice(Board board) {
        int bestMove = -1;
        int bestScore = Integer.MIN_VALUE;

        // Gehe alle möglichen Züge durch
        for (int i = 1; i <= 9; i++) {
            if (!board.isTaken(i)) {
                board.setBoard(i, symbol);
                int score = minimax(board, 0, false);
                // Mache Zug rückgängig
                board.setBoard(i, String.valueOf(i));

                // Wähle den besten Zug durch Auswertung der Spielsituation
                if (score > bestScore) {
                    bestScore = score;
                    bestMove = i;
                }
            }
        }
        return bestMove;
    }

    /**
     * Minimax-Algorithmus zur Berechnung des Scores
     * @param board : Spielsituation
     * @param depth : Tiefe des Algorithmus
     * @param isMaximizing : Maximieren oder Minimieren?
     * @return Der Score für die Spielsituation
     */
    private int minimax(Board board, int depth, boolean isMaximizing) {
        if (board.winCondition()) {
            return isMaximizing ? -1 : 1;
        }

        if (board.isTie()) {
            return 0;
        }

        int bestScore = isMaximizing ? Integer.MIN_VALUE : Integer.MAX_VALUE;

        for (int i = 1; i <= 9; i++) {
            if (!board.isTaken(i)) {
                board.setBoard(i, isMaximizing ? symbol : "X");
                int score = minimax(board, depth + 1, !isMaximizing);
                board.setBoard(i, String.valueOf(i));

                // Aktualisiere besten Score, je nach Situation
                if (isMaximizing) {
                    bestScore = Math.max(bestScore, score);
                } else {
                    bestScore = Math.min(bestScore, score);
                }
            }
        }
        return bestScore;
    }
}
