package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class SmartComputerTest {
    // Der Computer soll den Gewinn des Gegners verhindern, wenn möglich
    @Test
    void denyEnemyWin(){
        Board board = new Board();
        SmartComputer comp= new SmartComputer("#");

        board.setBoard(1, "X");
        board.setBoard(6, "#");
        board.setBoard(3, "X");

        assertEquals(2, comp.getPlayersChoice(board));
    }

    @Test
    void denyEnemyWin2(){
        Board board = new Board();
        SmartComputer comp= new SmartComputer("#");

        board.setBoard(2, "X");
        board.setBoard(6, "#");
        board.setBoard(8, "X");

        assertEquals(5, comp.getPlayersChoice(board));
    }

    @Test
    void denyEnemyWin3(){
        Board board = new Board();
        SmartComputer comp= new SmartComputer("#");

        board.setBoard(1, "X");
        board.setBoard(4, "#");
        board.setBoard(9, "X");

        assertEquals(5, comp.getPlayersChoice(board));
    }
}