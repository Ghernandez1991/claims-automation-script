


percent = input("What percentage liable are we? Example .35")
money = input("How much do we owe to the other company? ex 35,000.50")
amount_due = float(money)/float(percent)

final_amount = amount_due.__round__(2)



print(f"Place {final_amount} when writing the check in claim center. When the negligence is applied, it will equal the amount due. ")

input()
