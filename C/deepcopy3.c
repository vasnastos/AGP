#include <stdio.h>
#include <stdlib.h>

typedef char * string;

int changeString(string par)
{
    for(int i=0;i<strlen(par);i++)
    {
        int counter=0;
        if(par[i]=='a' || par[i]=='o' || par[i]=='e' || par[i]=='i' || par[i]=='u')
        {
            par[i]=='_';
            counter++;
        }
        return counter;
    }
}

int main(int argc,char **argv)
{
    const int size=500;
    string K=(string)malloc(size*sizeof(char));
    strcpy("Staghorn's leers and Dr. Peccary's glowers were not for the scenery,however, but for the people who wandered aimlessly through the littlepark and along the street beyond, carefully avoiding the area beneath the leaning steeple. All of them were uniformly young, ranging from perhaps seventeen at one extreme to no more than thirty at the other.When Dr. Peccary had first seen them, he'd cried out joyfully, You see, Staghorn, all young! All handsome! Then he'd stopped talking as he studied those in the foreground more closely.",K);
    printf("Changes Made:%d\n",changeString(K));
    printf("New String:%s",K);
    free(K);
}