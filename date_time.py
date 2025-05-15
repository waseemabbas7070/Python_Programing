from datetime import datetime
from datetime import date
from datetime import timedelta
now = datetime.now()
today = datetime.today().date()
specific_date = date(2022,6,4)
formated_date =now.strftime("%d-%m-%Y %H:%M:%S")

today = datetime.today()
tomorrow = today + timedelta(days=1)
print(f"Current Date and Time : {now}")
print(f"Today's Date : {today}")
print(f"Specific Date : {specific_date}")
print(f"Formatted Date : {formated_date}")
print(f"Tomorrow's Date : {tomorrow}")
