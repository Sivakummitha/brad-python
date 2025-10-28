#"Create a list of months from jan to dec in list and find out the quarter and financial year for each month for year 2022 and print like below
#ex: for Jan 2022, output should be: ""Jan 2022 - Q4 FY 2021-2022"",
#for oct 2022 : ""Oct 2022- Q3 FY 2022 - 2023"", etc"
import calendar
year = 2022
months = [calendar.month_abbr[i] for i in range(1, 13)]
for month_num, month_name in enumerate(months, 1):
    quarter = ''
    financial_year = ''
    if 4 <= month_num <= 6:
        quarter = 'Q1'
        financial_year = f'FY {year}-{year+1}'
    elif 7 <= month_num <= 9:
        quarter = 'Q2'
        financial_year = f'FY {year}-{year+1}'
    elif 10 <= month_num <= 12:
        quarter = 'Q3'
        financial_year = f'FY {year}-{year+1}'
    elif 1 <= month_num <= 3:
        quarter = 'Q4'
        financial_year = f'FY {year-1}-{year}'

    print(f'{month_name} {year} - {quarter} {financial_year}')



