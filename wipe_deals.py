with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1

for i, line in enumerate(lines):
    if "// Circle Deals Section" in line:
        start_idx = i - 2 # to capture the 'item {' before it
    if 'SectionTitle("Categories", "See All")' in line:
        end_idx = i - 2 # to keep 'item {' before it
        break

print(f"Start: {start_idx}, End: {end_idx}")

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx]

# Also remove circleDealsList
list_start = -1
list_end = -1
for i, line in enumerate(lines):
    if 'var circleDealsList by remember {' in line:
        list_start = i
    if list_start != -1 and 'val searchHints' in line:
        list_end = i
        break

print(f"List Start: {list_start}, List End: {list_end}")
if list_start != -1 and list_end != -1:
    del lines[list_start:list_end]

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.writelines(lines)
