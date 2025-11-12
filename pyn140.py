from datetime import datetime
today = datetime.now()
formats = {
    "dd-mm-yyyy": today.strftime("%d-%m-%Y"),
    "dd-MMM-yyyy": today.strftime("%d-%b-%Y"),
    "MMMM/dd/yyyy": today.strftime("%B/%d/%Y"),
    "yyyy/mm/dd": today.strftime("%Y/%m/%d"),
    "Day, dd Month yyyy": today.strftime("%A, %d %B %Y"),
    "dd/mm/yy hh:mm:ss": today.strftime("%d/%m/%y %H:%M:%S"),
}
for name, value in formats.items():
    print(f"{name}: {value}")
