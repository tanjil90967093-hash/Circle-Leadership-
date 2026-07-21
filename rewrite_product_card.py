import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

badge_code = """@Composable
fun CircleDealsBadge() {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        modifier = Modifier
            .padding(bottom = 4.dp)
            .clip(RoundedCornerShape(4.dp))
            .background(Brush.linearGradient(listOf(Color(0xFF00643C), Color(0xFF4CAF50))))
            .padding(horizontal = 6.dp, vertical = 2.dp)
    ) {
        Icon(Icons.Outlined.Star, contentDescription = null, tint = Color.White, modifier = Modifier.size(10.dp))
        Spacer(modifier = Modifier.width(2.dp))
        Text("Circle Deals", color = Color.White, fontSize = 9.sp, fontWeight = FontWeight.Bold)
    }
}
"""

# Insert badge code before ProductCard
content = content.replace("fun ProductCard(", badge_code + "\nfun ProductCard(")

# Now inject it into ProductCard title area
product_card_target = """        Spacer(modifier = Modifier.height(8.dp))
        Text(
          product.title,"""

product_card_replacement = """        Spacer(modifier = Modifier.height(8.dp))
        // Show badge for half the products to simulate some being Circle Deals, or maybe all mockProducts are Circle Deals?
        // Let's assume some are Circle Deals. For now we will just show it for mockProducts.
        // Or better yet, update the Product data model if possible. Wait, can't easily change data model if it's used elsewhere.
        // Let's just show it randomly based on product id or always. 
        if (product.id.hashCode() % 2 == 0) {
            CircleDealsBadge()
        }
        Text(
          product.title,"""

content = content.replace(product_card_target, product_card_replacement)

# And inject it into CircleDealCard
circle_deal_card_target = """        Spacer(modifier = Modifier.height(4.dp))
        Text(
          product.title,"""

circle_deal_card_replacement = """        Spacer(modifier = Modifier.height(4.dp))
        CircleDealsBadge()
        Text(
          product.title,"""

content = content.replace(circle_deal_card_target, circle_deal_card_replacement)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

