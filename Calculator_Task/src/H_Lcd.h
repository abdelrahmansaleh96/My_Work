#ifndef H_LCD_H_
#define H_LCD_H_

#include "H_Lcd_cfg.h"
#include "H_Lcd_prv.h"

#define LCD_u8stringSize  		16
#define LCD_FIRST_LINE			0
#define LCD_SCOND_LINE			1
typedef enum
{
	First_Delay=0,
	Function_set=1,
	Display_Control=2,
	Display_Clear=3,
	last_enable=5,
	done=4,
}Lcd_Init_State_t ;

typedef enum
{
	SetDDRAMAdress,
	sendchar

}Lcd_SendStringProcess_t;


typedef enum
{
	idle,
	write_str,
	clear_screen
}Lcd_Req_t;
typedef struct
{
	uint32_t Lcd_Port;
	uint8_t	 Lcd_Pin;
	uint8_t  res2[3];
}Lcdcfg_t;
typedef struct
{
	char  copy_u8String[LCD_u8stringSize];
	uint8_t x_pos;
	uint8_t y_pos;
}String_t;

typedef enum
{
	RequestAccepted,
	RequestNotAccepted
}ReqStatus_t;








void Lcd_SendCommand(uint8_t Copy_u8Command);
void Lcd_SendData(uint8_t Copy_u8Data);

ReqStatus_t Lcd_SendStringReq(String_t *Add_str);
void Lcd_SendString(char copy_u8String[LCD_u8stringSize]);
ReqStatus_t Lcd_ClearScreenReq(void);
void Lcd_ClearScreen(void);
void Lcd_SendNumber(uint32_t copy_u32Number);
void Lcd_GotoXYpostion(	uint8_t copy_u8x,uint8_t copy_u8y);
void Lcd_WriteSpecialcharacter(uint8_t *copy_pu8pattern,uint8_t copy_u8PatternNumper,uint8_t copy_u8x,uint8_t copy_u8y);


void Lcd_Task(void);


#endif
