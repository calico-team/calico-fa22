#include<bits/stdc++.h>
#define endl '\n'
using namespace std;
const int MAX_N = 1e3+2;
pair<int,int> person[MAX_N];
void solve()
{
    int n;
    int num;
    cin>>n;
    for(int i=0; i<n; i++)
    {
        cin>>num;
        person[i] = {num,i};
    }
    sort(person,person+n);
    long long ans = 0;
    for(int i=0; i<n; i++)
    {
        ans+=(person[i].first*(n-i));
    }
    cout<<ans<<endl;
    for(int i=0; i<n; i++)
    {
        cout<<person[i].second+1<<" ";
    }
    cout<<endl;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int T;
    cin>>T;
    for(int test_number=1; test_number<=T; test_number++)
    {
        solve();
    }
}
