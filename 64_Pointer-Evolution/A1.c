#include<stdio.h>
#include<stdlib.h>
int main(){
  int a = 10;   // this is static memory Allocation
  int *p;
  p = &a;    // Pointer P points address of  variable a 
  printf("a: %d", a);
  printf("\nAddress of a: %p", p);

  int *q ;
  q = (int*) malloc(4);   // created a dynamic memory of 4 bytes and this memory space does not destroy with ends of function. WE should free it with free method.
  printf("\n%p", q);
  free(q);
}

