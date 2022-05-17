#include <stdio.h>
#include <stdlib.h>
#include "H_Lcd.h"
#include "H_Lcd_prv.h"
#include "GPIO.h"
extern const Lcdcfg_t Lcd_cfgArray[];
#define FUNCTION_SET	(uint8_t)0b00111000u
#define DISPLAY_CONTROL	(uint8_t)0b00001100u
#define DISPLAY_CLEAR	(uint8_t)0b00000001u
static void Lcd_EnableBulse(void);
static Lcd_Init_State_t Lcd_Init(void);
static void Lcd_SendStringProcess(void);
static void Lcd_ClearScreenProcess(void);
static Lcd_Req_t req = 0;
static String_t Buffer_string;
static void Lcd_EnableBulse(void)
{
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_EN].Lcd_Port , Lcd_cfgArray[LCD_EN].Lcd_Pin , GPIO_LOW);
}

void Lcd_SendCommand(uint8_t Copy_u8Command)
{
	uint8_t Loc_u8Counter;
	/*set RW to write low*/
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_RW].Lcd_Port , Lcd_cfgArray[LCD_RW].Lcd_Pin , GPIO_LOW);

	/*set RS to command to low*/
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_RS].Lcd_Port , Lcd_cfgArray[LCD_RS].Lcd_Pin , GPIO_LOW);

	/*send command*/
	for(Loc_u8Counter=LCD_DB0;Loc_u8Counter<8;++Loc_u8Counter)
	{
		Gpio_enuSetPintValue((void *)Lcd_cfgArray[Loc_u8Counter].Lcd_Port , Lcd_cfgArray[Loc_u8Counter].Lcd_Pin , (uint8_t)(Copy_u8Command>>Loc_u8Counter &(uint8_t)1u));
	}
	/*Enable pulse*/
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_EN].Lcd_Port , Lcd_cfgArray[LCD_EN].Lcd_Pin , GPIO_HIGH);
}
void Lcd_SendData(uint8_t Copy_u8Data)
{
	uint8_t Loc_u8Counter;
	/*set RW to write low*/
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_RW].Lcd_Port , Lcd_cfgArray[LCD_RW].Lcd_Pin , GPIO_LOW);

	/*set RS to command to high*/
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_RS].Lcd_Port , Lcd_cfgArray[LCD_RS].Lcd_Pin , GPIO_HIGH);

	/*send data*/
	for(Loc_u8Counter=LCD_DB0;Loc_u8Counter<8;++Loc_u8Counter)
	{
		Gpio_enuSetPintValue((void *)Lcd_cfgArray[Loc_u8Counter].Lcd_Port , Lcd_cfgArray[Loc_u8Counter].Lcd_Pin , (uint8_t)(Copy_u8Data>>Loc_u8Counter &(uint8_t)1u));
	}

	/*Enable pulse*/
	Gpio_enuSetPintValue((void *)Lcd_cfgArray[LCD_EN].Lcd_Port , Lcd_cfgArray[LCD_EN].Lcd_Pin , GPIO_HIGH);
}
static Lcd_Init_State_t Lcd_Init(void)
{
	static Lcd_Init_State_t Loc_Init_state = First_Delay;
	static uint8_t counter_firstdelay,Enable_Need;
	GpioPincfg_t loc_pincfg;
	if(Enable_Need == 1)
	{
		Enable_Need=0;
		Lcd_EnableBulse();
	}
	else
	{
		switch(Loc_Init_state)
		{
			case First_Delay:
				++counter_firstdelay ;
				if(counter_firstdelay>=20)
				{
					uint8_t counter =0;
					for(counter = 0 ;counter<11;++counter)
					{
						loc_pincfg.port=Lcd_cfgArray[counter].Lcd_Port;
						loc_pincfg.pin=Lcd_cfgArray[counter].Lcd_Pin;
						loc_pincfg.mode=MODE_OUTPUT_PUSH_PULL_PULL_UP;
						loc_pincfg.speed=SPEED_LOW;
						Gpio_enuinitPinCfg(&loc_pincfg);
					}
					Loc_Init_state = Function_set;
				}
				else
				{

				}
				break;
			case Function_set:
			{
				Lcd_SendCommand(FUNCTION_SET);
				Enable_Need=1;
				Loc_Init_state = Display_Control;
				break;
			}
			case Display_Control:
				Lcd_SendCommand(DISPLAY_CONTROL);
				Enable_Need=1;
				Loc_Init_state = Display_Clear;
				break;
			case Display_Clear:
				Lcd_SendCommand(DISPLAY_CLEAR);
				Enable_Need=1;
				Loc_Init_state = last_enable;
				break;
			case last_enable:
				Loc_Init_state =done;
				break;
			case done:

				break;
		}
	}
	return Loc_Init_state;
}
void Lcd_Task(void)
{
	static Lcd_Init_State_t Loc_Init_state = First_Delay;

	if(Loc_Init_state != done)
	{
		Loc_Init_state = Lcd_Init();
	}
	else
	{
		switch(req)
		{
			case idle:
				break;
			case write_str:
				Lcd_SendStringProcess();
				break;
			case clear_screen:
				Lcd_ClearScreenProcess();
				break;
		}
	}
}
ReqStatus_t Lcd_SendStringReq(String_t *Add_str)
{
	ReqStatus_t ReqSatus = RequestAccepted;
	if(req == idle)
	{
		Buffer_string = *Add_str;
		req=write_str;
	}
	else
	{
		ReqSatus = RequestNotAccepted;
	}
	return ReqSatus;
}
static void Lcd_SendStringProcess(void)
{
	static uint8_t Loc_StringCounter,Loc_Enable_Need;
	static Lcd_SendStringProcess_t Loc_SendStringstate = SetDDRAMAdress;
	if(Loc_Enable_Need == 1)
	{
		Loc_Enable_Need=0;
		Lcd_EnableBulse();
	}
	else
	{
		switch(Loc_SendStringstate)
		{
		case SetDDRAMAdress:
		{
			uint8_t Loc_u8Adress = 0;
			if(Buffer_string.x_pos==LCD_FIRST_LINE)
			{
				Loc_u8Adress=Buffer_string.y_pos;
			}
			else if(Buffer_string.x_pos==LCD_SCOND_LINE)
			{
				Loc_u8Adress=(uint8_t)(0x40+Buffer_string.y_pos);
			}
			Lcd_SendCommand((uint8_t)(Loc_u8Adress+128));
			Loc_Enable_Need = 1;
			Loc_SendStringstate = sendchar;
			break;
		}

		case sendchar:
			if(Buffer_string.copy_u8String[Loc_StringCounter] == '\0')
			{
				Loc_SendStringstate = SetDDRAMAdress;
				Loc_Enable_Need = 0;
				Loc_StringCounter = 0;
				req = idle;

			}
			else
			{
				Lcd_SendData((uint8_t)Buffer_string.copy_u8String[Loc_StringCounter]);
				Loc_Enable_Need = 1;
				++Loc_StringCounter;
			}
			break;
		}
	}
}
static void Lcd_ClearScreenProcess(void)
{
	static uint8_t Loc_Enable_Need;
	if(Loc_Enable_Need == 1)
	{
		Loc_Enable_Need=0;
		Lcd_EnableBulse();
		req=idle;
	}
	else
	{
		Lcd_SendCommand(DISPLAY_CLEAR);
		Loc_Enable_Need=1;
	}

}
ReqStatus_t Lcd_ClearScreenReq(void)
{
	ReqStatus_t ReqSatus = RequestAccepted;
	if(req == idle)
	{
		req=clear_screen;
	}
	else
	{
		ReqSatus = RequestNotAccepted;
	}
	return ReqSatus;
}
