#include <stdio.h>

int globalm=10;

// Pass By Value
void Export(int k)
{
    for(int i=1;i<9;i+=2)
    {
        k+=i;
        globalm*=i;
    }
}


int main()
{
    int a=0;
    int b=a;
    b++;
    printf("A:%d\tB:%d\tGlobal:%d\n",a,b,globalm);
    Export(a);
    printf("A:%d\tB:%d\tGlobal:%d\n",a,b,globalm);
    return 0;
}