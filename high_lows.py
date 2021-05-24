import csv
from datetime import date, datetime
from matplotlib import pyplot as plt

filename = 'san_fran.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    # getting high temps
    dates, highs, lows = [], [], []
    for row in reader:
        # print(row)
        try:
            current_date = datetime.strptime(row[0], "%m/%d/%Y")
            dates.append(current_date)
            # print(current_date)

            highs.append(int(row[1]))
            lows.append(int(row[3]))
        except:
            continue
    
    # print(highs)
    # print(dates)

    # plot data
    fig = plt.figure(figsize=(10,6))
    plt.plot(dates, highs, c='red', alpha=0.5)
    plt.plot( dates, lows, c='blue', alpha = 0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
    # shading

    # format plot
    plt.title("Daily high and low temperatues of 2014 : sanfransicso", fontsize = 24)
    plt.xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)", fontsize = 16)
    plt.tick_params(axis='both', which='major', labelsize=16 , color = 'purple')
    # changing tick formats by tick params
    
    plt.show()


     

        

    
