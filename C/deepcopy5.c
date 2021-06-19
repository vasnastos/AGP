#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define RM 200


int MaxSumLine(int **board,int n,int m)
{
    srand(time(NULL));
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            board[i][j]=rand()%RM;
        }
    }
    int max=-1,summax=0;
    for(int i=0;i<n;i++)
    {
      int s=0;
      for(int j=0;j<m;j++)
      {
          s+=board[i][j];
      }
      if(s>summax)
      {
          summax=s;
          max=i;
      }
    }
    return max;
}

int main()
{
    const int size=10;
    int **b;
    b=(int **)malloc(size*sizeof(int *));
    for(int i=0;i<size;i++)
    {
        b[i]=(int *)malloc(size*sizeof(int));
    }
    printf("Line with max Random Sum:%d",MaxSumLine(b,size,size));
    for(int i=0;i<size;i++)
    {
        free(b[i]);
    }
    free(b);
}