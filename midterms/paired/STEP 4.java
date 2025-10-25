public class Tiny_Hospital {    
    public static void display_patient1(){
    int id = 1;
    String name = "Lea";
    String date = "July 1, 2006";
    System.out.println("Patient ID: "+ id);
    System.out.println("Patient Name: " + name);
    System.out.println("Patient Date of birth: " + date);
    }
    public static void display_room1(){
    int room_num = 1;
    String room_type = "private";
    String room_status = "occupied";
    Double room_fee = 2500.00;
    System.out.println("Room Number: "+ room_num);
    System.out.println("Room Type: " + room_type);
    System.out.println("Room Status: " + room_status);
    System.out.println("Room Fee: " + room_fee);
        System.out.println();
    }
    public static void display_patient2(){
    int id = 2;
    String name = "Angela";
    String date = "July 5, 2006";
    System.out.println("Patient ID: "+ id);
    System.out.println("Patient Name: " + name);
    System.out.println("Patient Date of birth: " + date);
    }
    public static void display_room2(){
    int room_num = 2;
    String room_type = "semi-private";
    String room_status = "occupied";
    Double room_fee = 1500.00;
    System.out.println("Room Number: "+ room_num);
    System.out.println("Room Type: " + room_type);
    System.out.println("Room Status: " + room_status);
    System.out.println("Room Fee: " + room_fee);
    }
	public static void main(String[] args) {
	 display_patient1();
	 display_room1();
	 display_patient2();
	 display_room2();
	}
}
