# Imports.
import pandas as pd
import numpy as np
import re
import json

# Define regex string lookup and array of results.
target = "Cinderella"
regex = r"([^.]*?" + target + "[^.]*\.)"
result = []

# Open text file and iterate through text file and apply regex line by line.
file = open("story.txt")
iterCount = 0
for lineNumber, line in enumerate(file):

    # Skip empty lines and regex that has no matches.
    if len(line) > 1 and len(re.findall(regex, line)) > 0:

        # Push dictionary to result list.
        regexResult = re.findall(regex, line)
        result.append({
            "Word": target,
            "Line Number": int(lineNumber),
            "Count": len(regexResult),
            "Result": regexResult
        })

        # Add to DataFrame.
        # df.loc[iterCount] = result[iterCount]
        iterCount += 1

# Close file to release memory.
file.close()

# Create DataFrame based on above list for result.
columns = ["Word", "Line Number", "Count", "Result"]
# index = [target]
df = pd.DataFrame(result, columns=columns)

# Print result.
print(df)
# print(json.dumps(result, indent=2))
