
abstract class Animal {

    private String name;

    // Constructor
    public Animal(String name) {
        this.name = name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public abstract void makeSound();

    public void eat() {
        System.out.println(this.name + " is eating");
    }
}

// inheritance
class Dog extends Animal {

    public Dog(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + " says: Woof woof!");
    }
}

class Cat extends Animal {

    public Cat(String name) {
        super(name);
    }

    @Override
    public void makeSound() {
        System.out.println(getName() + " says: Meow meow!");
    }
}

public class Main {

    public static void main(String[] args) {

        Dog myDog = new Dog("Bobby");
        Cat myCat = new Cat("Kitty");

        // Polymorphism
        myDog.makeSound();
        myCat.makeSound();

        myDog.eat();

        myDog.setName("Rocky");
        System.out.println("My dog's new name is " + myDog.getName());
    }
}
