#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<list>
#include<vector>
#include<queue>
#include<map>
using namespace std;
const int maxn=100010;
char str[maxn];
int main()
{
    int n,m;
    scanf("%d%d",&n,&m);
    scanf("%s",str+1);
    int ans=0,temp=m,l=1;
    for(int i=1;i<=n;++i){
        if(str[i]=='b')temp--;
        while(temp<0){
            if(str[l++]=='b')
            temp++;
            }
        ans=max(ans,i-l+1);
    }temp=m;l=1;
    for(int i=1;i<=n;++i){
        if(str[i]=='a')
        temp--;
        while(temp<0){
            if(str[l++]=='a')
            temp++;
            }
        ans=max(ans,i-l+1);
    }
    printf("%d\n",ans);
    return 0;
}