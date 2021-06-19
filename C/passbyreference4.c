#include <stdio.h>
#include <stdlib.h>

double summary(int *a,int *b,int *c)
{
    (*b)++;
    (*c)++;
    int d=*a;
    printf("AC:%d\n",++d);
    return (*a+*b+*c);
}

int main(int argc,char **argv)
{
    int x=5;
    int c=x++;
    printf("%d",c);

    // int a=4,b=5,c=6;
    // printf("A:%d\tB:%d\tC:%d\n",a,b,c);
    // printf("Avg:%.3lf\n",summary(&a,&b,&c));
    // printf("A:%d\tB:%d\tC:%d\n",a,b,c);
    // return 0;
}