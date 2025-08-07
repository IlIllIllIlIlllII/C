#include <stdio.h>

int main(void)
{
    int a;
    int b;
    double result;
    
    scanf("%d %d", &a, &b);
    
    result = (double)a / b; // 정수 나눗셈이 아닌 실수 나눗셈으로 변환
    printf("%.16lf", result); // 소수점 16자리까지 출력
    
    return 0;
}
