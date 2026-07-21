import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

content = content.replace(".androidx.compose.ui.draw.scale(scale)", ".scale(scale)")

if "import androidx.compose.ui.draw.scale" not in content:
    content = content.replace("import androidx.compose.ui.graphics.Color", "import androidx.compose.ui.graphics.Color\nimport androidx.compose.ui.draw.scale")

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
