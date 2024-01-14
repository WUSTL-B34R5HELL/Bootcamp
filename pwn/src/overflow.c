#include <stdio.h>
#include <string.h>

void vuln(char *);

int main(int argc, char * argv[]){
	if(argc < 2){
		printf("Missing input argument\n");
		return 1;
	}
	vuln(argv[1]);
	return 0;
}

void vuln(char * input){
	char buffer[10];
	strcpy(buffer, input);
	puts(buffer);
}

void win(){
	printf("Here's your flag: bearshell{overflow-to-victory}\n");
}
