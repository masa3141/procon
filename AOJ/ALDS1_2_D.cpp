//
//  ALDS1_2_D.cpp
//  
//
//  Created by mk on 2015/11/27.
//
//

#include <stdio.h>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <iostream>
using namespace::std;


long long cnt;
int l;
int A[1000000];
int n;
vector<int> G;

void insertionSort(int A[], int n, int g){
    for (int i=g; i<n; i++) {
        int v = A[i];
        int j = i - g;
        while (j >= 0 && A[j] > v) {
            A[j + g] = A[j];
            j -= g;
            cnt++;
        }
        A[j + g] = v;
//        printf("i=%d,g=%d,j=%d,v=%d\n",i,g,j,v);
//        printf("---\n");
//        for (int i = 0; i < n; i++) {
//            cout << A[i];
//            if(i != n-1){
//                cout << " ";
//            }
//        }
//        cout << endl;
    }

}


void shellSort(int A[], int n){
    for (int h=1; ; ) {
        if (h > n) break;
        G.push_back(h);
        h = 3*h + 1;
    }
    for (int i = G.size()-1; i >= 0; i--) {
        insertionSort(A, n, G[i]);
    }
}

int main(int argc, const char * argv[]) {
    cin >> n;
    for (int i = 0; i<n; i++) {
        scanf("%d", &A[i]);
    }
    cnt = 0;
    
    shellSort(A,n);
    
    cout << G.size() << endl;
    for (int i=G.size() - 1; i >= 0; i--) {
        printf("%d", G[i]);
        if(i)printf(" ");
    }
    printf("\n");
    printf("%lld\n", cnt);
    for (int i=0; i<n; i++) {
        printf("%d\n", A[i]);
    }
    
    return 0;
    
}
