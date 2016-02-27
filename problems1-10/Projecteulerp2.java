
package projecteulerp1;

/**
 *
 * @author jake
 */
public class Projecteulerp2 {

    public static void main(String[] args) {
        		int trail = 0;
                        int head = 1;
                        int tmp = 0;
                        int total = 0;
		while (head < 4000000){
                    tmp = head;
                    head = head + trail;
                    trail = tmp;
                    if (head % 2 == 0) {
                       total += head;
                    }
                }
		System.out.println(total);
    }
    
}
