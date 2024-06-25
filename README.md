# Age Calculator with Leap Year Consideration

This Python program calculates a person's age in terms of months, weeks, and days. It takes into account the leap years within the person's lifespan to provide an accurate conversion.

## Features

- Calculates the number of leap years between the year of birth and the current year.
- Converts the age into months, weeks, and days, considering leap years.
- Simple command-line interface for input and output.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/ahsan-do/age-calculator.git
    ```

2. Navigate to the project directory:

    ```sh
    cd age-calculator
    ```

## Usage

1. Run the program:

    ```sh
    python age_calculator.py
    ```

2. Enter your age when prompted.

3. The program will output your age in months, weeks, and days, taking into account the number of leap years.

## Example

```sh
$ python age_calculator.py
Enter your age: 25
Your age in months: 304
Your age in weeks: 1308
Your age in days: 9166
```
## Code Explanation
**Functions**
**is_leap_year(year):** Checks if a given year is a leap year.
```sh
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

**count_leap_years(start_year, end_year):** Counts the number of leap years between start_year and end_year inclusive.
```sh
def count_leap_years(start_year, end_year):
    return sum(1 for year in range(start_year, end_year + 1) if is_leap_year(year))
```

**age_to_months_weeks_days(age, leap_years_count):** Converts age in years to months, weeks, and days, including leap years.
```sh
def age_to_months_weeks_days(age, leap_years_count):
    days_in_regular_year = 365
    days_in_leap_year = 366
    days_in_years = (age - leap_years_count) * days_in_regular_year + leap_years_count * days_in_leap_year
    
    months = days_in_years // 30
    weeks = days_in_years // 7
    days = days_in_years
    
    return months, weeks, days
```

**Main Function**
**main():** Handles input, calculates year of birth, counts leap years, and converts age to months, weeks, and days.
```sh
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
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or comments, please reach out to [your-email@example.com].

