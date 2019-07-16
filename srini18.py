#include <stdio.h> 
 
int main() 
{ 
 
    int z, b, i, k, flag; 
    scanf("%d", &z); 
    scanf("%d", &b); 
    for (i = z; i <= b; i++) 
    { 
 
        if (i == 1 || i == 0) 
            continue; 
 
        flag = 1; 
 
        for (k = 2; k <= i / 2; ++k)
        { 
            if (i % k == 0)
            { 
                flag = 0; 
                break; 
            } 
        } 
        if (flag == 1) 
            printf("%d ", i); 
    } 
 
    return 0; 
} 
