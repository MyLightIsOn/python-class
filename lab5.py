import re
import pyperclip

pasted_data = pyperclip.paste()

# Regex for part number
numbers_regex = re.compile(r'(H[0-9])-([0-9]{4})')

# Regex for unit counts
unit_count_regex = re.compile(r'#\d+')

# Extra part number from pasted clipboard text
part_numbers = numbers_regex.findall(pasted_data)

# Extract unit counts from pasted clipboard text
unit_counts = unit_count_regex.findall(pasted_data)

# Turns unit_counts strings into integers.
clean_unit_counts = [int(u[1:]) for u in unit_counts]

# Extract supply line numbers from part numbers
supply_line_indices = [int(number[0][1]) for number in part_numbers]

# Initialize totals list for 10 supply lines
totals = [0] * 10

# Loop using index and update totals
for i in range(len(supply_line_indices)):
    line_index = supply_line_indices[i]
    units = clean_unit_counts[i]
    totals[line_index] += units

supply_line_names = [
    "Tango",    # 0
    "Sierra",   # 1
    "Victor",   # 2
    "Foxtrot",  # 3
    "Xray",     # 4
    "Hotel",    # 5
    "Delta",    # 6
    "Romeo",    # 7
    "India",    # 8
    "Echo"      # 9
]

for i in range(len(totals)):
    if totals[i] > 0:
        print(f"Supply Line {supply_line_names[i]} ---> {totals[i]}")

print(totals)
print(part_numbers)
print(unit_counts)
print(supply_line_indices)





"""
We need part H3-4729, uhh let's make that... yeah #12 units of that. 
And then also two of the H9-8281. Oh wait, no — it’s #9 actually. 
Right, add H1-3842 to the list, we’ll do #30 for that one.
I almost forgot — H4-6619, #17 on that. 
Also H3-0001 #45 and one more, H7-9292 with #11 units.
Make sure you don’t miss H0-1188 — give me #20 of those.
Oh! And H6-3217... #6 on that. Got it? Okay, I think that’s all for now.
"""

