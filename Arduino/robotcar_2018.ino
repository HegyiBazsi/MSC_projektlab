#include <AFMotor.h>
#include <EEPROM.h>

AF_DCMotor left(3, MOTOR34_1KHZ);
AF_DCMotor right(4, MOTOR34_1KHZ);

#define RECEIVE_TIMEOUT 3000
#define ADDRESS  1
#define ADDRESS2  2
#define DEFAULT_VALUE 170
#define DEFAULT_VALUE2 20
#define ECHO       9    //Pin of Arduino that is to be connected to the ECHO pin of the sensor.
#define TRIGGER    8    //Pin of Arduino that is to be connected to the TRIG pin of the sensor.
#define TRUE  1   //Constants for Boolean variables.
#define FALSE 0
#define CYCLE_TIME  500    //Measurement periodicity, ms.
#define TRIGGER_PULSE_WIDTH   11  //To launch ultrasonic wave pulses the TRIG pin of the sensor shall
                                  //get a pulse of at least 10 microseconds.
#define INITIALIZING_DELAY    10    //An arbitrary delay in ms to let the sensor wake up.
#define DISTANCE_DIVIDER         58   //A constant to get the result in centimeters.
#define RANGE_LIMIT_TIMEOUT    8700   //The maximum distance is defined to be 150 cm.
#define NO_ECHO_TIMEOUT         700   //Time-out value for the echo to arrive.
#define MUTE_TIMEOUT            200   //Time-out value for a mute period.
#define DISTANCE_VALUE_AT_TIMEOUT   0xFFFFFFFF    //Invalid value if the obstacle is too far.

byte val3, val2, val1, val;
byte char1, char2, char3, char4;
byte char5, char6;
byte valid = 1;
int number = 0;
int emer_distance = 0;
unsigned long time_stamp;
unsigned int distance;    //Variable for the distance. Unit: cm.

/*-------------------*/
/*----- E N U M -----*/
/*-------------------*/

typedef enum {  OK,                      //No error - OK.
                ECHO_PIN_LEVEL_HIGH,     //The signal level must be LOW before the echo arrives. If not it shall be indicated.
                NO_ECHO,                 //There is no echo - time-out has been reached.
                OUT_OF_RANGE             //Obstacle too far.
              } SENSOR_ERROR;

/*----------------------------------------------*/
/*-----T R I G G E R   U L T R A S O U N D -----*/
/*----------------------------------------------*/

void triggerUltraSound(void)
{
  digitalWrite(TRIGGER,HIGH);
  delayMicroseconds(TRIGGER_PULSE_WIDTH);
  digitalWrite(TRIGGER,LOW);
}

/*-----------------------*/
/*----- P H A S E 1 -----*/
/*-----------------------*/

byte phase_1(void)
{
  byte error = FALSE;   //First we assume that there will be no error.
  unsigned long timestamp = micros();   //Getting a time stamp.

  while (micros() - timestamp <= MUTE_TIMEOUT)    //Monitoring the signal level for a time determined by constant MUTE_TIMEOUT.
  {
    if (digitalRead(ECHO) == HIGH)    //If the signal level gets HIGH...
    {
      error = TRUE;                   //...there is an error.
      break;                          //Jumping out of the 'while' cycle.
    }
  }
  return error;
}

/*-----------------------*/
/*----- P H A S E 2 -----*/
/*-----------------------*/

byte phase_2(void)
{
  byte error = TRUE;            //First we assume that there will be an error.
  unsigned long timestamp = micros();     //Getting a time stamp.

  while (micros() - timestamp <= NO_ECHO_TIMEOUT)    //Monitoring the signal level for a time determined by constant NO_ECHO_TIMEOUT.
  {
    if (digitalRead(ECHO) == HIGH)    //If the signal level gets HIGH...
    {
      error = FALSE;                  //...everything is fine.
      break;                          //Jumping out of the 'while' cycle.
    }
  }
  return error;
}

/*-----------------------*/
/*----- P H A S E 3 -----*/
/*-----------------------*/

byte phase_3(unsigned long* ppulse_width)
{
  byte error = TRUE;            //First we assume that there will be an error.
  unsigned long timestamp = micros();     //Getting a time stamp.

  while (micros() - timestamp <= RANGE_LIMIT_TIMEOUT)     //Monitoring the signal level for a time determined by constant RANGE_LIMIT_TIMEOUT.
  {
    if (digitalRead(ECHO) == LOW)     //If the signal level gets LOW...
    {
      error = FALSE;              //...everything is fine.
      *ppulse_width = micros() - timestamp;   //Calculating the length of the ECHO pulse.
      break;                      //Jumping out of the 'while' cycle.
    }
  }
  return error;
}
/*----------------------------------*/
/*----- M E A S U R E   E C H O-----*/
/*----------------------------------*/

