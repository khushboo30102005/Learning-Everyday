#include<stdio.h>
int main(int argc, char* argv[]){
  int i;
  printf("Argument Count: %d", argc);
  for (int i = 0; i < argc; i++)
  {
    printf("\n %d). %s", argc, argv[i]);
  }
  
  printf("\n");
  return 0;
}