package org.example;

import java.util.Scanner;

/**
 * Der Player kann selbst über seinen Zug entscheiden.
 * Hierbei wird darauf geachtet, dass der Spieler auch
 * eine gültige Eingabe macht.
 */
public class Player extends Computer{
    public Player(String sym){
        super(sym);
    }

    /**
     * Der Spieler überlegt seinen Zug
     * @return : Die Wahl des Spielers ohne Zeichenfehler
     */
    @Override
    public int getPlayersChoice(Board board){
        Scanner input = new Scanner(System.in);
        System.out.println("Wähle ein freies Feld aus: ");
        String playersChoice = input.nextLine();

        // Wiederhole die Eingabe, bis der Spieler ein gültiges Feld auswählt
        while(!isPlayersChoiceValid(playersChoice)){
            System.out.println("Wähle ein freies Feld aus: ");
            playersChoice = input.nextLine();
        }
        //input.close();
        return Integer.parseInt(playersChoice);
    }

    /**
     * Ist die Eingabe eine Zahl 1-9?
     * @param playersChoice: String der Eingabe des Spielers
     * @return : bool
     */
    private boolean isPlayersChoiceValid(String playersChoice) {
        if (playersChoice.matches("\\d+")) {
            int choice = Integer.parseInt(playersChoice);
            return (1 <= choice) && (choice <= 9);
        }
        return false;
    }
}
