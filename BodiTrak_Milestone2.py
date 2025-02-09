import xarm
import time
import threading

arm = xarm.Controller('USB')

# Placeholder functions for vital sign data (replace with actual direction to get vitals from NICU monitor)
def get_heart_rate():
    """Fetch the heart rate from the monitoring system."""
    return 130  # Example heart rate

def get_blood_oxygen():
    """Fetch the blood oxygen level from the monitoring system."""
    return 95  # Example blood oxygen percentage

def get_resp_rate():
    """Fetch the blood oxygen level from the monitoring system."""
    return 50  # Example respiratory rate

# Safety thresholds (will be adjusted according to further research)
MAX_HEART_RATE = 180  # Beats per minute
HEART_RATE_CHANGE_THRESHOLD = 10  # Max acceptable rate of change per 5 sec
MIN_BLOOD_OXYGEN = 91  # Percentage
BLOOD_OXYGEN_CHANGE_THRESHOLD = 10  # Max acceptable rate of change per 5 sec
MIN_RESP_RATE = 30  # Breaths per minute
MAX_RESP_RATE = 60  # Breaths per minute

# Vital signs monitoring frequency in seconds
MONITORING_FREQUENCY = 5  # Will depend on concerning rates of change of vitals

# Global variables
running = False  # Initialize running as False

# Function to define positions for massage pattern with various pressure levels
def perform_massage_motion(pressure_level):
    """ 
    Execute one cycle of the massage motion.
    :param pressure_level: The pressure level to be applied (soft, medium, or hard).
    """
    # List of example positions gathered manually that create a triangular pattern
    if pressure_level == "soft":
        arm.setPosition([[3, 47], [4, 848], [5, 632], [6, 500]], 4000, wait=True)  # Position 1
        arm.setPosition([[3, 90], [4, 849], [5, 597], [6, 498]], 4000, wait=True)  # Position 2
        arm.setPosition([[3, 74], [4, 751], [5, 480], [6, 458]], 4000, wait=True)  # Position 3
        arm.setPosition([[3, 65], [4, 785], [5, 533], [6, 459]], 4000, wait=True)  # Position 4
        arm.setPosition([[3, 51], [4, 820], [5, 574], [6, 460]], 4000, wait=True)  # Position 5

    elif pressure_level == "medium":
        arm.setPosition([[3, 90], [4, 771], [5, 486], [6, 483]], 4000, wait=True)   # Position 1
        arm.setPosition([[3, 73], [4, 738], [5, 462], [6, 451]], 4000, wait=True)   # Position 2
        arm.setPosition([[3, 85], [4, 837], [5, 566], [6, 449]], 4000, wait=True)   # Position 3
        arm.setPosition([[3, 91], [4, 930], [5, 692], [6, 452]], 4000, wait=True)   # Position 4
        arm.setPosition([[3, 103], [4, 909], [5, 653], [6, 532]], 4000, wait=True)  # Position 5
        arm.setPosition([[3, 163], [4, 938], [5, 644], [6, 553]], 4000, wait=True)  # Position 6
        arm.setPosition([[3, 109], [4, 799], [5, 497], [6, 517]], 4000, wait=True)  # Position 7

    elif pressure_level == "hard":
        arm.setPosition([[3, 117], [4, 920], [5, 655], [6, 490]], 4000, wait=True)  # Position 1
        arm.setPosition([[3, 92], [4, 776], [5, 503], [6, 491]], 4000, wait=True)   # Position 2
        arm.setPosition([[3, 54], [4, 677], [5, 415], [6, 491]], 4000, wait=True)   # Position 3
        arm.setPosition([[3, 56], [4, 645], [5, 394], [6, 449]], 4000, wait=True)   # Position 4
        arm.setPosition([[3, 68], [4, 641], [5, 386], [6, 422]], 4000, wait=True)   # Position 5
        arm.setPosition([[3, 67], [4, 665], [5, 415], [6, 391]], 4000, wait=True)   # Position 6
        arm.setPosition([[3, 86], [4, 768], [5, 489], [6, 361]], 4000, wait=True)   # Position 7
        arm.setPosition([[3, 97], [4, 824], [5, 550], [6, 410]], 4000, wait=True)   # Position 8
        arm.setPosition([[3, 108], [4, 859], [5, 578], [6, 479]], 4000, wait=True)  # Position 9

# Function to determine initial pressure setting
def determine_initial_pressure(gestational_age, weight):
    """Determine the initial pressure setting based on patient data."""
    if gestational_age < 32 or weight < 1500:  # Units: gestational age = weeks; weight = grams
        return "soft"
    elif 32 <= gestational_age < 37 or 1500 <= weight < 2500:
        return "medium"
    else:
        return "hard"

# Function to monitor vitals and adjust pressure settings dynamically
def monitor_vitals_and_adjust():
    """Continuously monitor vitals and adjust pressure settings during massage."""
    global running, current_pressure
    previous_heart_rate = get_heart_rate()
    previous_blood_oxygen = get_blood_oxygen()
    start_time = time.time()

    while running:
        heart_rate = get_heart_rate()
        blood_oxygen = get_blood_oxygen()
        resp_rate = get_resp_rate()

        # Check heart rate threshold
        if heart_rate > MAX_HEART_RATE:
            print("Heart rate is too high! Stopping massage.")
            running = False
            break

        # Check blood oxygen percentage
        if blood_oxygen < MIN_BLOOD_OXYGEN:
            print("Blood oxygen is too low! Stopping massage.")
            running = False
            break

        # Check respiratory rate 
        if resp_rate < MIN_RESP_RATE or resp_rate > MAX_RESP_RATE:
            print("Respiratory rate is outside of acceptable range! Stopping massage.")
            running = False
            break

        # Check rate of change in heart rate and blood oxygen
        heart_rate_change = heart_rate - previous_heart_rate
        blood_oxygen_change = previous_blood_oxygen - blood_oxygen

        if abs(heart_rate_change) > HEART_RATE_CHANGE_THRESHOLD or blood_oxygen_change > BLOOD_OXYGEN_CHANGE_THRESHOLD:
            print("Vitals changing too quickly. Reducing pressure.")
            if current_pressure == "hard":
                current_pressure = "medium"
            elif current_pressure == "medium":
                current_pressure = "soft"

        previous_heart_rate = heart_rate
        previous_blood_oxygen = blood_oxygen

        # Stop massage after 10 minutes
        if time.time() - start_time > 10 * 60:
            print("10 minutes elapsed. Stopping massage.")
            running = False
            break

        time.sleep(MONITORING_FREQUENCY)  # Adjust vitals monitoring frequency dynamically

# Main massage execution function
def start_massage(gestational_age, weight):
    """Start the robotic arm massage based on patient data."""
    global running, current_pressure
    
    current_pressure = determine_initial_pressure(gestational_age, weight)
    running = True

    # Start monitoring vitals in a separate thread
    monitor_thread = threading.Thread(target=monitor_vitals_and_adjust)
    monitor_thread.start()

    try:
        while running:
            perform_massage_motion(current_pressure)  # Not sure how to make sure the robot arm goes back to position one before changing pressure levels
            print(f"Performing massage with pressure level: {current_pressure}")
    finally:
        running = False
        monitor_thread.join()
        print("Massage stopped.")

# Example patient case
if __name__ == "__main__":
    # Example patient data
    gestational_age = 34  # in weeks
    weight = 1800  # in grams

    start_massage(gestational_age, weight)
