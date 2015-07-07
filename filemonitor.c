#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/inotify.h>
#include <unistd.h>
#include <string.h>

#define EVENT_SIZE ( sizeof (struct inotify_event) )
#define BUF_LEN ( 1024 * ( EVENT_SIZE + 16 ) )
void monitor_magicbox(void);
int length, i = 0;
int fd;
int wd;
int pid;
char buffer[BUF_LEN];
int moved_flag;
int ret;
struct inotify_event *event;

int main( int argc, char *argv[], char *envp[] )
{
  int length, i = 0;
  int fd;
  int wd;
  char buffer[BUF_LEN];
  struct inotify_event *event;
  

  fd = inotify_init();

  if ( fd < 0 ) {
    perror( "inotify_init" );
  }

  wd = inotify_add_watch( fd, "./MagicBox",
                         IN_MODIFY | IN_CREATE | IN_DELETE | IN_MOVED_TO | IN_MOVED_FROM);
 
 
while(1) {
   
  //if(pid == 0) printf("Inside the fork");
   
   length = read( fd, buffer, BUF_LEN );

  if ( length < 0 ) {
    perror( "read" );
  }

  while (i<length) {
   event = ( struct inotify_event * ) &buffer[ i ];
    if ( event->len ) {
     // Do nothing if Hidden or temporary file
     if(event->name[0] == '.' || event->name[strlen(event->name)-1] == '~') printf("Hidden file or Temporary filw . Ignoring....\n");
      // Check Activity
      else {
       
      if ( event->mask & IN_CREATE ) {
        if ( event->mask & IN_ISDIR ) {
          printf( "The directory %s was created.\n", event->name );
        }
        else {
          printf( "The file %s was created.\n", event->name );

         
        }
      }


       if ( event->mask & IN_MOVED_FROM ) {
        if ( event->mask & IN_ISDIR ) {
          printf( "The directory %s was moved out.\n", event->name );
        }
        else {
         
             pid = fork();
       if(pid!= 0) printf( "The file %s was MOVED OUT of MagicBox.\n", event->name );
           if(pid ==0) {
                      printf(" Child : %d \n", pid);
                 ;
                  printf("EXECL returned %d \n", ret);
                

                       }
        }
      }

      else if ( event->mask & IN_DELETE ) {
        if ( event->mask & IN_ISDIR ) {
          printf( "The directory %s was deleted.\n", event->name );
        }
        else {
          printf( "The file %s was deleted.\n", event->name );
        }
      }
      else if ( event->mask & IN_MODIFY ) {
        if ( event->mask & IN_ISDIR ) {
          printf( "The directory %s was modified.\n", event->name );
        }
        else {
          printf( "The file %s was modified.\n", event->name );
        }
      }
        else if ( event->mask & IN_MOVED_TO ) {
        if ( event->mask & IN_ISDIR ) {
          printf( "The directory %s was moved into MagicBox.\n", event->name );
        }
        else {
           pid = fork();
       if(pid!= 0) 
       {
         printf( "The file %s was MOVED INTO MagicBox.\n", event->name );
         char buff [100];
         printf("FileSplitter.py -i ./MagicBox/%s -n 3 -s",event->name);
         int var = sprintf(buff,"python ./ArrayBPXOREncoder.py %s",event->name);
         printf("ArrayBPXOREncoder %s",event->name);
         sleep(5);
         int ret = system(buff);
         var1 = sprintf(buff,"python ./upload_server1.py %s",event->name);
         printf("Uploaded to server 1 ");
          ret1 = system(buff);
          var1 = sprintf(buff,"python ./upload_server2.py %s",event->name);
         printf("Uploaded to server 2");
          ret1 = system(buff);
          var1 = sprintf(buff,"python ./upload_server3.py %s",event->name);
         printf("Uploaded to server 3");
          ret1 = system(buff);
          var1 = sprintf(buff,"python ./upload_server4.py %s",event->name);
         printf("Uploaded to server 4");
          ret1 = system(buff);
         

        }
           if(pid ==0) {
                  printf(" Child : %d \n", pid);

                  printf("EXECL returned %d \n", ret);
                 }
        }
      }
     
    }
    
   }
    i += EVENT_SIZE + event->len;
  }

 length =0;
 i=0;
}
 


  ( void ) inotify_rm_watch( fd, wd );
  ( void ) close( fd );

  exit( 0 );
}





