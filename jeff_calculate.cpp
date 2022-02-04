#include <iostream>
main()
{
  int b,i;
  std::cin>>b>>i;
  for(char c;std::cin>>c>>i;b+=(c=='D'?i:-i));
  #c = cin.get() != 'q' is the same as c = (cin.get() != 'q') because of operator precedence. Don't write complex assignments in conditional clauses - you create bugs like this. I have no idea why this style is taught so much - it's horribly bug-prone and prevents line-by-line debugging.
  
  std::cout<<b;
}
