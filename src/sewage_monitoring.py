import csv
import os
import random
import time
from datetime import datetime


# ============================================================
# SEWAGE MONITORING SYSTEM
# Python Simulation Prototype
# ============================================================

# Project folders
DATA_FOLDER = "data"
CSV_FILE = os.path.join(DATA_FOLDER, "sensor_data.csv")

# Number of readings
NUMBER_OF_READINGS = 20

# Time between readings
READING_INTERVAL = 1

# Safety thresholds
TEMPERATURE_LIMIT = 50.0
HUMIDITY_LIMIT = 90.0

CH4_LIMIT = 100.0
CO_LIMIT = 50.0
H2S_LIMIT = 10.0
NH3_LIMIT = 35.0


# ============================================================
# CREATE DATA FOLDER
# ============================================================

def create_data_folder():
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)


# ============================================================
# SENSOR SIMULATION
# ============================================================

def read_temperature():
    return round(random.uniform(25.0, 55.0), 2)


def read_humidity():
    return round(random.uniform(40.0, 100.0), 2)


def read_ch4():
    return round(random.uniform(5.0, 150.0), 2)


def read_co():
    return round(random.uniform(2.0, 80.0), 2)


def read_h2s():
    return round(random.uniform(0.5, 20.0), 2)


def read_nh3():
    return round(random.uniform(5.0, 60.0), 2)


# ============================================================
# READ ALL SENSORS
# ============================================================

def read_all_sensors():

    sensor_data = {
        "temperature": read_temperature(),
        "humidity": read_humidity(),
        "ch4": read_ch4(),
        "co": read_co(),
        "h2s": read_h2s(),
        "nh3": read_nh3()
    }

    return sensor_data


# ============================================================
# CHECK SENSOR SAFETY
# ============================================================

def check_safety(sensor_data):

    alerts = []

    temperature = sensor_data["temperature"]
    humidity = sensor_data["humidity"]
    ch4 = sensor_data["ch4"]
    co = sensor_data["co"]
    h2s = sensor_data["h2s"]
    nh3 = sensor_data["nh3"]

    # Temperature
    if temperature > TEMPERATURE_LIMIT:
        alerts.append(
            f"High temperature: {temperature} °C"
        )

    # Humidity
    if humidity > HUMIDITY_LIMIT:
        alerts.append(
            f"High humidity: {humidity} %"
        )

    # Methane
    if ch4 > CH4_LIMIT:
        alerts.append(
            f"High methane (CH4): {ch4} ppm"
        )

    # Carbon monoxide
    if co > CO_LIMIT:
        alerts.append(
            f"High carbon monoxide (CO): {co} ppm"
        )

    # Hydrogen sulfide
    if h2s > H2S_LIMIT:
        alerts.append(
            f"High hydrogen sulfide (H2S): {h2s} ppm"
        )

    # Ammonia
    if nh3 > NH3_LIMIT:
        alerts.append(
            f"High ammonia (NH3): {nh3} ppm"
        )

    # Determine system status
    if len(alerts) == 0:
        status = "SAFE"

    elif len(alerts) == 1:
        status = "WARNING"

    else:
        status = "DANGER"

    return status, alerts


# ============================================================
# CONTROL EXHAUST FAN AND BUZZER
# ============================================================

def control_devices(status):

    if status == "SAFE":

        fan = "OFF"
        buzzer = "OFF"

    elif status == "WARNING":

        fan = "ON"
        buzzer = "OFF"

    else:

        fan = "ON"
        buzzer = "ON"

    return fan, buzzer


# ============================================================
# DISPLAY SENSOR VALUES
# ============================================================

def display_sensor_data(sensor_data):

    print()
    print("=" * 60)
    print("             SEWAGE MONITORING SYSTEM")
    print("=" * 60)

    print(
        f"Temperature : {sensor_data['temperature']} °C"
    )

    print(
        f"Humidity    : {sensor_data['humidity']} %"
    )

    print(
        f"CH4         : {sensor_data['ch4']} ppm"
    )

    print(
        f"CO          : {sensor_data['co']} ppm"
    )

    print(
        f"H2S         : {sensor_data['h2s']} ppm"
    )

    print(
        f"NH3         : {sensor_data['nh3']} ppm"
    )

    print("-" * 60)


