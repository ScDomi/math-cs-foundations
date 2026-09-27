package org.example;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class BoardTest {
    @Test
    void setBoardTest(){
        Board board = new Board();
        board.setBoard(1, "X");
        board.setBoard(5, "X");

        assertFalse(board.isTaken(2));
        assertFalse(board.isTaken(4));
        assertFalse(board.isTaken(6));

        assertTrue(board.isTaken(1));
        assertTrue(board.isTaken(5));
    }

    @Test
    void isTakenTest(){
        Board board = new Board();

        board.setBoard(1, "X");
        board.setBoard(2, "#");
        board.setBoard(7, "X");
        board.setBoard(9, "#");

        assertTrue(board.isTaken(1));
        assertTrue(board.isTaken(2));
        assertTrue(board.isTaken(7));
        assertTrue(board.isTaken(9));

        assertFalse(board.isTaken(3));
        assertFalse(board.isTaken(4));
        assertFalse(board.isTaken(5));
        assertFalse(board.isTaken(6));
        assertFalse(board.isTaken(8));
    }

    @Test
    void isTieTest(){
        Board board = new Board();

        for(int i = 1; i <= 9; i++){
            board.setBoard(i, "X");
        }
        assertTrue(board.isTie());

        for(int i = 1; i <= 9; i++){
            board.setBoard(i, "#");
        }
        assertTrue(board.isTie());
    }

    @Test
    void winConditionTest(){
        Board board = new Board();

        board.setBoard(1, "X");
        board.setBoard(2, "X");
        board.setBoard(3, "X");
        assertTrue(board.winCondition());
    }

    @Test
    void winConditionTest2(){
        Board board = new Board();

        board.setBoard(1, "X");
        board.setBoard(4, "X");
        board.setBoard(7, "X");
        assertTrue(board.winCondition());
    }

    @Test
    void winConditionTest3(){
        Board board = new Board();

        board.setBoard(1, "X");
        board.setBoard(5, "X");
        board.setBoard(9, "X");
        assertTrue(board.winCondition());
    }
}