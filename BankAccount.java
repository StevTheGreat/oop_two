import java.util.Scanner; 

public class BankAccount { 
    private double balance; 

    public BankAccount(double initialBalance){ 
        if (initialBalance < 0) { 
            throw new IllegalArgumentException("Initial balance cannot be negative"); 
        } 
        this.balance = initialBalance; 
    } 

    public double getBalance(){ 
        return balance; 
    } 

    public void setBalance(double amount){ 
        if (amount < 0 ) { 
            throw new IllegalArgumentException("Balance cannot be negative"); 
        } 
        this.balance = amount; 
    } 

    public static void main(String[] args) { 
        Scanner scanner = new Scanner(System.in); 

        System.out.print("Enter initial balance: "); 
        double initialBalance = scanner.nextDouble(); 
        

        BankAccount account = new BankAccount(initialBalance); 
        System.out.println("Account created. Balance: " + account.getBalance()); 

        System.out.print("Enter amount to update balance: "); 
        double updatedBalance = scanner.nextDouble(); 
        

        account.setBalance(updatedBalance);
        System.out.println("Account updated. Balance: " + account.getBalance()); 

        scanner.close(); 
    } 
}