# ============================================================
# DISPLAY SYSTEM STATUS
# ============================================================

def display_status(status, fan, buzzer):

    print(f"System Status : {status}")
    print(f"Exhaust Fan   : {fan}")
    print(f"Buzzer        : {buzzer}")

    print("=" * 60)


# ============================================================
# DISPLAY ALERTS
# ============================================================

def display_alerts(status, alerts):

    if status == "SAFE":

        print("No abnormal condition detected.")

    else:

        print()
        print("!" * 60)

        if status == "WARNING":
            print("WARNING: ABNORMAL CONDITION DETECTED")

        else:
            print("DANGER: CRITICAL CONDITION DETECTED")

        print("!" * 60)

        for alert in alerts:
            print("ALERT:", alert)

        print("!" * 60)


# ============================================================
# SAVE SENSOR DATA
# ============================================================

def save_reading(sensor_data, status, fan, buzzer, alerts):

    file_exists = os.path.exists(CSV_FILE)

    with open(
        CSV_FILE,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        # Create column headings for a new file
        if not file_exists:

            writer.writerow([
                "Timestamp",
                "Temperature_C",
                "Humidity_Percent",
                "CH4_ppm",
                "CO_ppm",
                "H2S_ppm",
                "NH3_ppm",
                "System_Status",
                "Exhaust_Fan",
                "Buzzer",
                "Alerts"
            ])

        writer.writerow([
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),
            sensor_data["temperature"],
            sensor_data["humidity"],
            sensor_data["ch4"],
            sensor_data["co"],
            sensor_data["h2s"],
            sensor_data["nh3"],
            status,
            fan,
            buzzer,
            " | ".join(alerts)
            if alerts
            else "None"
        ])


# ============================================================
# DISPLAY FINAL SUMMARY
# ============================================================

def show_summary(
    total_readings,
    safe_count,
    warning_count,
    danger_count
):

    print()
    print("=" * 60)
    print("              MONITORING SUMMARY")
    print("=" * 60)

    print(f"Total Readings : {total_readings}")
    print(f"SAFE           : {safe_count}")
    print(f"WARNING        : {warning_count}")
    print(f"DANGER         : {danger_count}")

    print("-" * 60)

    print(
        f"Sensor data saved to: {CSV_FILE}"
    )

    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("       SMART SEWAGE MONITORING SYSTEM")
    print("              PYTHON PROTOTYPE")
    print("=" * 60)

    print()
    print("Initializing monitoring system...")

    # Create data folder
    create_data_folder()

    print("Data folder ready.")

    # Counters
    safe_count = 0
    warning_count = 0
    danger_count = 0

    print("Sensors initialized.")
    print("Monitoring started.")

    try:

        # Take multiple sensor readings
        for reading_number in range(
            1,
            NUMBER_OF_READINGS + 1
        ):

            print()
            print(
                f"Reading {reading_number}"
                f" / {NUMBER_OF_READINGS}"
            )

            # Read sensors
            sensor_data = read_all_sensors()

            # Display sensor values
            display_sensor_data(sensor_data)

            # Check safety
            status, alerts = check_safety(
                sensor_data
            )

            # Control devices
            fan, buzzer = control_devices(
                status
            )

            # Display status
            display_status(
                status,
                fan,
                buzzer
            )

            # Display alerts
            display_alerts(
                status,
                alerts
            )

            # Save data
            save_reading(
                sensor_data,
                status,
                fan,
                buzzer,
                alerts
            )

            # Update counters
            if status == "SAFE":

                safe_count += 1

            elif status == "WARNING":

                warning_count += 1

            else:

                danger_count += 1

            # Wait before next reading
            if reading_number < NUMBER_OF_READINGS:

                time.sleep(
                    READING_INTERVAL
                )

    except KeyboardInterrupt:

        print()
        print("Monitoring stopped by user.")

    finally:

        total_readings = (
            safe_count
            + warning_count
            + danger_count
        )

        show_summary(
            total_readings,
            safe_count,
            warning_count,
            danger_count
        )

        print()
        print("Program completed.")


# ============================================================
# START PROGRAM
# ============================================================

if __name__ == "__main__":
    main()