#include <stdio.h>
#include <stdlib.h>

double summary(int *a,int *b,int *c)
{
    (*a)++;
    (*b)++;
    (*c)++;
    return (*a+*b+*c)/3.0;
}

int main(int argc,char **argv)
{
    int a=4,b=5,c=6;
    printf("A:%d\tB:%d\tC:%d\n",a,b,c);
    printf("Avg:%.3lf\n",summary(&a,&b,&c));
    printf("A:%d\tB:%d\tC:%d\n",a,b,c);
    return 0;
}