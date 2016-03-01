package projecteulerp1;

class projecteulerp3
{
	public static void main (String[] args) throws java.lang.Exception
	{
		long i = 2L;
		long n = 600851475143L; //it's three get over it
		while(i * i < n) {
			while(n % i == 0) {
				n = n / i;
			}
			i += 1;
		}
		System.out.println(n);
	}
}
