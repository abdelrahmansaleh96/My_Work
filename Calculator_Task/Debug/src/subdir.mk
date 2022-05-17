################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/GPIO.c \
../src/H_Lcd.c \
../src/H_Lcd_cfg.c \
../src/KeyPad.c \
../src/KeyPad_cfg.c \
../src/RCC.c \
../src/Sched.c \
../src/Sched_cfg.c \
../src/Systick.c \
../src/app.c \
../src/main.c 

OBJS += \
./src/GPIO.o \
./src/H_Lcd.o \
./src/H_Lcd_cfg.o \
./src/KeyPad.o \
./src/KeyPad_cfg.o \
./src/RCC.o \
./src/Sched.o \
./src/Sched_cfg.o \
./src/Systick.o \
./src/app.o \
./src/main.o 

C_DEPS += \
./src/GPIO.d \
./src/H_Lcd.d \
./src/H_Lcd_cfg.d \
./src/KeyPad.d \
./src/KeyPad_cfg.d \
./src/RCC.d \
./src/Sched.d \
./src/Sched_cfg.d \
./src/Systick.d \
./src/app.d \
./src/main.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GNU Arm Cross C Compiler'
	arm-none-eabi-gcc -mcpu=cortex-m4 -mthumb -mfloat-abi=soft -Og -fmessage-length=0 -fsigned-char -ffunction-sections -fdata-sections -ffreestanding -fno-move-loop-invariants -Wall -Wextra  -g3 -DDEBUG -DUSE_FULL_ASSERT -DTRACE -DOS_USE_TRACE_SEMIHOSTING_DEBUG -DSTM32F401xC -DUSE_HAL_DRIVER -DHSE_VALUE=25000000 -I"../include" -I"../system/include" -I"../system/include/cmsis" -I"../system/include/stm32f4-hal" -std=gnu11 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -c -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


