//
//  ALDS1_3_A.cpp
//  
//
//  Created by mk on 2015/11/30.
//
//

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace::std;

int top, S[1000];

void push(int x){
    S[++top] = x;
}

int pop(){
    top--;
    return S[top+1];
}


int main(int argc, const char * argv[]) {

    int a, b;
    top = 0;
    char s[100];
    //scanfでEOFを受け付けられない
    while (scanf("%s", s) != '\n') {
        printf("s=%s", s);
        if(s[0] == '+'){
            a = pop();
            b = pop();
            push(a+b);
        }else if(s[0] == '-'){
            b = pop();
            a = pop();
            push(a-b);
        }else if(s[0] == '*'){
            a = pop();
            b = pop();
            push(a*b);
        } else{
            push(atoi(s));
        }
    }
    
    printf("%d\n", pop());
    return 0;
}
