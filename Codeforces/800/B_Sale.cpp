#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    for (int i = 0; i < n;i++)
    {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int lav = 0, cnt = 0;

    for (int i = 0; i < n and cnt < m;i++)
    {
        if(a[i]<0)
        {
            lav += -a[i];
            cnt++;
        }

    }

    cout << lav << endl;
}