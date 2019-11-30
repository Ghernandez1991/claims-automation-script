# claims-automation-scripts


1-Script 1

Intercompany arbitration requires repetition such as creating folders to store claims data and creating uniform files for each claim in arb. I wrote a brief script to automate the process. 

Problem- Having to create a folder for each claim, numbering it accordingly and creating a file called (contentions.docx) for each individual claim on my list. 

Solution. 
The script takes a python list, iterates through it and for each item in the list creates a folder and places a word docx titled "contentions" inside the folder. 

2-Script 2


Problem
When issuing checks after intercompany arbitration, it requires the user to change the claim loss details and update the liability percentage. In a case where comparative negligence was applied, the system reduces the payment by the percentage of negligence. However
this requires adjusters to do the math and find out the amount of money required, before the comparative negligence is applied. 

For example. 

The award is $9,000. We were found 40% at fault. 
Users would need to take 9000/.40 = 22,500 for claim center to apply 40% from $22,500. I have had more than several users ask me how to do this. 

The script automates this process by selecting inputs(negligence % and money due) and completes the math operation. 
The numbers are converted to floats and rounded to ensure a 2 digit number. 

I have pumped this out to an executable as well for use on non-python installed computers. 



3-Script 3


When a decision is reached, I need to update the claim file with the decision and notify the adjuster. This is a time consuming process that takes numerous clicks to navigate to the decision and to type in the claim number repetitively. 

Solution


I wrote a python function using beautiful soup and spliter(selenium) to automate the process. The function takes in a user claim number, and then clicks its way to the decision with no more imput from the user. The function ends at the PDF version of the decision, allowing the user to download it. 
