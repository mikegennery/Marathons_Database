# Marathons Database
# Michael Gennery
# September 2020
# Version 2

from csv import reader

from MJG_Functions import *


###

### FUNCTIONS

###



# Display Statistics Dictionary

def stat_display(stat_dict):
    tab_text4 = '\t'
    for name in stat_dict:
        temp_name = str(name)
        temp_length = len(temp_name)
        if temp_length > 20:
            tab_text4 = '\t'
        elif (temp_length > 13 and len(temp_name) <= 20):
            tab_text4 = '\t\t'
        elif (temp_length > 5 and len(temp_name) <= 13):
            tab_text4 = '\t\t\t'
        elif (temp_length > 3 and len(temp_name) <= 5):
            tab_text4 = '\t\t\t\t'
        elif temp_length <= 3:
            tab_text4 = '\t'

        print('\t',name,tab_text4,stat_dict[name])



# Move filtered data from main_table into display_table

def filter_the_table(
    main_table = [],    # This is where the data from the CSV file will be read into
    from_date_num = 1,       # Filter Codes - Date
    to_date_num = 73049,
    from_miles = 0,     # Filter Codes - Distance
    to_miles = 99,
    from_total_secs = 0,     # Filter Codes - Time
    to_total_secs = 86400,
    ):

    # VARIABLES LIST
    
    # This is a list of the displayed data
        # each_run[0] - Race Number
        # each_run[1] - Date - Day
        # each_run[2] - Date - Month
        # each_run[3] - Date - Year
        # each_run[4] - Race Name
        # each_run[5] - City
        # each_run[6] - Country
        # each_run[7] - Distance in Miles
        # each_run[8] - Time - Hours
        # each_run[9] - Time - Minutes
        # each_run[10] - Time - Seconds
        # each_run[11] - Date Number
        # each_run[12] - Time in seconds

    display_table = []

    # FILTER CODE - Used to determine if the run will be displayed i.e. added to the display table
    
    filter_code = False
    
    for each_run in main_table:

        filter_code = False # Reset The filter code


        # FILTER DATE

        if each_run[11] >= from_date_num and each_run[11] <= to_date_num:

            filter_code = True

                
        # FILTER DISTANCE

        if filter_code is True: # Perform the remaining filter checks if the run falls between the sepcified dates
            if (each_run[7] >= from_miles and each_run[7] <= to_miles):

                # FILTER TIME

                if (each_run[12] >= from_total_secs) and (each_run[12] <= to_total_secs):
                    
                    filter_code = True # Display the run if it matches the selected criteria for distance
                    
                else:
                    filter_code = False
            else:
                filter_code = False
        
            # Display the run if it matches the selected criteria
        
        if filter_code is True:
            display_table.append(each_run)

    return(display_table)




# Display the filtered table

