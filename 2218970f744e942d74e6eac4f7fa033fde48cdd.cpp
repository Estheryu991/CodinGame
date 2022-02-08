#include<bits/stdc++.h>

using namespace std;

int main()
{
    int a,b;
    vector<pair<int,int>> c;
    cin>>a>>b;
    cout<<a/b<<".";
    do
    {
        a=a%b*10;
        pair<int,int> q(a,a/b);
        auto it = find(c.begin(),c.end(),q);
        if(it != c.end())
            break;
        else
            c.push_back(q);

    }while(1);
    
    for(auto it:c)
    {
        if(it.first == a)
            cout<<"(";
        cout<<it.second;
    }
    cout << ")";
}
