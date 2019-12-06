


#PyBank
#Dependencies
import os
import csv


# In[25]:


#files to load and output
file_to_load = os.path.join("budget_data.csv")
file_to_output = os.path.join("budget_analysis.txt")

#Track financial parameters
total_months = 0
month_of_change =[]
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999999999999999999999]
total_net = 0

#read csv and convert into a list of dictionaries

#budget_data.csv = os.path.join(".", "PyBank", "budget_data.csv")

with open(file_to_load, newline="") as financial_data:
    reader = csv.reader(financial_data)
        
    header = next(reader)
    print(header)
    
    #Extract first row to aboid appending to net_change_list
    first_row = next(reader)
    print(first_row)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    
    #loop thru data
    for row in reader:
        
            #track the toal
            total_months = total_months + 1
            total_net = total_net + int(row[1])
            print(total_net)
            
            #track the net change
            net_change = int(row[1]) - prev_net
            prev_net = int(row[1])
            net_change_list = net_change_list + [net_change]
            month_of_change = month_of_change + [row[0]]
            
            if net_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = net_change
                
            if net_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = net_change
                
    #calculate the average net change
    net_monthly_avg = sum(net_change_list) / len(net_change_list)
    
    output = (
            f"\nFinancial Analysis\n"
            f"=======================\n"
            f"Total Months: {total_months}\n"
            f"Total: ${total_net}\n"
            f"Average Change : ${net_monthly_avg:.2f}\n"
            f"Greatest Increase In Profits {greatest_increase[0]}, (${greatest_increase[1]})\n"
            f"Greatest Decrease In Profits {greatest_decrease[0]}, (${greatest_decrease[1]})\n"
    ) 
    
    print(output)
    
    with open(file_to_output, "w") as text_file:
        text_file.write(output)
    
    
                
                
                
    
    


# In[ ]:




