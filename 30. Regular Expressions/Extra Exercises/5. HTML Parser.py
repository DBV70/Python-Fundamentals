import re

html_content = input()

# Extract title
title_match = re.search(r'<title>(.*?)</title>', html_content, re.DOTALL)
title = title_match.group(1) if title_match else ""

# Extract body content and remove all HTML tags
body_match = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL)
body_content = body_match.group(1) if body_match else ""

# Remove all HTML tags (anything between < and >)
cleaned_content = re.sub(r'<[^>]*>|\\n', '', body_content)

# Print results
print(f"Title: {title}")
print(f"Content: {cleaned_content}")