public class Box3D extends Box {

    private double height;

    public Box3D(double length, double breadth, double height) {

        super(length, breadth);
        this.height = height;
    }

    public double volume() {
        return length * breadth * height;
    }

    public static void main(String[] args) {

        Box box = new Box(5, 3);
        System.out.println("Box area = " + box.area());

        Box3D box3d = new Box3D(5, 3, 4);

        System.out.println("Box3D area = " + box3d.area());
        System.out.println("Box3D volume = " + box3d.volume());
    }
}