import re
pattern = r"[*^]+([A-Za-z ]{6,})[*^]+[^+\w]*\++([\d.,\-]+)\++"

encrypted_messages = input()
matches = re.findall(pattern, encrypted_messages)
artifacts = {}

for match in matches:
    artifact = match[0]
    coordinates = match[1].split(",")
    if not artifact or not coordinates:
        artifacts.clear()
    else:
        artifacts[artifact] = coordinates

if artifacts:
    for artifact, coordinates in artifacts.items():
        print(f"Found {artifact} at coordinates {", ".join(coordinates)}.")
else:
    print("No valid artifacts found.")