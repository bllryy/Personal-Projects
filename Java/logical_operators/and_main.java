public class and_main {

	public static void main(String[] args) {
		
		//logic ops
		//&& and
		//|| or
		//! not
		
		int temp = 25;

		if(temp>30) {
			System.out.println("Its hot outside");
		}
		else if(temp>=20 && temp<=30) {
			System.out.println("It is warm outside");
		} 
		else {
			System.out.println("It is cold outside");
		}
	}
}
