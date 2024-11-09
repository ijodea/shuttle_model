import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def time_to_minutes(time_str):
    """Convert time string (HH:MM) to minutes since midnight"""
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def minutes_to_time(minutes):
    """Convert minutes since midnight to time string (HH:MM)"""
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02d}:{mins:02d}"

def generate_arrival_data(schedule_path, num_weeks=4):
    """
    Generate sample arrival data based on the schedule
    with realistic variations in arrival times
    """
    # Read the schedule
    schedule_df = pd.read_csv(schedule_path)
    
    # Initialize empty lists for our arrival data
    arrival_times = []
    days = []
    depart_ats = []
    
    # Process each day's data
    for day in ['MON', 'TUE', 'WED', 'THU', 'FRI']:
        # Get school departure times
        sch_times = schedule_df[f'{day}_SCHOOL_DEPART'].tolist()
        sta_times = schedule_df[f'{day}_STATION_DEPART'].tolist()
        
        # Generate data for each week
        for week in range(num_weeks):
            # Process school departures
            for scheduled_time in sch_times:
                # Convert to minutes for easier calculation
                scheduled_mins = time_to_minutes(scheduled_time)
                
                # Add 15 minutes for expected travel time
                expected_arrival = scheduled_mins + 15
                
                # Add random variation
                # Morning rush hours (7:30-9:30) have more variation
                if 450 <= scheduled_mins <= 570:  # 7:30-9:30
                    variation = np.random.normal(2, 3)  # Mean delay of 2 mins, SD of 3 mins
                else:
                    variation = np.random.normal(0, 2)  # Mean delay of 0 mins, SD of 2 mins
                
                actual_arrival = expected_arrival + variation
                
                # Convert back to time string
                arrival_time = minutes_to_time(int(actual_arrival))
                
                arrival_times.append(arrival_time)
                days.append(day)
                depart_ats.append('SCH')
            
            # Process station departures
            for scheduled_time in sta_times:
                scheduled_mins = time_to_minutes(scheduled_time)
                expected_arrival = scheduled_mins + 15
                
                # Station departures typically have less variation
                variation = np.random.normal(0, 1.5)
                actual_arrival = expected_arrival + variation
                
                arrival_time = minutes_to_time(int(actual_arrival))
                
                arrival_times.append(arrival_time)
                days.append(day)
                depart_ats.append('STA')
    
    # Create DataFrame
    arrival_df = pd.DataFrame({
        'ARRIVAL_TIME': arrival_times,
        'DAY': days,
        'DEPART_AT': depart_ats
    })
    
    # Sort by day and arrival time
    arrival_df = arrival_df.sort_values(['DAY', 'ARRIVAL_TIME'])
    
    return arrival_df

# Generate the data
arrival_data = generate_arrival_data('gStation2.csv', num_weeks=4)

# Save to CSV
arrival_data.to_csv('arrival_data.csv', index=False)

# Display first few rows and some statistics
print("\nFirst few rows of generated data:")
print(arrival_data.head(10))

print("\nSummary statistics:")
print(f"Total number of records: {len(arrival_data)}")
print("\nRecords per day:")
print(arrival_data['DAY'].value_counts())
print("\nRecords per departure location:")
print(arrival_data['DEPART_AT'].value_counts())
