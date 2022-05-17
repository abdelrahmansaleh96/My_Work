#include "stdint.h"
#include "Gpio.h"
#include "KeyPad.h"




uint8_t KeysState[KEYPAD_MAX_RAWS][KEYPAD_MAX_COLS] = {Key_NotPressed};


const const KeyPadInit_t Loc_au8KeysPinsRows[KEYPAD_MAX_RAWS]=
{
		[0]={
				.Port=GPIOB,
				.Pin=6
			},

		[1]={
				.Port=GPIOB,
				.Pin=7
			},

		[2]={
				.Port=GPIOB,
				.Pin=8
			},

		[3]={
				.Port=GPIOB,
				.Pin=9
			}

};

const const KeyPadInit_t Loc_au8KeysPinsColms[KEYPAD_MAX_COLS]=
{
		[0]={
				.Port=GPIOB,
				.Pin=5
			},

		[1]={
				.Port=GPIOB,
				.Pin=4
			},

		[2]={
				.Port=GPIOB,
				.Pin=3
			},

		[3]={
				.Port=GPIOA,
				.Pin=12
			}

};



const uint8_t KeyPad_auint8_tKeys[KEYPAD_MAX_RAWS][KEYPAD_MAX_COLS]=
{
{'7', '8', '9','/'},
{'4', '5', '6','*'},
{'1', '2', '3','-'},
{'#', '0', '=','+'}
};
