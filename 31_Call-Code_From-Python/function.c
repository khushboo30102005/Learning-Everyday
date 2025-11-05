int lcm(int a, int b){
  int L;
  for(L=a>b?a:b;L<= a*b;L++)
    if(L%a == 0 && L%b == 0)
       return L;
  return 1;     
}

int fact(int n){
  int f = 1;
  while(n)
  {
    f = f*n;
    n--;
  }
  return f;
  
}

int isPrime(int n){
  int i;
  for(i = 2; i< n; i++)
    if(n%i==0)
        return 0;
  return 1;      
}


// cmd for windows  compiling a C source file (function.c) into a shared library (.so file)  ==> gcc --std=c11 -shared -o customlib1.dll function.c