import java.util.Scanner;
import java.util.ArrayList;


public class Driver {

  public static void main(String[] args) {
    System.out.println("How much can you spend? ")
    Scanner scan = new Scanner(System.in);
    double total = scan.nextDouble();
    double sum = 0; // total proportions entered by the user
    int i = 0; // index

    ArrayList<Double> proportion = new ArrayList<Double>(); // storage 
    System.out.println("Enter your proportion of various expenses.");
    System.out.println("The system stops if cummulative proportion exceedes 100%");
    
    do {
        System.out.println("Your proportion of expense " + (i + 1) + ":");
      double value = scan.nextDouble(); // var to store the user input
      proportion.add(value); // add to the array ArrayList
      sum += proportion.get(i); // get from the array list
    } while (sum <= 100);
    scan.close();
    if (sum > 100) {
      double cummulative = 0.0;
      for (int j = 0;) // -1 so we dont fall off or go to the end of a arr

    }


  }
}
