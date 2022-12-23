import pandas as pd
bot_command = "SN!猜數字 "
lowerbound = 0
upperbound = 1001
c = "start"
while c != "end":
    print("Between " + str(lowerbound) + " and " + str(upperbound))
    result = int((upperbound - lowerbound) / 2 + lowerbound)
    df = pd.DataFrame([bot_command + str(result)])
    df.to_clipboard(index=False, header=False)
    print("Let's try " + str(result) + " (copied to clipboard)")
    c = input("小於(s)/大於(g)/猜到了(end)/RESET: ")
    if c == "s":
        lowerbound = result
    elif c == "g":
        upperbound = result
    elif c == "RESET":
        lowerbound = 0
        upperbound = 1001
    elif c != "end":
        print("ERROR, please input again")