void measureEcho(unsigned long* ppw, SENSOR_ERROR* perr)
{
  SENSOR_ERROR error_code = OK;     //First we assume that there will be no error.
  unsigned long pulse_width = DISTANCE_VALUE_AT_TIMEOUT;      //Initial and invalid value for the length of the ECHO pulse.

  if (phase_1() == TRUE)       //Monitoring the ECHO sognal level in PHASE1.
  {
    error_code = ECHO_PIN_LEVEL_HIGH;   //Indicating that there was an error, i.e. the ECHO level got HIGH too early.
  }
  else if (phase_2() == TRUE) //Monitoring the ECHO sognal level in PHASE2.
  {
    error_code = NO_ECHO;                //Indicating that there was an error, i.e. the ECHO pulse did not arrive in time.
  }
  else if (phase_3(&pulse_width) == TRUE)   //Monitoring the ECHO sognal level in PHASE3.
  {
    error_code = OUT_OF_RANGE;           //Indicating that there was an error, i.e. the ECHO pulse is too long.
  }
  else
  {}    //We love MISRA C...

  *perr = error_code;     //The error code is returned.
  *ppw = pulse_width;     //The measured (or the initial) pulse width is returned.
}

/*-----------------------------------*/
/*----- D I S P L A Y   D A T A -----*/
/*-----------------------------------*/

unsigned int displayData(unsigned long pulse_width, SENSOR_ERROR error_code)
{
  unsigned int distance;
  
  if(error_code != OK)    //If there was any error...
  {
    Serial.print("Measurement error. Error code: ");
    Serial.print(error_code, DEC);
    Serial.print(". ");

    switch(error_code)    //...the error message is sent according to the error type.
    {
      case ECHO_PIN_LEVEL_HIGH:
          Serial.println("Echo's signal level high.\n");
          break;
      case NO_ECHO:
          Serial.println("Echo time out.\n");
          break;
      case OUT_OF_RANGE:
          Serial.println("Obstacle too far.\n");
          break;
    }
  }
  else    //If there was no error...
  {
    //distance = (unsigned int)(pulse_width / DISTANCE_DIVIDER);    //Calculating the distance in cm.
    distance = (unsigned int)((pulse_width + DISTANCE_DIVIDER/2) / DISTANCE_DIVIDER);    //Calculating the distance in cm, with rounding.
    
    Serial.print("Measured pulse width = ");
    Serial.print(pulse_width,DEC);
    Serial.print(" microseconds. Distance = ");
    Serial.print(distance,DEC);
    Serial.println(" cm.\n");
  }
  return distance;
}

/*---------------------*/
/*----- S E T U P -----*/
/*---------------------*/
void setup()
{
	Serial.begin(9600); 
	
	byte stored_speed; 		//Variable to store the cruise control speed stored_speed read out from the EEPROM.
	byte stored_distance;    	//Variable to store the emergency stop distance stored_speed read out from the EEPROM.
	
	stored_speed = EEPROM.read(ADDRESS);
	stored_distance = EEPROM.read(ADDRESS2);

  pinMode(ECHO, OUTPUT);
  pinMode(TRIGGER, OUTPUT);
  digitalWrite(ECHO,LOW);       //According to the manual the sensor's both pins are first
  digitalWrite(TRIGGER,LOW);    //initialized by putting low level voltage to them.

  delay(INITIALIZING_DELAY);    //An arbitrary delay.
  
  pinMode(ECHO, INPUT);         //After this the Arduino's pin dedicated to ECHO is set as INPUT.
  
	Serial.print("Cruise control data stored in the EEPROM: ");
	Serial.println(stored_speed,DEC); 
	
	if (stored_speed >= 150 && stored_speed <= 200)   //Is the value read out in the range of validity?
	{
		number = stored_speed;   //Yes, it is.
	}
	else
	{
		number = DEFAULT_VALUE;    //No, it is not, so the default value is applied.
		write_value_to_EEPROM();   //The default value is saved into the EEPROM immediately.
	}
	
	Serial.print("Emergency stop distance data stored in the EEPROM: ");
	Serial.println(stored_distance,DEC);  
	
	if (stored_speed >= 10 && stored_speed <= 40)   //Is the value read out in the range of validity?
	{
		emer_distance = stored_distance;   //Yes, it is.
	}
	else
	{
		emer_distance = DEFAULT_VALUE2;    //No, it is not, so the default value is applied.
		write_distance_to_EEPROM();   //The default value is saved into the EEPROM immediately.
	}
	
//MENU	
	Serial.println();
	Serial.println("---------------------------------- M E N U -----------------------------------");
	Serial.println("---------- Press C now to enter into   C A L I B R A T I O N   mode ----------");
	Serial.println();
	Serial.println("------------------------------S U B    M E N U -------------------------------");
	Serial.println("Press c now to enter into   C R U I S E   C O N T R O L   S E T T I N G   mode");
	Serial.println("Press e now to enter into   E M E R G E N C Y   S T O P   S E T T I N G   mode");
	Serial.println();
	
//Clock starts here	
	time_stamp = millis();  
}