def display_the_table(display_table):

    print('\nMARATHONS FOR MICHAEL GENNERY\n')
    print('\nRACE NO\t DATE\t\t\t NAME\t\t\t\t\t CITY\t\t\t COUNTRY\t\t DISTANCE\t TIME')
    print('\n\t DD / MMM / YYYY\t\t\t\t\t\t\t\t\t\t\t\t MILES\t\t H : MM : SS')
    print('====================================================================================================================================================')

    # VARIABLE LIST
    
    # This is a list of the displayed data
        # each_run[0] - Race Number
        # each_run[1] - Date - Day
        # each_run[2] - Date - Month
        # each_run[3] - Date - Year
        # each_run[4] - Race Name
        # each_run[5] - City
        # each_run[6] - Country
        # each_run[7] - Distance in Miles
        # each_run[8] - Time - Hours
        # each_run[9] - Time - Minutes
        # each_run[10] - Time - Seconds
        # each_run[11] - Date Number
        # each_run[12] - Time in seconds


    # STATISTICS
    
    from_total_secs = 0
    to_total_secs = 0
    run_total_secs = 0

    total_num_cities = {}
    total_num_countries = {}
    total_num_distance = {}

    # Time statistics

    lowest_time = 36000
    highest_time = 0
    run_count = 0
    total_time = 0
    average_time = 0

    # Displaying Statistics

    print_lowest_time = ()
    print_highest_time = ()
    print_average_time = ()
    print_total_time = ()

    # Aligning Text

    tab_text = ''
    tab_text2 = ''
    tab_text3 = ''
    tab_text4 = ''

    # Displaying dates and times

    display_day = ''
    display_month = ''
    display_hour = ''
    display_mins = ''
    display_secs = ''

    months = {
        '1' : 'JAN','2' : 'FEB','3' : 'MAR','4' : 'APR','5' : 'MAY','6' : 'JUN','7' : 'JUL','8' : 'AUG','9' : 'SEP','10' : 'OCT','11' : 'NOV','12' : 'DEC'
        }

    nums = {'0' : '00','1' : '01','2' : '02','3' : '03','4' : '04','5' : '05','6' : '06','7' : '07','8' : '08','9' : '09'}

    for each_run in display_table:

    # The number of tabs depends on the length of the field to enable alignment of text

    # Align Location
    
        if len(each_run[4]) >= 23:
            tab_text = '\t\t'
        elif len(each_run[4]) == 22:
            tab_text = '\t\t'
        elif len(each_run[4]) == 21:
            tab_text = '\t\t\t'
        elif len(each_run[4]) >= 17 and len(each_run[4]) < 21:
            tab_text = '\t\t\t'
        elif len(each_run[4]) >= 14 and len(each_run[4]) < 17:
            tab_text = '\t\t\t'
        elif len(each_run[4]) >= 11 and len(each_run[4]) < 14:
            tab_text = '\t\t\t\t'
        elif len(each_run[4]) >= 7 and len(each_run[4]) < 11:
            tab_text = '\t\t\t\t\t'
        elif len(each_run[4]) <= 7:
            tab_text = '\t\t\t\t\t\t'
        else:
            tab_text = '\t\t'

    # Align Country
    
        if len(each_run[5]) >= 14:
            tab_text2 = '\t'
        elif len(each_run[5]) >=8 and len(each_run[5]) < 14:
            tab_text2 = '\t\t'
        elif len(each_run[5]) >5 and len(each_run[5]) < 8:
            tab_text2 = '\t\t'
        elif len(each_run[5]) == 5:
            tab_text2 = '\t\t\t'
        elif len(each_run[5]) < 5:
            tab_text2 = '\t\t\t'
        else:
            tab_text2 = '\t\t'

    # Align Distance

        if len(each_run[6]) >= 14:
            tab_text3 = '\t'
        elif len(each_run[6]) >=10 and len(each_run[6]) < 14:
            tab_text3 = '\t\t'        
        elif len(each_run[6]) >=6 and len(each_run[6]) < 10:
            tab_text3 = '\t\t'
        elif len(each_run[6]) >=1 and len(each_run[6]) < 5:
            tab_text3 = '\t\t\t'
        else:
            tab_text3 = '\t\t\t'

    # This is a list of the displayed data
        # each_run[0] - Race Number
        # each_run[1] - Day
        # each_run[2] - Month
        # each_run[3] - Year
        # each_run[4] - Race Name
        # each_run[5] - City
        # each_run[6] - Country
        # each_run[7] - Distance in Miles
        # each_run[8] - Hours
        # each_run[9] - Minutes
        # each_run[10] - Seconds
        # each_run[12] - Time in seconds
    
    # Display Date and time correctly

        if each_run[1] < 10:
            display_day = nums[str(each_run[1])]
        else:
            display_day = str(each_run[1])

        temp_month = str(each_run[2])
    
        display_month = months[temp_month]

        if each_run[9] < 10:
            display_mins = nums[str(each_run[9])]
        else:
            display_mins = str(each_run[9])

        if each_run[10] < 10:
            display_secs = nums[str(each_run[10])]
        else:
            display_secs = str(each_run[10])

        # CALCULATE THE STATISTICS

        # Calculate the time of the run
                
        run_total_secs = calc_secs(each_run[8], each_run[9], each_run[10])

        # Update Time Statistics

        if (run_total_secs < lowest_time):
            lowest_time = run_total_secs
        if (run_total_secs > highest_time):
            highest_time = run_total_secs
        run_count += 1
        total_time += run_total_secs
            
        # each_run[5] - City

        if each_run[5] in total_num_cities:
            total_num_cities[each_run[5]] += 1
        else:
            total_num_cities[each_run[5]] = 1

        # each_run[6] - Country

        if each_run[6] in total_num_countries:
            total_num_countries[each_run[6]] += 1
        else:
            total_num_countries[each_run[6]] = 1

        # each_run[7] - Distance in Miles

        if each_run[7] in total_num_distance:
            total_num_distance[each_run[7]] += 1
        else:
            total_num_distance[each_run[7]] = 1
            
        average_time = (total_time / run_count)

        # Print the run from the display table
        
        print(each_run[0],'\t',display_day,'/',display_month,'/',each_run[3],'\t',each_run[4],tab_text,each_run[5],tab_text2,each_run[6],tab_text3,each_run[7],'\t\t',each_run[8],':',display_mins,':',display_secs)
              
    # DSIPLAY THE STATISTICS

    if run_count > 0:
        
        void = input('\nPRESS ENTER TO DISPLAY STATISTICS')

        print('\nSTATISTICS')
        print('\nCITIES\t\t\t\t\t QUANTITY')
        stat_display(total_num_cities)
        print('\nCOUNTRIES\t\t\t\t QUANTITY')
        stat_display(total_num_countries)
        print('\nDISTANCES')
        print('\t MILES\t QUANTITY')
        stat_display(total_num_distance)
        print('\nTOTAL NUMBER OF RUNS: ',run_count)
        print('\n\t\t HH : MM : SS')

        print_lowest_time = calc_hours_mins_secs(lowest_time)
        print_highest_time = calc_hours_mins_secs(highest_time)
        print_average_time = calc_hours_mins_secs(average_time)
        print_total_time = calc_hours_mins_secs(total_time)

        print('\nLOWEST TIME: \t',print_lowest_time[0],':',print_lowest_time[1],':',print_lowest_time[2])
        print('HIGHEST TIME: \t',print_highest_time[0],':',print_highest_time[1],':',print_highest_time[2])
        print('AVERAGE TIME: \t',print_average_time[0],':',print_average_time[1],':',print_average_time[2])
        print('TOTAL TIME: \t',print_total_time[0],':',print_total_time[1],':',print_total_time[2])

    else:

        print('\nNo runs to display')


