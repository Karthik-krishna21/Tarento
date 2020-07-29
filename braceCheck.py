# - Accept a String input
# - Print the number of opening braces and closing braces in the input String
# - Verify if every opening brace has an equivalent closing brace. Print well formed if every opening brace has an equivalent closing brace.
# Print invalid if every opening brace does not have an equivalent closing brace

# Input and variable initialization 
string = input ()
openCount = 0
closeCount = 0
tcount = 0

# Loop to check number of braces and whether they match
for i in string:
  if i == '{':
    openCount += 1
    if tcount >= 0:
        tcount += 1

  elif i == '}':
    closeCount += 1
    if tcount <= 0:
        tcount = -1
    else:
        tcount -= 1

# Output    
print ("Opening braces - ", openCount, ", Closing braces - ", closeCount)
if openCount == closeCount and tcount == 0:
  print ("Well Performed")
else:
  print ("Invalid")
