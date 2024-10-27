#include <stdio.h>
#include <stdlib.h>

#define FLAG_SIZE 100
#define BUFFER_SIZE 120

void Rome(){
    FILE * f = fopen("flag.txt", "r"); 
    if (f == NULL) {
        printf("You're so close , try creating a flag.txt file in your local directory for this to work \n");
        exit(1);
    }

    printf("\nCiao amico, ti ho preso della pizza \n");
    char flag[FLAG_SIZE];
    fread(flag, 1, FLAG_SIZE, f); 
    fclose(f);
    printf("%s\n", flag);
    exit(0);     
}

void vuln(){
   char buf[BUFFER_SIZE];
   printf("They say all roads lead to Rome...\n");
   printf("So , pave your way to it : \n");
   fgets(buf, BUFFER_SIZE*2, stdin); // oops , silly me 
   return;
}

int main(void){

    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    vuln();

    printf("Boooo , you're still here >u<\n");
    return 0;
}
