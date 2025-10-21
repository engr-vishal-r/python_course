import difflib
import os

strings = ["he", "yellow","helo","hello"]
target = "hell"

best_match = difflib.get_close_matches(target, strings, n=1)
if best_match:
    print(best_match[0])
else:
    print("No match found")



best_match = max(strings, key=lambda s: len(os.path.commonprefix([s, target])))
print(best_match)