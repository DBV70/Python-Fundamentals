import re
pattern = r"\b(?P<Day>\d{2})([-.\/])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
dates = input()
matches = re.finditer(pattern, dates)
for match in matches:
    print(f"Day: {match.group('Day')}, Month: {match.group('Month')}, Year: {match.group('Year')}")
