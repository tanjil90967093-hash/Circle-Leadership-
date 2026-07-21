import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()


badge = """@Composable
fun CircleDealsBadge() {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier
            .padding(bottom = 4.dp)
            .clip(RoundedCornerShape(4.dp))
            .background(androidx.compose.ui.graphics.Brush.linearGradient(listOf(Color(0xFF00643C), Color(0xFF4CAF50))))
            .padding(horizontal = 6.dp, vertical = 2.dp)
    ) {
        Icon(Icons.Outlined.Star, contentDescription = null, tint = Color.White, modifier = Modifier.size(10.dp))
        Spacer(modifier = Modifier.width(2.dp))
        Text("Circle Deals", color = Color.White, fontSize = 9.sp, fontWeight = FontWeight.Bold)
    }
}
"""

if "fun CircleDealsBadge" not in content:
    content = content.replace("fun ProductCard", badge + "\nfun ProductCard")


product_card_title = """        Spacer(modifier = Modifier.height(8.dp))
        Text(
          product.title,"""

product_card_title_replacement = """        Spacer(modifier = Modifier.height(8.dp))
        if (product.isCircleDeal) {
            CircleDealsBadge()
        }
        Text(
          product.title,"""

content = content.replace(product_card_title, product_card_title_replacement)

# Make sure normal product grid clicks go to onProductClick
# In HomeScreen, the "Just For You" products grid is like this:
grid_target = """      val chunkedProducts = mockProducts.chunked(2)
      items(chunkedProducts) { rowProducts ->
        Row(
          modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 8.dp, vertical = 6.dp),
          horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
          for (product in rowProducts) {
            ProductCard(product, modifier = Modifier.weight(1f))
          }"""

grid_replacement = """      val chunkedProducts = mockProducts.chunked(2)
      items(chunkedProducts) { rowProducts ->
        Row(
          modifier = Modifier
            .fillMaxWidth()
            .padding(horizontal = 8.dp, vertical = 6.dp),
          horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
          for (product in rowProducts) {
            ProductCard(product, modifier = Modifier.weight(1f).clickable { 
                if (product.isCircleDeal) {
                    onCircleDealsClick(product.id.toString())
                } else {
                    onProductClick(product.id)
                }
            })
          }"""

content = content.replace(grid_target, grid_replacement)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
