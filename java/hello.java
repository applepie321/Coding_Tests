import java.util.Arrays;
import java.util.Scanner;

public class Hello
{
    public static void main (String[]args)
    {
        Scanner s = new Scanner (System.in);
        System.out.printf("Input number : ");
        String input = s.nextLine();
        if (input.length () == 5
                && input.chars ().distinct ().count () == input.length ())
        {
            char[] chars = input.toCharArray ();
            Arrays.sort (chars);
            String sorted = new String (chars);
            System.out.println (sorted);
        }
    }
}
