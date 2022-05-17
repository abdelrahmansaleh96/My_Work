#include <stdio.h>
#include <stdlib.h>
#include "GPIO.h"
#include "H_Lcd.h"


const Lcdcfg_t Lcd_cfgArray[]=
{
		[LCD_DB0]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=0
		},
		[LCD_DB1]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=1
		},
		[LCD_DB2]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=2
		},
		[LCD_DB3]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=3
		},
		[LCD_DB4]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=4
		},
		[LCD_DB5]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=5
		},
		[LCD_DB6]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=6
		},
		[LCD_DB7]=
		{
				.Lcd_Port= GPIOA,
				.Lcd_Pin=7
		},
		[LCD_RS]=
		{
				.Lcd_Port= GPIOB,
				.Lcd_Pin=0
		},
		[LCD_RW]=
		{
				.Lcd_Port= GPIOC,
				.Lcd_Pin=14
		},
		[LCD_EN]=
		{
				.Lcd_Port= GPIOC,
				.Lcd_Pin=15
		},

};
