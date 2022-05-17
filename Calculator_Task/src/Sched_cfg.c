#include <stdio.h>
#include <stdlib.h>

#include "Sched.h"
#include "Sched_cfg.h"
#include "app.h"
#include "H_Lcd.h"
#include "KeyPad.h"
#include "H_Lcd.h"

const Runnable_t runnables[]=
{
		[3]=
		{
				.Cbf          =  CheckKeypad,
				.CyclicTimeMS = 20,
		},

		[0]=
		{
				.Cbf    	  =  KeyPad_Task,
				.CyclicTimeMS =  2,
		},

		[1]=
		{
				.Cbf    	  =  Calc_Draw,
				.CyclicTimeMS =  2,
		},
		[2]=
		{
				.Cbf    	  =  Lcd_Task,
				.CyclicTimeMS =  2,
		},

};

