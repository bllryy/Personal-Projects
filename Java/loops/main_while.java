import java.util.Scanner;

public class main_while {
    
    public static void main(String[] args) {
        // keps going as long as true

        Scanner scanner = new Scanner(System.in);
        String name = "";

        do{
            System.out.print("Enter your name: ");
            name = scanner.nextLine();
        }while(name.isBlank());
        System.out.println("Hello "+name);
    }
}
