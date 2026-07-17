import java.util.Random;

public class TestCompartment {
    public static void main(String[] args) {
        Compartment[] train = new Compartment[10];
        Random rand = new Random();

        for (int i = 0; i < train.length; i++) {
            int type = rand.nextInt(4) + 1;

            switch (type) {
                case 1:
                    train[i] = new FirstClass();
                    break;
                case 2:
                    train[i] = new Ladies();
                    break;
                case 3:
                    train[i] = new General();
                    break;
                case 4:
                    train[i] = new Luggage();
                    break;
            }
        }

        System.out.println("=== Train Compartment Notices ===\n");

        for (int i = 0; i < train.length; i++) {
            System.out.println("Compartment " + (i + 1) + " [" +
                    train[i].getClass().getSimpleName() + "]:");
            System.out.println("  " + train[i].notice());
        }
    }
}