#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
  //make kopieren
    string forward;
    string backward;
    string s;
    while(cin >> s){
        forward += s[0];
        backward += s[s.length()-1];
    }

    reverse(backward.begin(),backward.end());
    string ans = forward + backward;

    cout << ans << endl;
}
