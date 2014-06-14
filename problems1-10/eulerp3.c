#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 2;
    long long n = 600851475143;
    while(i * i < n){
        while(n % i == 0){
            n = n/i;
        }
        i += 1;
    }
    printf("%d\n", n);
    return 0;
}
