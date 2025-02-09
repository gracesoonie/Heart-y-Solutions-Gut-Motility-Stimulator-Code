# Gut-Motility-Stimulator-Code
This repository contains files for Milestone A/1 and B/2.

The code utilizes ccourson's Hiwonder-xArm1S Github repository (https://github.com/ccourson/Hiwonder-xArm1S/tree/main/Python).

# Milestone-A-Code
This repository contains files for version 1 (V1) and version 2 (V2) of the Python code for Milestone A.

# V1 Code
The V1 code utilizes the servo positions recorded from the HiWonder xArm PC program and translate those positions into a Python script. This is a simple script that executes one cycle of the "bermuda triangle" pattern neonatal intensive care unit nurses perform during neonatal abdominal massages. 

# V2 Code
The V2 code allows the robot arm to execute the massage pattern in the V1 code continously for a maximum of 10 minutes. The massage pattern can be executed with three different levels of applied pressure: soft, medium, and hard. "Soft" indicates the lowest applied pressure level, "hard" indicates the greatest applied pressure level, and "medium" indicates an applied pressure level between "soft" and "hard".

The initial pressure level that the robot arm applies is determined by values that can be inputed, such as gestational age, weight, and lenght of NICU stay.

Throughout the duration of the massage, the pressure level can change due to the theoretical feedback system included in the code. The feedback system takes in the neonate's heart rate and blood oxygen levels to detect dangerous levels that will cause the robot arm to stop the massage or concerning rates of change that will cause the robot arm to apply less pressure.

