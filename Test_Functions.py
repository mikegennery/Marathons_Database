# Michael Gennery
# Test Functions
# June 2020
# Version 2


from MJG_Functions import *

# VARIABLES
    
nums = {'0' : '00','1' : '01','2' : '02','3' : '03','4' : '04','5' : '05','6' : '06','7' : '07','8' : '08','9' : '09'}

date_string = ''

date_difference = 0

prev_date_num = 0

calender = {
    0 : 0,
    1 : 31, # January
    2 : 28, # February
    3 : 31, # March
    4 : 30, # April
    5 : 31, # May
    6 : 30, # June
    7 : 31, # July
    8 : 31, # August
    9 : 30, # September
    10 : 31, # October
    11 : 30, # November
    12 : 31  # December
    }

test_year = 0

months = {
    '1' : 'JAN','2' : 'FEB','3' : 'MAR','4' : 'APR','5' : 'MAY','6' : 'JUN','7' : 'JUL','8' : 'AUG','9' : 'SEP','10' : 'OCT','11' : 'NOV','12' : 'DEC'
    }

day_child = {
        'Monday'    : 'Monday\'s Child is fair of face',
        'Tuesday'   : 'Tuesday\'s Child is full of grace',
        'Wednesday' : 'Wednesday\'s Child is full of woe',
        'Thursday'  : 'Thursday\'s Child has far to go',
        'Friday'    : 'Friday\'s Child is loving and giving',
        'Saturday'  : 'Saturday\'s Child works hard for a living',
        'Sunday'    : 'But the child who is born on the Sabbath Day Is bonny and blithe, merry and gay'
        }

weekday = ''

# Flags

valid_input = False

quit_prog_option = ''
quit_prog = False

# TEST FUNCTIONS

print('\nMichael Gennery')
print('Functions')
print('June 2020')

print('\nTest Args & Kwargs\n11th November 2000\n')

print(call_date_to_num(Day=1,Month=11,Year=2000))
print(call_date_to_num(month=11,year=2000,day=1))
print(call_date_to_num(YYYY=2000, DD=1, MM=11))
print(call_date_to_num(y=2000, M=11, D=1))
print(call_date_to_num(m=11,y=2000, d=1))
print(call_date_to_num(dd=1,mm=11,yyyy=2000))
print(call_date_to_num(2000,11,1))

print('\nTest String')

while date_string != '99':

    date_string = input('\nEnter a date in the following format (YYYYMMDD) (99 to quit): ')

    if date_string == '99':
        break

    date_num = date_to_num(date_string)

    if date_num != 0:
        print('\nDate Number: ',date_num)
        date_difference = date_num - prev_date_num  # Calculate the difference between this date number and the previous date
        print('Date Difference: ',date_difference)
        prev_date_num = date_num                    # Copy this date number to the previous date variable for the next loop
        weekday = day_of_week(date_num)
        print(weekday,' - ',day_child[weekday])

print('\nTest Tuple or List')
date_string = '00'

while date_string != '99':

    date_year = input('\nEnter a year in the following format YYYY (99 to quit): ')
    if date_year == '99':
        date_string == '99'
        break

    date_month = input('\nEnter a month in the following format MM (99 to quit): ')
    if date_month == '99':
        date_string == '99'
        break

    date_day = input('\nEnter a day in the following format DD (99 to quit): ')
    if date_day == '99':
        date_string == '99'
        break

    date_num = date_to_num([date_year,date_month,date_day])

    if date_num != 0:
        print('\nDate Number: ',date_num)
        date_difference = date_num - prev_date_num  # Calculate the difference between this date number and the previous date
        print('Date Difference: ',date_difference)
        prev_date_num = date_num                    # Copy this date number to the previous date variable for the next loop
        weekday = day_of_week(date_num)
        print(weekday,' - ',day_child[weekday])


print('\nDatetime Object')
date_string = '00'

while date_string != '99':

    date_year = input('\nEnter a year in the following format YYYY (99 to quit): ')
    if date_year == '99':
        date_string == '99'
        break

    date_month = input('\nEnter a month in the following format MM (99 to quit): ')
    if date_month == '99':
        date_string == '99'
        break

    date_day = input('\nEnter a day in the following format DD (99 to quit): ')
    if date_day == '99':
        date_string == '99'
        break

    date_num = date_to_num([date_year,date_month,date_day])
    datetime_object = date_to_datetime([date_year,date_month,date_day])

    if date_num != 0:
        print('\nDate Number: ',date_num)
        date_difference = date_num - prev_date_num  # Calculate the difference between this date number and the previous date
        print('Date Difference: ',date_difference)
        prev_date_num = date_num                    # Copy this date number to the previous date variable for the next loop
        weekday = day_of_week(date_num)
        print(weekday,' - ',day_child[weekday])
        print(datetime_object)
        
print('\nDISPLAY CALENDER')

valid_input = False # Reset the error flag

while not valid_input:
    enter_test_year = input('\nEnter a year (YYYY) or (99 to quit): ')
    try:
        test_year = int(enter_test_year)
    except ValueError:
        valid_input = False
        print('Invalid Input!')
        test_year =  0
    except TypeError:
        valid_input = False
        print('Invalid Input!')
        test_year = 0
    if (test_year < 1900 or test_year > 2099) and test_year != 99:
        valid_input = False
        print('Year must be between 1900 and 2099!')
    else:
        valid_input = True

if test_year != 99:
    
    print('\nCALENDER FOR YEAR',test_year)
    print('\nDATE\t\t\t DATE STRING\t DATE NUMBER\t WEEKDAY\t DATE TEXT')
    print('====================================================================================================================================================')

    for test_month in range(1,13):
        for test_day in range(1,32):

            test_year_text = str(test_year)

            if ((test_year / 4) - (test_year // 4)) == 0: # Test for a leap year
                calender[2] = 29 # February has 29 days in a leap year
            else:
                calender[2] = 28
                
            if test_day <= calender[test_month]: # Only do this loop if the day number is within range for the month 
            
                if test_month < 10:
                    test_month_text = nums[str(test_month)]
                else:
                    test_month_text = str(test_month)
                if test_day < 10:
                    test_day_text = nums[str(test_day)]
                else:
                    test_day_text = str(test_day)
            
                test_date = test_year_text + test_month_text + test_day_text

                if test_day < 10:
                    test_day_text = nums[str(test_day)]
                else:
                    test_day_text = str(test_day)

                if test_day == 1:
                    print('')

                print(test_day_text,'/',months[str(test_month)],'/',test_year,'\t',test_date,'\t',date_to_num(test_date),'\t\t',day_of_week(test_date),'\t',(date_to_text(test_date)[4]),'\t',date_to_datetime(test_date))
