year=365
month=30
print("Take a guess of any number of days:")
def get_years_months_days():
    days=input(int())
    if int(days)>365:
        years=int(int(days) /365)
        months=int(int(int(days) % 365) / 30)
        remaining_days=int(int(int(days) % 365) % 30)
        print(f"years:{years},months:{months},days:{remaining_days}")
    elif int(days)>30:
        years=0
        months=int(int(days) / 30)
        remaining_days=int(int(days) % 30)
        print(f"years:{years},months:{months},days:{remaining_days}")
    else:
        years=0
        months=0
        remaining_days=days
        print(f"years:{years},months:{months},days:{remaining_days}")    


get_years_months_days()    

    