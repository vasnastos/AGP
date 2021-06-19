#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define size 500


struct employee
{
   char name[255];
   double salary;
   struct employee *emp;
};

typedef struct employee employee;

double average_Salary(employee *curr)
{
    double s=0.0;
    int i=1;
    while(curr!=NULL)
    {
      if(i%3==0) 
      strcpy(curr->name,"Modified");
      s+=curr->salary;
      curr=curr->emp;
      i++;
    }
    return s/i;
}

void push_back(employee *e,char *name,double s)
{
    while(e->emp!=NULL)
    {
      e=e->emp;
    }
    employee *newemployee=(employee *)malloc(sizeof(employee));
    strcpy(newemployee->name,name);
    newemployee->salary=s;
    newemployee->emp=NULL;
    e->emp=newemployee;
}

void FreeMem(employee *he)
{
    while(he!=NULL)
    {
        employee *de=he;
        he=he->emp;
        free(de);
    }
}

void PrintList(employee *e)
{
    while(e!=NULL)
    {
        printf("%s\t%lf\n",e->name,e->salary);
        e=e->emp;
    }
}

int main()
{
    employee *head=(employee *)malloc(sizeof(employee));
    strcpy(head->name,"IOANNIS CHRISTOU");
    head->salary=3500;
    head->emp=NULL;
    FILE *fp=fopen("../PYTHON/DATA/employees.csv","r");
    if(fp==NULL)
    {
        perror("File did not open!!!");
        exit(-1);
    }
    char line[size];
    char data[2][size];
    while(fgets(line,size,fp)!=NULL)
    {
        if(line[strlen(line)-1]=='\n')
        {
            line[strlen(line)-1]=' ';
        }
        char *token=strtok(line,",");
        int j=0;
        while(token!=NULL)
        {
           strcpy(data[j],token);
            j++;
            token=strtok(NULL,",");
        }
        push_back(head,data[0],atof(data[1]));
    }
    PrintList(head);
    printf("\n\n");
    printf("Average Salary:%.3lf\n\n",average_Salary(head));
    PrintList(head);
    FreeMem(head);
    return 0;
}