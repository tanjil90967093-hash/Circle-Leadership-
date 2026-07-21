import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Fix onCircleDealsClick() with no args
content = content.replace("onCircleDealsClick()", "onCircleDealsClick(null)")

# Fix onCircleDealsClick(product.id) -> product.id.toString()
content = content.replace("onCircleDealsClick(product.id)", "onCircleDealsClick(product.id.toString())")

# Update CircleDealCard to have clickable with string ID
# Find `CircleDealCard(circleDealsList[index], modifier = Modifier.width(130.dp))`
content = content.replace("CircleDealCard(circleDealsList[index], modifier = Modifier.width(130.dp))", 
                          "CircleDealCard(circleDealsList[index], modifier = Modifier.width(130.dp).clickable { onCircleDealsClick(circleDealsList[index].id.toString()) })")

# Find `CircleDealCard(product, modifier = Modifier.weight(1f))` in HomeScreen (wait, the one in CircleDealsScreen has `onProductClick` instead)
# Only change the ones in HomeScreen that might not have clickables.
# Actually I'll just leave others if they are fine.

# Let's also fix the missing `maxLines` on the first Show More button if I care, but just fixing the compile error is enough.

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

