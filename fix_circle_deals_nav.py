import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Let's fix the build issue first if there is any, maybe the product click in Circle Deals is calling a non-existent route. Wait, the compile task hasn't finished reporting.
