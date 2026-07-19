public class Outer {

    public void display() {
        System.out.println("Display from Outer class");
    }

    class Inner {

        public void display() {
            System.out.println("Display from Inner class");
        }
    }

    public static void main(String[] args) {

        Outer outer = new Outer();
        outer.display();

        Outer.Inner inner = outer.new Inner();
        inner.display();
    }
}