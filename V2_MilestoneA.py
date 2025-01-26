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

# Safety thresholds (will be adjusted according to further research)
MAX_HEART_RATE = 180  # Beats per minute
HEART_RATE_CHANGE_THRESHOLD = 10  # Max acceptable rate of change per 5 sec
MIN_BLOOD_OXYGEN = 91  # Percentage
BLOOD_OXYGEN_CHANGE_THRESHOLD = 10  # Max acceptable rate of change per 5 sec

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
        arm.setPosition([[3, 156], [4, 863], [5, 580], [6, 548]], 4000, wait=True)  # Positions to be updated in Milestone B
        arm.setPosition([[3, 217], [4, 872], [5, 542], [6, 526]], 4000, wait=True)  # Position 2
        arm.setPosition([[3, 212], [4, 820], [5, 480], [6, 502]], 4000, wait=True)  # Position 3
        arm.setPosition([[3, 200], [4, 797], [5, 457], [6, 469]], 4000, wait=True)  # Position 4
        arm.setPosition([[3, 166], [4, 810], [5, 509], [6, 468]], 4000, wait=True)  # Position 5
        arm.setPosition([[3, 129], [4, 810], [5, 550], [6, 468]], 4000, wait=True)  # Position 6
        arm.setPosition([[3, 107], [4, 820], [5, 578], [6, 468]], 4000, wait=True)  # Position 7
        arm.setPosition([[3, 75], [4, 836], [5, 606], [6, 468]], 4000, wait=True)   # Position 8
        arm.setPosition([[3, 66], [4, 846], [5, 622], [6, 456]], 4000, wait=True)   # Position 9
        arm.setPosition([[3, 96], [4, 918], [5, 655], [6, 440]], 4000, wait=True)   # Position 10
        arm.setPosition([[3, 96], [4, 904], [5, 667], [6, 474]], 4000, wait=True)   # Position 11
        arm.setPosition([[3, 132], [4, 904], [5, 659], [6, 529]], 4000, wait=True)  # Position 12
        arm.setPosition([[3, 175], [4, 905], [5, 622], [6, 552]], 4000, wait=True)  # Position 13

    elif pressure_level == "medium":
        arm.setPosition([[3, 156], [4, 863], [5, 580], [6, 548]], 4000, wait=True)  # Position 1
        arm.setPosition([[3, 217], [4, 872], [5, 542], [6, 526]], 4000, wait=True)  # Position 2
        arm.setPosition([[3, 212], [4, 820], [5, 480], [6, 502]], 4000, wait=True)  # Position 3
        arm.setPosition([[3, 200], [4, 797], [5, 457], [6, 469]], 4000, wait=True)  # Position 4
        arm.setPosition([[3, 166], [4, 810], [5, 509], [6, 468]], 4000, wait=True)  # Position 5
        arm.setPosition([[3, 129], [4, 810], [5, 550], [6, 468]], 4000, wait=True)  # Position 6
        arm.setPosition([[3, 107], [4, 820], [5, 578], [6, 468]], 4000, wait=True)  # Position 7
        arm.setPosition([[3, 75], [4, 836], [5, 606], [6, 468]], 4000, wait=True)   # Position 8
        arm.setPosition([[3, 66], [4, 846], [5, 622], [6, 456]], 4000, wait=True)   # Position 9
        arm.setPosition([[3, 96], [4, 918], [5, 655], [6, 440]], 4000, wait=True)   # Position 10
        arm.setPosition([[3, 96], [4, 904], [5, 667], [6, 474]], 4000, wait=True)   # Position 11
        arm.setPosition([[3, 132], [4, 904], [5, 659], [6, 529]], 4000, wait=True)  # Position 12
        arm.setPosition([[3, 175], [4, 905], [5, 622], [6, 552]], 4000, wait=True)  # Position 13

    elif pressure_level == "hard":
        arm.setPosition([[3, 156], [4, 863], [5, 580], [6, 548]], 4000, wait=True)  # Positions to be updated in Milestone B
        arm.setPosition([[3, 217], [4, 872], [5, 542], [6, 526]], 4000, wait=True)  # Position 2
        arm.setPosition([[3, 212], [4, 820], [5, 480], [6, 502]], 4000, wait=True)  # Position 3
        arm.setPosition([[3, 200], [4, 797], [5, 457], [6, 469]], 4000, wait=True)  # Position 4
        arm.setPosition([[3, 166], [4, 810], [5, 509], [6, 468]], 4000, wait=True)  # Position 5
        arm.setPosition([[3, 129], [4, 810], [5, 550], [6, 468]], 4000, wait=True)  # Position 6
        arm.setPosition([[3, 107], [4, 820], [5, 578], [6, 468]], 4000, wait=True)  # Position 7
        arm.setPosition([[3, 75], [4, 836], [5, 606], [6, 468]], 4000, wait=True)   # Position 8
        arm.setPosition([[3, 66], [4, 846], [5, 622], [6, 456]], 4000, wait=True)   # Position 9
        arm.setPosition([[3, 96], [4, 918], [5, 655], [6, 440]], 4000, wait=True)   # Position 10
        arm.setPosition([[3, 96], [4, 904], [5, 667], [6, 474]], 4000, wait=True)   # Position 11
        arm.setPosition([[3, 132], [4, 904], [5, 659], [6, 529]], 4000, wait=True)  # Position 12
        arm.setPosition([[3, 175], [4, 905], [5, 622], [6, 552]], 4000, wait=True)  # Position 13

# Function to determine initial pressure setting
def determine_initial_pressure(gestational_age, weight, length_of_stay):
    """Determine the initial pressure setting based on patient data."""
    if gestational_age < 32 or weight < 1500 or length_of_stay < 7:  # Units: gestational age = weeks; weight = grams; lenght of stay = days
        return "soft"
    elif 32 <= gestational_age < 37 or 1500 <= weight < 2500 or 7 <= length_of_stay < 14:
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
def start_massage(gestational_age, weight, length_of_stay):
    """Start the robotic arm massage based on patient data."""
    global running, current_pressure
    
    current_pressure = determine_initial_pressure(gestational_age, weight, length_of_stay)
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
    length_of_stay = 10  # in days

    start_massage(gestational_age, weight, length_of_stay)