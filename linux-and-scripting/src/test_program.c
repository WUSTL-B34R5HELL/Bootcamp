#include <stdio.h>
#include <string.h>

int main(){
	char * flag = "bearshell{pYth0n1s3AsY}";
	printf("Hello, welcome to my awesome program\nEnter the numbers 1-10,000 to get the flag\n");
	
	int input;
	int correct = 1; //booleans don't exist in c
	int i = 1;
	for(i; i <= 10000; ++i){
		printf("Enter next number: ");

		scanf("%d", &input);
		if (input != i){
			correct = 0;
			break;
		}
	}

	if(correct) printf("Congrats! Here's your flag: %s\n", flag);
}
