#include<stdio.h> 
int main()
{
int i,j;//i控制行数，j控制列数
for(i=1;i<=9;i++)
 {
 	for(j=1;j<=i;j++)
 	printf("%d*%d=%-3d",j,i,i*j); 
 	printf("\n");
 } 

return 0;
}
