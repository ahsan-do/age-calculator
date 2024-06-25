from datetime import datetime

def is_leap_year(year):
    """Check if a given year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def count_leap_years(start_year, end_year):
    """Count the number of leap years between start_year and end_year inclusive."""
    return sum(1 for year in range(start_year, end_year + 1) if is_leap_year(year))

def age_to_months_weeks_days(age, leap_years_count):
    """Convert age in years to months, weeks, and days, including leap years."""
    days_in_regular_year = 365
    days_in_leap_year = 366
    days_in_years = (age - leap_years_count) * days_in_regular_year + leap_years_count * days_in_leap_year
    
    months = days_in_years // 30
    weeks = days_in_years // 7
    days = days_in_years
    
    return months, weeks, days

def main():
    # Get the current year
    current_year = datetime.now().year
    
    # Take the person's age as input
    age = int(input("Enter your age: "))
    
    # Calculate the year of birth
    year_of_birth = current_year - age
    
    # Count the number of leap years from year_of_birth to current_year
    leap_years_count = count_leap_years(year_of_birth, current_year)
    
    # Convert the age to months, weeks, and days
    months, weeks, days = age_to_months_weeks_days(age, leap_years_count)
    
    print(f"Your age in months: {months}")
    print(f"Your age in weeks: {weeks}")
    print(f"Your age in days: {days}")

if __name__ == "__main__":
    main()
