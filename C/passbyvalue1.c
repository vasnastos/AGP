#include <stdio.h>
#include <math.h>

void changeVal(int *k)
{
    (*k)++;
    printf("New K Value:%d\n",*k);
}

void readM(double m)
{
    m=sqrt(m);
    printf("New M Value:%lf\n",m);
}

int main()
{
   int a=19,b=21;
   changeVal(a);
   changeVal(b);
   readM(a);
   readM(b);
   printf("A:%d\tB:%d",a,b);

   return 0;
}