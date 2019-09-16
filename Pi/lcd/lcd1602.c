#include <stdio.h>                                                                        
#include <wiringPi.h>                                                             
#include <mcp23017.h>
#include <lcd.h>
 
int main()
{
        int display,i,count;
        wiringPiSetup();
        mcp23017Setup (100, 0x20);
        printf ("Raspberry Pi - MCP23017 Testn");
        for(i=0;i<16;i++)
          pinMode(100+i,OUTPUT);
        digitalWrite(114,0);
        display=lcdInit(2,16,4,115,113,112,111,110,109,0,0,0,0);
        lcdHome(display);
        lcdClear(display);
        lcdPosition(display,0,0);
        lcdPuts(display,"Hello World");
        while(1)
        {
                lcdPosition(display,0,1);                                                                                       
                lcdPrintf(display,"%d",count++);
                delay(300);
                printf("lcd1602n");
        }
}
