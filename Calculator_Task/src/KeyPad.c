


#include "stdint.h"
#include "KeyPad.h"
#include "KeyPad_Priv.h"
#include "Gpio.h"
#include "Systick.h"
#include <diag/Trace.h>


extern const KeyPadInit_t Loc_au8KeysPinsRows[KEYPAD_MAX_RAWS];
extern const KeyPadInit_t Loc_au8KeysPinsColms[KEYPAD_MAX_COLS];
extern const uint8_t KeyPad_auint8_tKeys[KEYPAD_MAX_RAWS][KEYPAD_MAX_COLS];

static uint8_t  PressedKey_state;

void KeyPad_Init(void)
{
	uint8_t index;
	GpioPincfg_t KeyPad_cfg;
	for(index = 0 ; index < KEYPAD_MAX_RAWS; ++index)
	{
		KeyPad_cfg.port  = Loc_au8KeysPinsRows[index].Port;
		KeyPad_cfg.pin   = Loc_au8KeysPinsRows[index].Pin;
		KeyPad_cfg.mode  = MODE_INPUT_PULL_UP;
		KeyPad_cfg.speed = SPEED_LOW;
		Gpio_enuinitPinCfg(&KeyPad_cfg);
	}
	for(index = 0 ; index < KEYPAD_MAX_COLS; ++index)
	{
		KeyPad_cfg.port  = Loc_au8KeysPinsColms[index].Port;
		KeyPad_cfg.pin   = Loc_au8KeysPinsColms[index].Pin;
		KeyPad_cfg.mode  = MODE_OUTPUT_PUSH_PULL_NOPULL_UP_NOPULL_DOWN;
		KeyPad_cfg.speed = SPEED_LOW;
		Gpio_enuinitPinCfg(&KeyPad_cfg);
		Gpio_enuSetPintValue((void*)Loc_au8KeysPinsColms[index].Port,Loc_au8KeysPinsColms[index].Pin ,GPIO_HIGH);
	}
}

void KeyPad_Task(void)
{
	static uint8_t counter =0 , prev_PressedKey = 0,PressedKey_private_state;
	volatile uint8_t Loc_u8CounterClm , Loc_u8counterRow;
	uint8_t Loc_u8Read = GPIO_HIGH,curr_PressedKey = 0;


	for(Loc_u8CounterClm = 0 ; Loc_u8CounterClm < KEYPAD_MAX_COLS  ; Loc_u8CounterClm++)
	{
		/*Activate the pattern*/
		Gpio_enuSetPintValue((void*)Loc_au8KeysPinsColms[Loc_u8CounterClm].Port,Loc_au8KeysPinsColms[Loc_u8CounterClm].Pin , GPIO_LOW);

		for(Loc_u8counterRow = 0 ; Loc_u8counterRow < KEYPAD_MAX_RAWS && Loc_u8Read == GPIO_HIGH ; Loc_u8counterRow++)
		{
			Gpio_enuGetPinValue((void*)Loc_au8KeysPinsRows[Loc_u8counterRow].Port,Loc_au8KeysPinsRows[Loc_u8counterRow].Pin, &Loc_u8Read);
		}
		/*Deactivate the pattern*/
	    Gpio_enuSetPintValue((void*)Loc_au8KeysPinsColms[Loc_u8CounterClm].Port,Loc_au8KeysPinsColms[Loc_u8CounterClm].Pin ,GPIO_HIGH);
		if(Loc_u8Read == GPIO_LOW)
		{
			curr_PressedKey = KeyPad_auint8_tKeys[Loc_u8counterRow-1][Loc_u8CounterClm];
			break;
		}
	}
	if(curr_PressedKey == prev_PressedKey)
	{
		++counter;
	}
	else
	{
		counter=0;
	}
	if(counter == 5)
	{
		if(curr_PressedKey == 0 && PressedKey_private_state != 0)
		{
			PressedKey_state = PressedKey_private_state;
		}
		PressedKey_private_state = curr_PressedKey;

		counter = 0;
	}
	prev_PressedKey = curr_PressedKey;
}




KeyPad_teunErrorStatus KeyPad_enuGetKey(uint8_t *Add_puint8_tPressedKey)
{
	KeyPad_teunErrorStatus ReturnStatus =Keypad_enuOk;

	if(Add_puint8_tPressedKey == (void*)0)
	{
		ReturnStatus = KeyPad_enuNullPointerErr;
	}
	else
	{
		*Add_puint8_tPressedKey = PressedKey_state;
		PressedKey_state = Key_NotPressed;
	}
	return ReturnStatus;
}


