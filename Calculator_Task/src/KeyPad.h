/**
  ******************************************************************************
  * @file    KeyPad_Int.h
  * @author  Ahmed Hassan Hosny
  * @version V1
  * @date    Mar 19, 2022
  * @brief   Header file of KeyPad module.
  *
  ******************************************************************************
  */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef KEYPAD_INT_H_
#define KEYPAD_INT_H_

#include "KeyPad_cfg.h"

/* Defined Macros  -----------------------------------------------------------*/





typedef enum
{
	Keypad_enuOk,
	KeyPad_enuNullPointerErr,
}KeyPad_teunErrorStatus;


typedef enum
{
	Key_NotPressed,
	Key_Pressed,
}KeyPadStates_t;


#define KEYPAD_TIMEPERIOD					(uint8_t)(0x02U)


void KeyPad_Task(void);


/* KeyPad APIS  -----------------------------------------------------------------*/

/**
  * @brief This function used to find the pressed key in the keypad
  *
  * @param  Add_puint8_tPressedKey: Address of the variable that will hold the key status
  *
  * @retval KeyPad_teunErrorStatus: return variable of type enum that contains the error status
  */
KeyPad_teunErrorStatus KeyPad_enuGetKey(uint8_t* Add_puint8_tPressedKey);


void KeyPad_Init(void);




#endif /* KEYPAD_INT_H_ */
