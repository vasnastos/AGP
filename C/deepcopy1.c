#include <stdio.h>
#include <stdlib.h>

void readdata(int table[],int size)
{
    for(int i=0;i<size;i++)
    {
        printf("Give table[%d]:",i);
        scanf("%d",&table[i]);
    }
}

int main(int argc,char **argv)
{
    if(argc<2)
    {
      perror("Error on command line arguments\n");
      return -2;
    }
    printf("File Executed:%s\n",argv[0]);
    int size=atoi(argv[1]);
    int *data=(int *)malloc(size*sizeof(int));
    readdata(data,size);
    printf("\n\nRESULTS\n*******************************\n");
    for(int i=0;i<size;i++)
    {
        printf("table[%d]:%d\n",i,data[i]);
    }
    free(data);
    return 0;
}