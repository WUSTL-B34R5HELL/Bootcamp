#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <libgen.h>
#include <stdlib.h>
#include <string.h>
#include <linux/limits.h>

#define winning_name "output"

char * flag = "bearshell{fds-for-the-win}";

void win(){
  printf("Congrats! Here's your flag: %s\n", flag);
}

int main(){  
  //determine file name
  char buf[PATH_MAX + 1];
  int size = readlink("/proc/self/fd/1", buf, PATH_MAX);
  if (size < 0){
    perror("readlink");
    exit(1);
  }
  buf[size + 1] = '\00';
  char * file_name = basename(buf);
  printf("Current output file: %s\n", file_name);

  //take last 
  if(!strncmp(file_name, winning_name, PATH_MAX)){
    win();
  }
  else{
    printf("You lose! Try again.\n");
  }
}