###

### MAIN CODE

###



# Read data about marathons from a CSV file into a table

marathons_file = open('Marathons.csv')
marathons_db = reader(marathons_file)
marathons_table = list(marathons_db)

# VARIABLES LIST

display_option = '' # Dose the user wish to display the whole table?
filter_option = ''  # Does the user wish to filter the table?
sort_option = ''    # Does the user wish to sort the table?
sort_code = 0       # Which field does the user which to sort the table be?
sort_order = ''     # Ascending or Descending?

display_table = []  # This is the table used to display the filtered data which will be wiped with each run

# Filter codes

from_day = 1       # Filter Codes - Date
from_month = 1
from_year = 1900
from_date_num = 0

to_day = 31
to_month = 12
to_year = 9999
to_date_num = 73049

from_miles = 0      # Filter Codes - Distance
to_miles = 99

from_hours = 0      # Filter Codes - Time
from_mins = 0
from_secs = 0
to_hours = 99
to_mins = 59
to_secs = 59

# Calender for validating entered dates

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

# Flags

valid_input = False
quit_prog_option = ''
quit_prog = False

# Move data from marathons_table into a simpler and tidier format in main_table

main_table = []

for each_run in marathons_table:

    # This is a list of the displayed data
        # each_run[0] - Race Number
        # each_run[1] - Day
        # each_run[2] - Month
        # each_run[3] - Year
        # each_run[4] - Race Name
        # each_run[5] - City
        # each_run[6] - Country
        # each_run[7] - Distance in Miles
        # each_run[8] - Hours
        # each_run[9] - Minutes
        # each_run[10] - Seconds
        # each_run[11] - Date Number
        # each_run[12] - Time in seconds

    main_table_run = []
    main_table_run.append(int(each_run[0]))        # Index Number
    
    temp_date = each_run[1]                         # Extract the Date
    temp_day = temp_date[0:2]                           # Day
    temp_month = temp_date[3:5]                         # Month
    temp_year = temp_date[6:10]                         # Year
    main_table_run.append(int(temp_day))           # Append the Date
    main_table_run.append(int(temp_month))    
    main_table_run.append(int(temp_year))

    temp_date_num = date_to_num((temp_year,temp_month,temp_day)) # Date Number
    
    main_table_run.append(each_run[2])        # Run Nume
    
    main_table_run.append(each_run[3])        # Location
    main_table_run.append(each_run[5])        # Country

    temp_distance = int(each_run[6])
    main_table_run.append(temp_distance)        # Distance (Miles)

    temp_time = each_run[10]                        # Extract and append
    temp_time = temp_time[11:]                      # the time
    temp_hour = temp_time[0:2]                      # Extract hours
    temp_mins = temp_time[3:5]                      # Extract Minutes
    temp_secs = temp_time[6:9]                      # Extract Seconds

    try:
        main_table_run.append(int(temp_hour))           # Append Hours
        main_table_run.append(int(temp_mins))           # Append Minutes
        main_table_run.append(int(temp_secs))           # Append Seconds
    except ValueError:
        main_table_run.append(0)           # Append 0
        main_table_run.append(0)           # if no time
        main_table_run.append(0)           # is recorded
        temp_hour = 0
        temp_mins = 0
        temp_secs = 0
    
    main_table_run.append(temp_date_num) # Append Date Number

    temp_total_secs = calc_secs(int(temp_hour),int(temp_mins),int(temp_secs)) # Append Time in seconds
    main_table_run.append(temp_total_secs)
    
    main_table.append(main_table_run)   # Append data to main table

    


