# ymdhms_to_jd.py
#
# Usage: python3 ymdhms_to_jd.py year month day hour minute second
# This script converts the given date and time into a fractional Julian Date (JD).
# The Julian Date represents the continuous count of days since January 1, 4713 BCE at 12:00 UT.
#
# Parameters:
# year: Year of the date (integer)
# month: Month of the date (integer, 1 to 12)
# day: Day of the month (integer)
# hour: Hour of the day (integer, 0 to 23)
# minute: Minute of the hour (integer, 0 to 59)
# second: Second of the minute (float, can have decimal portion)
#
# Output:
# Prints the fractional Julian Date corresponding to the input date and time.
#
# Written by: Jeren Browder
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys  # for argument parsing

def ymdhms_to_julian_date(year, month, day, hour, minute, second):
    """
    Convert a calendar date and time (year, month, day, hour, minute, second)
    to the corresponding Julian Date (JD).
    
    Args:
        year (int): Year of the date.
        month (int): Month of the date (1 = January, ..., 12 = December).
        day (int): Day of the month.
        hour (int): Hour of the day (0-23).
        minute (int): Minute of the hour (0-59).
        second (float): Seconds of the minute (can have a decimal portion).
        
    Returns:
        float: The Julian Date corresponding to the given date and time.
    """
    # Adjust for months of January and February
    if month <= 2:
        year -= 1
        month += 12

    # Calculate the integer part of the Julian Date
    A = year // 100
    B = 2 - A + A // 4

    jd_int = int(365.25 * (year + 4716)) + int(30.6001 * (month + 1)) + day + B - 1524.5

    # Convert the time portion (hour, minute, second) to fractional days
    frac_day = (hour + minute / 60.0 + second / 3600.0) / 24.0

    # The total Julian Date is the sum of the integer and fractional parts
    jd_frac = jd_int + frac_day

    return jd_frac

def main():
    # Check that the correct number of arguments were passed
    if len(sys.argv) != 7:
        print("Usage: python3 ymdhms_to_jd.py year month day hour minute second")
        sys.exit(1)

    # Parse the input arguments
    year = int(sys.argv[1])
    month = int(sys.argv[2])
    day = int(sys.argv[3])
    hour = int(sys.argv[4])
    minute = int(sys.argv[5])
    second = float(sys.argv[6])  # Allow the second to have a decimal portion

    # Perform the conversion to Julian Date
    jd_frac = ymdhms_to_julian_date(year, month, day, hour, minute, second)

    # Output the result
    print(jd_frac)

if __name__ == "__main__":
    main()