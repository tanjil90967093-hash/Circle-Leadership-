import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Fix duplicate composable
content = content.replace("@Composable\n@Composable\nfun CircleDealsBadge() {", "@Composable\nfun CircleDealsBadge() {")
content = content.replace("fun ProductCard(product: Product, modifier: Modifier = Modifier) {", "@Composable\nfun ProductCard(product: Product, modifier: Modifier = Modifier) {")


with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

