/* 
In C++ way of handle Memory Management ==>

1. Pointer (Same As C)  ==> 
   In pointer we have more Authority on memory same as c. and this is the reason of safety issue like: memory leak etc.

2. Reference Variable ==>
   Power/Authority decrease  AND Safety Increase
   In this we use '&' sigh instead of '*'.

3. Smart Pointer ==>   Allowing Automatic memory management

*/
//2. Reference Variable ==>
void f1(){
  int a = 10; 
  int &x = a;   // created with & symbol and Necessary to initialize and Contain only one value through out the program 
  x++;  // this line increase a not x.
}

//3. Smart Pointer ==>
// unique_ptr is a template class and p is a object of this class. With the end of this object pointer will automatically destroy.

// int f2(){
//   unique_ptr <int> p(new (int(20)));
// }