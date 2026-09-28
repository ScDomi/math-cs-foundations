import java.util.Random;

/**
 * Computer auf Niveau eines Kleinkinds:
 * Er setzt seinen Stein auf ein zufälliges Feld
 */
class Computer{
    private final String symbol;

    public Computer(String sym){
        symbol = sym;
    }

    public String getSymbol(){
        return symbol;
    }

    /**
     * Computer überlegt seinen Zug
     * @return : Zufallszahl 1-9
     */
    public int getPlayersChoice(Board board){
        Random random = new Random();
        return random.nextInt(9) +1;
    }
}