print('\nMARATHONS FOR MICHAEL GENNERY')
print('July 2020') 

while not quit_prog:

    # Sort Options

    # Does the user wish to sort the table?

    valid_input = False # Reset the error flag
        
    while not valid_input:
        sort_option = input('\nDo you wish to sort the marathons database? (Y = YES, N = NO): ')
        if sort_option == 'Y' or sort_option == 'y' or sort_option == 'N' or sort_option == 'n':
            valid_input = True
        else:
            valid_input = False
            print('You Must Enter Y or N!')

    valid_input = False # Reset the error flag

    if sort_option == 'Y' or sort_option == 'y':

        # NOTE: Sort facility under construction - NOT AVAILABLE!

        print('\nNOTE: Sort facility under construction - NOT AVAILABLE!')

        """

    # Which field does the user which to sort the table on?
    
        while not valid_input:
            sort_code = input('\nEnter sort code (1 = DATE, 2 = NAME, 3 = CITY, 4 = COUNTRY, 5 = DISTANCE, 6 = TIME): ')
            if int(sort_code) < 1 or int(sort_code) > 6:
                print('You Must Enter an option between 1 and 6!')
                valid_input = False
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        # Ascending or Descending?
        
        while not valid_input:
            sort_order = input('(A = Ascending, D = Descending): ')
            if sort_order == 'A' or sort_order == 'a' or sort_order == 'D' or sort_order == 'd' :
                valid_input = True
            else:
                valid_input = False
                print('You Must Enter A or D!')

                """

    valid_input = False # Reset the error flag

    # Dose the user wish to display the whole table?
    
    while not valid_input: 
        display_option = input('\nDo you wish to display all the marathons in their present order?  (Y = YES, N = NO): ')
        if display_option == 'Y' or display_option == 'y' or display_option == 'N' or display_option == 'n':
            valid_input = True
        else:
            valid_input = False
            print('You Must Enter Y or N!')

    valid_input = False # Reset the error flag

    # Does the user wish to filter the table?
    
    if display_option == 'N' or display_option == 'n':
        while not valid_input: 
            filter_option = input('\nDo you wish to filter the marathons database? (Y = YES, N = NO): ') 
            if filter_option == 'Y' or filter_option == 'y' or filter_option == 'N' or filter_option == 'n':
                valid_input = True
            else:
                valid_input = False
                print('You Must Enter Y or N!')

    valid_input = False # Reset the error flag

    if (filter_option == 'Y' or filter_option == 'y') and (display_option == 'N' or display_option == 'n'):

        # Filter Codes - Date

        print('\nFROM DATE')
        
        while not valid_input:
            from_year = input('YEAR (1900 - 2099): ')
            try:
                from_year = int(from_year)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_year = 0
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_year = 0
            if (from_year < 1900 or from_year > 2099):
                valid_input = False
                print('Year must be between 1900 and 2099!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            from_month = input('MONTH (1 - 12): ')

            try:
                from_month = int(from_month)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_month = 0
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_month = 0
            if from_month < 1 or from_month > 12:
                valid_input = False
                print('Month must be between 1 and 12!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            from_day = input('DAY (1 - 31): ')
            try:
                from_day = int(from_day)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_day = 0
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_day = 0
            if from_day < 1 or from_day > 31:
                valid_input = False
                print('Day must be between 1 and 31!')
            else:
                valid_input = True

        from_date_num = date_to_num((from_year,from_month,from_day)) # Calculate the from date number
        
        print('\nTO DATE')

        valid_input = False # Reset the error flag

        while not valid_input:
            to_year = input('YEAR (1900 - 2099): ')
            try:
                to_year = int(to_year)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_year = 0
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_year = 0
            if to_year < 1900 or to_year > 2099:
                valid_input = False
                print('Year must be between 1900 and 2099!')
            else:
                valid_input = True
                
        valid_input = False # Reset the error flag

        while not valid_input:
            to_month = input('MONTH (1 - 12): ')
            try:
                to_month = int(to_month)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_month = 0
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_month = 0
            if to_month < 1 or to_month > 12:
                valid_input = False
                print('Month must be between 1 and 12!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            to_day = input('DAY (1 - 31): ')
            try:
                to_day = int(to_day)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_day = 0
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_day = 0
            if to_day < 1 or to_day > 31:
                valid_input = False
                print('Day must be between 1 and 31!')
            else:
                valid_input = True


        to_date_num = date_to_num((to_year,to_month,to_day)) # Calculate the to date number
        
        # Filter Codes - Distance

        valid_input = False # Reset the error flag

        while not valid_input:
            from_miles = input('\nFROM DISTANCE (MILES): ')
            try:
                from_miles = int(from_miles)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_miles = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_miles = -1
            if from_miles < 0 or from_miles > 99:
                valid_input = False
                print('Miles must be between 0 and 99!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            to_miles = input('TO DISTANCE (MILES): ')
            try:
                to_miles = int(to_miles)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_miles = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_miles = -1
            if to_miles < 1 or to_miles > 99:
                valid_input = False
                print('Miles must be between 1 and 99!')
            else:
                valid_input = True

        # Filter Codes - Time

        print('\nFROM TIME')

        valid_input = False # Reset the error flag

        while not valid_input:
            from_hours = input('HOURS (0 - 23): ')
            try:
                from_hours = int(from_hours)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_hours = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_hours = -1
            if from_hours < 0 or from_hours > 23:
                valid_input = False
                print('Hours must be between 0 and 23!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            from_mins = input('MINUTES (0 - 59): ')
            try:
                from_mins = int(from_mins)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_mins = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_mins = -1
            if from_mins < 0 or from_mins > 59:
                valid_input = False
                print('Minutes must be between 0 and 59!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            from_secs = input('SECONDS (0 - 59): ')
            try:
                from_secs = int(from_secs)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                from_secs = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                from_secs = -1
            if from_secs < 0 or from_secs > 59:
                valid_input = False
                print('Seconds must be between 0 and 59!')
            else:
                valid_input = True

        from_total_secs = calc_secs(from_hours,from_mins,from_secs)
        
        print('\nTO TIME')

        valid_input = False # Reset the error flag

        while not valid_input:
            to_hours = input('HOURS (0 - 23): ')
            try:
                to_hours = int(to_hours)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_hours = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_hours = -1
            if to_hours < 0 or to_hours > 23:
                valid_input = False
                print('Hours must be between 0 and 23!')
            else:
                valid_input = True

        valid_input = False # Reset the error flag

        while not valid_input:
            to_mins = input('MINUTES (0 - 59): ')
            try:
                to_mins = int(to_mins)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_mins = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_mins = -1
            if to_mins < 0 or to_mins > 59:
                valid_input = False
                print('Minutes must be between 0 and 59!')
            else:
                valid_input = True
                
        valid_input = False # Reset the error flag

        while not valid_input:
            to_secs = input('SECONDS (0 - 59): ')
            try:
                to_secs = int(to_secs)
            except ValueError:
                valid_input = False
                print('Invalid Input!')
                to_secs = -1
            except TypeError:
                valid_input = False
                print('Invalid Input!')
                to_secs = -1
            if to_secs < 0 or to_secs > 59:
                valid_input = False
                print('Seconds must be between 0 and 59!')
            else:
                valid_input = True

        to_total_secs = calc_secs(to_hours,to_mins,to_secs)
                        
        # Filter the table with the data entered by the user

        display_table = filter_the_table(main_table,
                                         from_date_num,       # Filter Codes - Date
                                         to_date_num,
                                         from_miles,     # Filter Codes - Distance
                                         to_miles,
                                         from_total_secs,     # Filter Codes - Time
                                         to_total_secs
                                         )
    else:
        display_table = filter_the_table(main_table) # Run the filter function with default settings if the user did not request filtering

    # Display the table

    display_the_table(display_table)

    valid_input = False # Reset the error flag

    # Ask the user if they would like to use the program again

    while not valid_input:
        quit_prog_option = input('\nDo you wish to use the program again? (Y = YES, N = NO): ')
        if quit_prog_option == 'Y' or quit_prog_option == 'y' or quit_prog_option == 'N' or quit_prog_option == 'n':
            valid_input = True
        else:
            valid_input = False
            print('You Must Enter Y or N!')

    if quit_prog_option == 'Y' or quit_prog_option == 'y':
        quit_prog = False
    else:
        quit_prog = True
