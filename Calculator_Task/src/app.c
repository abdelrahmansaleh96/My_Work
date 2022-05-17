#include "stdint.h"
#include "H_Lcd.h"
#include "KeyPad.h"
#include "app.h"

static void clear_str(void);
static void Revers_Num(uint16_t copy_Number, uint8_t index_start);
static uint8_t  Glop_first_Op=0;
static uint8_t  Glop_Scond_Op=0;
static uint8_t  Glop_Op;
static uint8_t index_start=0;
#define persision 100

typedef enum
{
	op1,
	op2,
	op
}clacState_t;


typedef enum
{
	first_num,
	socnd_num
}Operand_t;

static String_t str={"               ",LCD_FIRST_LINE,0};

void CheckKeypad(void)
{
	static clacState_t CalcState   = op1;
	static Operand_t  Operand_state = first_num;
	volatile uint16_t res=0;
	uint8_t Loc_ReadKey;
	static uint8_t equal = 0;

	KeyPad_enuGetKey(&Loc_ReadKey);

	if(Loc_ReadKey != 0)
	{
		switch (CalcState)
		{
			case op1:
				if(Loc_ReadKey >='0' && Loc_ReadKey <= '9')
				{
					if(Operand_state == first_num )
					{
						clear_str();
						Glop_first_Op  = (Glop_first_Op)+ (Loc_ReadKey-'0');
						str.copy_u8String[index_start++]=Loc_ReadKey;
						Operand_state= socnd_num;

					}
					else
					{
						Glop_first_Op = Glop_first_Op * 10 + (Loc_ReadKey-'0');
						str.copy_u8String[index_start++]=Loc_ReadKey;
						Operand_state=first_num;
						CalcState = op;
					}
				}
				else if((Loc_ReadKey =='/' ||
						Loc_ReadKey =='*'||
						Loc_ReadKey =='-'||
						Loc_ReadKey =='+') && Operand_state== socnd_num )
					{
						Glop_Op = Loc_ReadKey;
						str.copy_u8String[index_start++]=Loc_ReadKey;
						CalcState = op2;
						Operand_state=first_num;
					}

			break;
			case op:
				if(Loc_ReadKey =='/' ||
					Loc_ReadKey =='*'||
					Loc_ReadKey =='-'||
					Loc_ReadKey =='+')
				{
					Glop_Op = Loc_ReadKey;
					str.copy_u8String[index_start++]=Loc_ReadKey;
					CalcState = op2;
				}
				break;
			case op2:
				if(Loc_ReadKey >='0' && Loc_ReadKey <= '9')
				{
					if(Operand_state == first_num )
					{
						Glop_Scond_Op  = (Glop_Scond_Op)+ (Loc_ReadKey-'0');
						str.copy_u8String[index_start++]=Loc_ReadKey;
						Operand_state= socnd_num;
					}
					else
					{
						Glop_Scond_Op = Glop_Scond_Op * 10 + (Loc_ReadKey-'0');
						str.copy_u8String[index_start++]=Loc_ReadKey;
						Operand_state=first_num;
						CalcState   = op1;
						equal = 1;
					}
				}
				else if(Loc_ReadKey == '=' && Operand_state == socnd_num )
				{
					CalcState   = op1;
					equal = 1;
					Operand_state = first_num;
				}
				break;
		}
	}
	if(equal == 1)
	{
		equal = 0;
		str.copy_u8String[index_start++]='=';
		if(Glop_Op == '+')
		{
			res = Glop_first_Op + Glop_Scond_Op;
		}
		else if (Glop_Op == '*')
		{
			res = Glop_first_Op * Glop_Scond_Op;
		}
		else if(Glop_Op == '-')
		{
			if(Glop_first_Op >= Glop_Scond_Op)
			{
				res = Glop_first_Op - Glop_Scond_Op;
			}
			else
			{
				res =  Glop_Scond_Op - Glop_first_Op;
				str.copy_u8String[index_start++]='-';
			}
		}
		else
		{
			if(Glop_Scond_Op == 0)
			{
				res = 0;
			}
			else
			{
				res = Glop_first_Op / Glop_Scond_Op;
			}
		}

		Revers_Num(res,index_start++);
		if(Glop_Op == '/')
		{
			res = ((Glop_first_Op * persision) /Glop_Scond_Op ) - res*100;
			str.copy_u8String[index_start++]='.';
			Revers_Num(res,index_start++);
		}
		if(Glop_Scond_Op == 0)
		{
			str.copy_u8String[index_start-3]='E';
			str.copy_u8String[index_start-2]='R';
			str.copy_u8String[index_start-1]='R';
			str.copy_u8String[index_start-0]='O';
			str.copy_u8String[index_start+1]='R';
		}

	}
}

void Calc_Draw(void)
{
	Lcd_SendStringReq(&str);
}


static void clear_str(void)
{
	uint8_t index;
	for(index = 0 ;index<16;++index)
	{
		str.copy_u8String[index]=' ';
	}
	Glop_first_Op=0;
	Glop_Scond_Op=0;
	index_start=0;
}

static void Revers_Num(uint16_t copy_Number, uint8_t index_start)
{
	uint16_t Local_reserved,index =0;
	if(copy_Number==0)
	{
		str.copy_u8String[index+index_start]='0';
	}
	else
	{
		Local_reserved = 1;
		while(copy_Number != 0)
		{
			Local_reserved = Local_reserved * 10 + copy_Number % 10;
			copy_Number/=10;
		}
		do
		{
			str.copy_u8String[index+index_start]=((Local_reserved%10)+'0');
			Local_reserved/=10;
			++index;
		}while(Local_reserved!=1);
	}
}


