package org.example;

import java.util.Objects;

/**
 * Die Klasse Board repräsentiert das Tic-Tac-Toe-Feld.
 * Das Board kann angezeigt werden, durch Spieler verändert
 * werden, zeigt an, wie das Spiel ausgeht, und weiß auch,
 * welche Felder bereits besetzt sind.
 */
public class Board {
    private final String[][] board;

    public Board() {
        board = new String[3][3];
        initialiseBoard();
    }

    /**
     * Der Spieler setzt seinen Spielstein
     * @param playersChoice: int
     * @param symbol: String
     */
    public void setBoard(int playersChoice, String symbol){
        int j = (playersChoice-1) % 3;
        int i = (playersChoice-1) / 3;
        board[i][j] = symbol;
    }

    /**
     *  Gibt beim Aufruf das Spielbrett auf der Konsole aus
     */
    public void printBoard() {
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
        }
        System.out.println("└" + "- - - - - -" + "┘");
    }

    /**
     * Überprüfung, ob ein Spieler gewonnen hat
     * @return : Ist das Spiel vorbei?
     */
    public boolean winCondition(){
        // Überprüfe entlang der Zeilen
        for(int i = 0; i < 3; i++){
            if (Objects.equals(board[i][0], board[i][1]) && Objects.equals(board[i][1], board[i][2])) {
                return true;
            }
        }
        // Überprüfe entlang der Spalten
        for(int j = 0; j < 3; j++){
            if(Objects.equals(board[0][j], board[1][j]) && Objects.equals(board[1][j], board[2][j])){
                return true;
            }
        }
        // Überprüfe Diagonal (2 Fälle)
        if(Objects.equals(board[0][0], board[1][1]) && Objects.equals(board[1][1], board[2][2])){
            return true;
        } else {
            return Objects.equals(board[0][2], board[1][1]) && Objects.equals(board[1][1], board[2][0]);
        }
        // Spiel ist doch noch nicht vorbei
    }

    /**
     * Überprüfung, ob das Spiel unentschieden ausgegangen ist
     * @return : true heißt Unentschieden, false heißt kein Unentschieden
     */
    public boolean isTie() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // Alle Felder belegt
                if (board[i][j].matches("\\d+")) {
                    return false;
                }
            }
        }
        // Alle Felder sind belegt → Unentschieden
        return true;
    }

    /**
     * Ist das gewählte Feld bereits besetzt?
     * @param playersChoice : Spielfeldwahl des Spielers/Computers
     * @return : true = besetzt, false = nicht besetzt
     */
    public boolean isTaken(int playersChoice) {
        // Rücktransformation zu 2D Adressierung
        int j = (playersChoice-1) % 3;
        int i = (playersChoice-1) / 3;

        return !Objects.equals(board[i][j], String.valueOf(playersChoice));
    }
    private void initialiseBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                // Verwende Linearisierung des Arrays, um Kästchen durchzunummerieren
                board[i][j] = String.valueOf(3 * i + j + 1);
            }
        }
    }
}