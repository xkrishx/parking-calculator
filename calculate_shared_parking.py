from LandUse import parking_demand
from get_inputs import get_working_directory

#Get working directory from command line input
in_arg = get_working_directory()
working_directory = in_arg.dir

#Calculate weekday parking tables and export to Excel
weekday_parking_demand = parking_demand('Weekday')
weekday_filepath = working_directory + '\Outputs\WeekdayParking.xlsx'
weekday_parking_demand.to_excel(weekday_filepath)

#Calculate weekend parking tables and export to Excel
weekend_parking_demand = parking_demand('Weekend')
weekend_filepath = working_directory + '\Outputs\WeekendParking.xlsx'
weekend_parking_demand.to_excel(weekend_filepath)



