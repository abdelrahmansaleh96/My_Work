#include <stdio.h>
#include <stdlib.h>

#include "diag/Trace.h"


#include "RCC.h"
#include "sched.h"
#include "KeyPad.h"

int main(int argc, char* argv[])
{
	(void)argc;
	(void)argv;
	RCC_EnablePriphralCLK(RCC_AHB1ENR_GPIOAEN_SET_M);
	RCC_EnablePriphralCLK(RCC_AHB1ENR_GPIOBEN_SET_M);
	RCC_EnablePriphralCLK(RCC_AHB1ENR_GPIOCEN_SET_M);
	KeyPad_Init();
	Sched_Init();
	Sched_Start();
	return 0;
}

