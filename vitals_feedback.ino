const int valvePins[] = {1, 2, 3, 4};  // Valve control pins

// Test vitals data for simulation
int heartRateValues[] = {130, 130, 130, 130, 130};
int spo2Values[] = {95, 95, 95, 95, 95};
int respRateValues[] = {40, 40, 40, 40, 40};

const int numReadings = sizeof(heartRateValues) / sizeof(heartRateValues[0]);

int currentIndex = 0;  // Index to track current reading from the arrays

int openTime = 1000;   // Initial open time, set based on conditions
int gestationalAge = 30;  // Manually input for simulation
int weight = 1000;  // Manually input for simulation

int previousHeartRate = heartRateValues[0];
unsigned long lastReadTime = 0;
unsigned long lastHeartRateCheck = 0;
unsigned long lastStableCheck = 0;
unsigned long startMillis = 0;
bool systemRunning = true;

const unsigned long duration = 10 * 60000;  // 10 minutes in milliseconds
const unsigned long readInterval = 1000;    // Interval for reading values (1 second)
const unsigned long heartRateCalcInterval = 5000;  // Interval for heart rate calculation (5 seconds)
const unsigned long stabilityInterval = 60000;     // Heart rate stability interval (60 seconds)


void setup() {
  // Initialize valve pins
  for (int i = 0; i < 4; i++) {
    pinMode(valvePins[i], OUTPUT);
  }

  // Initialize Serial communication
  Serial.begin(9600);

  // Determine initial open time based on gestational age and weight
  if (gestationalAge < 32 || weight < 1500) {
    openTime = 300;
  } else if ((gestationalAge >= 32 && gestationalAge < 37) || (weight >= 1500 && weight < 2500)) {
    openTime = 600;
  } else {
    openTime = 1000;
  }

  // Initialize the start time
  startMillis = millis();
  lastReadTime = startMillis;
  lastHeartRateCheck = startMillis;
  lastStableCheck = startMillis;
}

void loop() {
  if (!systemRunning) {
    return;
  }

  unsigned long currentTime = millis();

  // Read inputs and check conditions at a specified interval
  if (currentTime - lastReadTime >= readInterval) {
    // Read simulated sensor values
    int heartRate = heartRateValues[currentIndex];
    int spo2 = spo2Values[currentIndex];
    int respRate = respRateValues[currentIndex];

    // Vitals safety threshold checks
    if (heartRate < 120 || heartRate > 170) {
      Serial.print("Heart rate out of range: "); Serial.println(heartRate);
      stopSystem();
      return;
    }
    if (spo2 < 91) {
      Serial.print("SpO2 out of range: "); Serial.println(spo2);
      stopSystem();
      return;
    }
    if (respRate < 30 || respRate > 60) {
      Serial.print("Respiratory rate out of range: "); Serial.println(respRate);
      stopSystem();
      return;
    }

    // Print the values for the Serial Plotter
    Serial.print("HeartRate "); Serial.print(heartRate); Serial.print(" ");
    Serial.print("SPO2 "); Serial.print(spo2); Serial.print(" ");
    Serial.print("RespRate "); Serial.print(respRate); Serial.print(" ");
    Serial.print("ValveOpenTime "); Serial.println(openTime);

    // Update index and lastReadTime
    currentIndex = (currentIndex + 1) % numReadings;
    lastReadTime = currentTime;
  }

  // Check and calculate heart rate changes every 5 seconds
  if (currentTime - lastHeartRateCheck >= heartRateCalcInterval) {
    int currentHeartRate = heartRateValues[currentIndex];  // Current heart rate from array
    int heartRateChange = currentHeartRate - previousHeartRate;

    // Adjust open time based on heart rate changes
    if (heartRateChange >= 10) {
      openTime = max(openTime - 100, 0);  // Decrease by 100 ms
    } else if (heartRateChange >= 5 && heartRateChange < 10) {
      openTime = max(openTime - 50, 0);   // Decrease by 50 ms
    }

    previousHeartRate = currentHeartRate;
    lastHeartRateCheck = currentTime;
  }

  // Increase openTime by 50ms if heart rate is stable for 1 minute
  if (currentTime - lastStableCheck >= stabilityInterval) {
    int heartRateChange = heartRateValues[currentIndex] - previousHeartRate;
    if (abs(heartRateChange) < 5) {
      openTime += 50;  // Increase by 50 ms for stability
      Serial.println("ValveOpenTime increased by 50ms due to stable heart rate.");
    }
    lastStableCheck = currentTime;
  }

  // Check if openTime has reached 0
  if (openTime == 0) {
    Serial.println("ValveOpenTime reached 0, stopping system.");
    stopSystem();
    return;
  }

  // Valve control - 
  // Will need to change once we have all valves connected and
  // know how to activate them sequentially!!
  static unsigned long lastValveTime = 0;
  static int valveIndex = 0;
  static bool valveState = LOW;

  if (currentTime - lastValveTime >= openTime) {
    if (valveState == LOW) {
      digitalWrite(valvePins[valveIndex], LOW);
      valveState = HIGH;
      lastValveTime = currentTime;
    } else {
      digitalWrite(valvePins[valveIndex], HIGH);
      valveState = LOW;
      lastValveTime = currentTime;
      valveIndex = (valveIndex + 1) % 4;  // Move to next valve
    }
  }
  
  // Check if the massage should end based on duration
  if (currentTime - startMillis > duration) {
    Serial.println("Massage performed for 10 minutes");
    stopSystem();
  }
}

void stopSystem() {
  systemRunning = false;
  Serial.println("System stopped");
}