/*-------------------------------------------------*/
/*----- W R I T E   C C S   T O  E E P R O M  -----*/
/*-------------------------------------------------*/
//CCS = Cruise Control Speed

void write_value_to_EEPROM(void)
{
	EEPROM.write(ADDRESS,number);
}

/*-------------------------------------------------*/
/*----- W R I T E   E S D   T O  E E P R O M  -----*/
/*-------------------------------------------------*/
//ESD = Emergency Stop Distance

void write_distance_to_EEPROM(void)
{
	EEPROM.write(ADDRESS2,emer_distance);
}	

/*-------------------*/
/*----- L O O P -----*/
/*-------------------*/

void loop() 
{
//Here we enter into calibration mode, if we press the button C  
	if(millis()-time_stamp < RECEIVE_TIMEOUT)
	{		
		if (Serial.available() == 1)
		{ 
			val = Serial.read();
			if(val == 'C')
			{
				Serial.println("CALIBRATION");
				val1 = val; 
				while (val1 == val) 
				{
//Here we enter into cruise control mode, if we press the button c          
					if (Serial.available() == 1)
					{
						val1 = Serial.read();
						if(val1 == 'c')
						{
							Serial.println("Cruise control"); 
							val2 = val1;
							while(val2 == val1)
							{
								if(Serial.available() == 3)
								{
									char2 = Serial.read();
									char3 = Serial.read();
									char4 = Serial.read();
				
									if ( (char2 < '0') || (char2 > '9') ) valid = 0;
									if ( (char3 < '0') || (char3 > '9') ) valid = 0;
									if ( (char4 < '0') || (char4 > '9') ) valid = 0;
					
									number = ( char2 - '0' ) * 100 + ( char3 - '0' ) * 10 + ( char4 - '0' );
				
									if ( (number < 150) || (number > 200)) valid = 0;
				
									if (valid == 1)    //The incoming characters were valid, so a legal number could be formed.
									{               
										Serial.print("Speed: ");
										Serial.println(number, DEC);    //Sending back the value of the incoming number in decimal form.
										Serial.println();               
										adjustMotor(number);
										write_value_to_EEPROM();                 //Saving this value into the EEPROM.								
										Serial.println("\nSpeed value OK");
									}
									else
									{
										Serial.println("\nWrong command\n");
										break;
									}
								}
							}
						}//val = 'c' 
			  
	//Here we enter into emergency exit mode, if we press the button e                    
						else if(val1 == 'e')
						{
							Serial.println("Emergency stop");   
							val3 = val1;
							while(val3 == val1)
							{
								if(Serial.available() == 2)
								{
									char5 = Serial.read();
									char6 = Serial.read();
								
									if ( (char5 < '0') || (char5 > '9') ) valid = 0;
									if ( (char6 < '0') || (char6 > '9') ) valid = 0;
					
									emer_distance = ( char5 - '0' ) * 10 + ( char6 - '0' );
				
									if ( (emer_distance < 10) || (emer_distance > 41)) valid = 0;
				
									if (valid == 1)    //The incoming characters were valid, so a legal number could be formed.
									{               
										Serial.print("Min distance: ");
										Serial.println(emer_distance, DEC);    //Sending back the value of the incoming number in decimal form.
										Serial.println();  
										write_distance_to_EEPROM();                 //Saving this value into the EEPROM.								
										Serial.println("\nDistance Value OK");									  
									}
									else
									{
									  Serial.println("\nWrong command\n");
									  break;
									}
								}
							}
						}     
	//In case if we press any other buttons, we receive the following error line          
						else
						{
							Serial.println("Wrong command");
						}
					}
				} 
			}
		}
	}
//In case we don't press the button C, the cruise control mode starts to run	
	else
	{   
    unsigned long pulse_width;    
    SENSOR_ERROR error_code;      
    triggerUltraSound();                      
    measureEcho(&pulse_width,&error_code);
       
    unsigned int mert_tav = displayData(pulse_width,error_code);
    if(mert_tav >= emer_distance)
    {
      adjustMotor(number);    
    }
    else
    {
      adjustMotor(number/2);
      delay(3);
      adjustMotor(0);
    }
    delay(CYCLE_TIME);                       
	}
}

/*-----------------------------------*/
/*----- A D J U S T   M O T O R -----*/
/*-----------------------------------*/

void adjustMotor(int value)
{
	byte PWM_speed;

	if (value >=0 )
	{
		PWM_speed = (byte)value;
	}
	else
	{
		PWM_speed = (byte)(-value);
	}
  
	right.setSpeed(PWM_speed);
	left.setSpeed(PWM_speed);

	if (value == 0)
	{
		right.run(RELEASE);
		left.run(RELEASE);
	}
	else if (value > 0 )
	{
		right.run(FORWARD);
		left.run(FORWARD);
	}
}
