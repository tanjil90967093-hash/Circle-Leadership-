import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Fix the duplicate annotation and missing annotation
content = content.replace("@Composable\n@Composable\nfun CircleDealsBadge() {", "@Composable\nfun CircleDealsBadge() {")
content = content.replace("fun ProductCard(product: Product, modifier: Modifier = Modifier) {", "@Composable\nfun ProductCard(product: Product, modifier: Modifier = Modifier) {")

# Add missing import for Brush
if "import androidx.compose.ui.graphics.Brush" not in content:
    content = content.replace("import androidx.compose.ui.graphics.Color", "import androidx.compose.ui.graphics.Color\nimport androidx.compose.ui.graphics.Brush")

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

