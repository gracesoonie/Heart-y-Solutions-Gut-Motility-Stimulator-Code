# Gut Motility Stimulator Code
This repository contains files for Milestone 1 and 2.

The code utilizes ccourson's Hiwonder-xArm1S Github repository (https://github.com/ccourson/Hiwonder-xArm1S/tree/main/Python).

---------------------------------------------------------------------------------------------------------------------------------------------

# Milestone 1 V1 Code
The V1 code utilizes the servo positions recorded from the HiWonder xArm PC program and translate those positions into a Python script. This is a simple script that executes one cycle of the "bermuda triangle" pattern neonatal intensive care unit nurses perform during neonatal abdominal massages. 

# Milestone 1 V2 Code
The V2 code allows the robot arm to execute the massage pattern in the V1 code continously for a maximum of 10 minutes. The massage pattern can be executed with three different levels of applied pressure: soft, medium, and hard. "Soft" indicates the lowest applied pressure level, "hard" indicates the greatest applied pressure level, and "medium" indicates an applied pressure level between "soft" and "hard".

The initial pressure level that the robot arm applies is determined by values that can be inputed, such as gestational age, weight, and length of NICU stay.

Throughout the duration of the massage, the pressure level can change due to the theoretical feedback system included in the code. The feedback system takes in the neonate's heart rate and blood oxygen levels to detect dangerous levels that will cause the robot arm to stop the massage or concerning rates of change that will cause the robot arm to apply less pressure.

---------------------------------------------------------------------------------------------------------------------------------------------

# Milestone 2 Force Sensing Resistor (FSR) Code
This code builds on Milestone 1 V1 Code. We took the FSR measurements from the NICU nurse and attempted to mimic the measurements using the robot arm. The code displays the positions that we found most accurately followed the NICU nurse's FSR measurements. 

# Milestone 2 BodiTrak Code
This code builds on Milestone 1 V2 Code. The changed made are the following:

**Updated positions for the three different levels of applied pressure**:
The BodiTrak pressure mat was used for the pressure measurements. The positions are a product of our attempts to mimic the pressure measurements gathered from a team member's attempt at performing an abdominal massage at three different pressure levels. 

**Deletion of consideration of length of NICU stay**:
After speaking to one of the NICU nurses, she expressed that length of NICU stay is not considered when determining the initial pressure of the abdominal massage. Therefore, we have removed it from the code.

**Addition of respiratory rate in vital signs monitoring**:
After speaking to one of the NICU nurses, she expressed that respiratory rate, along with heart rate and blood oxygen percentage, are monitored during the massage and used as a metric to determine how to change the pressure applied. Therefore, we have added a variable for respiratory rate that will be monitored throughout the massage. If respiratory rate goes above the maximum or below the minimum respiratory rate set, then the Gut Motility Stimulator will stop the massage. 
