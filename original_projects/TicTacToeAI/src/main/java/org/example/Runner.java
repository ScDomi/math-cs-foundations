/**
 * Aufgabe 2:
 * Ein Tic-Tac-Toe-Spiel mit intelligentem Computer
 * @author Dominik Schwagerl
 * @since 2024-01-17
 */
package org.example;

/**
 * Führt ein Tic-Tac-Toe-Spiel zwischen Spieler und
 * Computer aus. Das Spiel ist zu Ende, wenn ein Spieler
 * gewonnen hat oder es Unentschieden ausgeht. Der
 * Gewinner wird am Ende des Spiels verkündet.
 */
public class Runner {
    public static void main(String[] args) {

        Board board = new Board();
        SmartComputer Comp = new SmartComputer("#");
        Player PlayerX = new Player("X");

        Computer currPlayer = PlayerX;
        board.printBoard();

        // Game Loop
        while (!board.winCondition() && !board.isTie()) {

            int playersChoice = currPlayer.getPlayersChoice(board);

            while(board.isTaken(playersChoice)){
                playersChoice = currPlayer.getPlayersChoice(board);
            }

            board.setBoard(playersChoice, currPlayer.getSymbol());
            board.printBoard();

            currPlayer = (currPlayer == PlayerX) ? Comp : PlayerX;
        }
        Computer Winner;
        if(currPlayer == PlayerX){
            Winner = Comp;
        }else{
            Winner = PlayerX;
        }
        if (board.winCondition()) {
            System.out.println("Spieler " + Winner.getSymbol() + " hat gewonnen!");
        } else if (board.isTie()) {
            System.out.println("Das Spiel endet unentschieden.");
        }
    }
}
