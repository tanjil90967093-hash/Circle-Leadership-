import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

content = content.replace(
    "val circleDeals = mockProducts.filter { it.isCircleDeal }.shuffled()",
    "val circleDeals = remember { mockProducts.filter { it.isCircleDeal }.shuffled() }"
)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
