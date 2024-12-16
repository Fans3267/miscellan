
class Vehicle {
    private String brand;
    private int maxSpeed;

    public Vehicle(String brand, int maxSpeed) {
        this.brand = brand;
        this.maxSpeed = maxSpeed;
    }
    public String getBrand() {
        return brand;
    }
    public int getMaxSpeed() {
        return maxSpeed;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }
    public void setMaxSpeed(int maxSpeed) {
        this.maxSpeed = maxSpeed;
    }

    public void start() { System.out.println("The vehicle is starting."); }
    public void stop() {
        System.out.println("The vehicle is stopping.");
    }
    public void drive() {
        System.out.println("The vehicle is in motion.");
    }
}

class ElectricCar extends Vehicle {
    private int batteryCapacity;
    public ElectricCar(String brand, int maxSpeed, int batteryCapacity) {
        super(brand, maxSpeed);
        this.batteryCapacity = batteryCapacity;
    }

    public int getBatteryCapacity() {
        return batteryCapacity;
    }
    public void setBatteryCapacity(int batteryCapacity) {
        this.batteryCapacity = batteryCapacity;
    }

    public void showInfo() {
        System.out.print("Brand: " + getBrand()+", ");
        System.out.print("Max Speed: " + getMaxSpeed()+", ");
        System.out.print("Fuel Type: " + batteryCapacity +"\n");
    }
}

class HybridCar extends Vehicle {
    private String fuelType;
    public HybridCar(String brand, int maxSpeed, String fuelType) {
        super(brand, maxSpeed);
        this.fuelType = fuelType;
    }
    public String getFuelType() {
        return fuelType;
    }
    public void setFuelType(String fuelType) {
        this.fuelType = fuelType;
    }
    public void showInfo() {
        System.out.print("Brand: " + getBrand()+", ");
        System.out.print("Max Speed: " + getMaxSpeed() + ", ");
        System.out.print("Fuel Type: " + fuelType +"\n");
    }
}


public class Main {
    public static void main(String[] args) {
        Vehicle myCar = new Vehicle("Toyota", 120);
        myCar.start();
        myCar.drive();

        ElectricCar myElectricCar = new ElectricCar("Tesla", 150, 50000);
        myElectricCar.start();
        myElectricCar.drive();
        myElectricCar.showInfo();

        HybridCar myHybridCar = new HybridCar("Toyota Prius", 100, "Petrol");
        myHybridCar.start();
        myHybridCar.drive();
        myHybridCar.showInfo();
    }
}
