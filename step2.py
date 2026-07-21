import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()


circle_deals_section = """      item {
        Spacer(modifier = Modifier.height(24.dp))
        Row(
           modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
           horizontalArrangement = Arrangement.SpaceBetween,
           verticalAlignment = Alignment.CenterVertically
        ) {
           Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.weight(1f)) {
             val infiniteTransition = androidx.compose.animation.core.rememberInfiniteTransition(label = "shimmer")
             val translateAnim = infiniteTransition.animateFloat(
                initialValue = 0f,
                targetValue = 1000f,
                animationSpec = androidx.compose.animation.core.infiniteRepeatable(
                    animation = androidx.compose.animation.core.tween(durationMillis = 3000, easing = androidx.compose.animation.core.LinearEasing),
                    repeatMode = androidx.compose.animation.core.RepeatMode.Restart
                ), label = "shimmerTranslate"
             )
             val brush = androidx.compose.ui.graphics.Brush.linearGradient(
                colors = listOf(Color(0xFF4CAF50), Color(0xFFFFC107), Color(0xFFFF9800), Color(0xFFFFD700), Color(0xFF4CAF50)),
                start = androidx.compose.ui.geometry.Offset(translateAnim.value, translateAnim.value),
                end = androidx.compose.ui.geometry.Offset(translateAnim.value + 200f, translateAnim.value + 200f)
             )
             Text(
                text = "CIRCLE DEALS", 
                style = MaterialTheme.typography.titleLarge.copy(
                    fontWeight = FontWeight.ExtraBold,
                    letterSpacing = 1.sp,
                    brush = brush,
                    shadow = androidx.compose.ui.graphics.Shadow(
                        color = Color(0xFFFFC107).copy(alpha = 0.5f), 
                        offset = androidx.compose.ui.geometry.Offset(0f, 4f), 
                        blurRadius = 8f
                    )
                ),
                maxLines = 1,
                overflow = TextOverflow.Ellipsis,
                modifier = Modifier.weight(1f, fill = false)
             )
             Spacer(modifier = Modifier.width(12.dp))
             val timerBg = Color(0xFFFFB300)
             val timerText = Color.Black
             Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                 Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 6.dp, vertical = 3.dp)) {
                     Text("02", color = timerText, fontSize = 12.sp, fontWeight = FontWeight.ExtraBold)
                 }
                 Text(":", color = timerBg, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                 Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 6.dp, vertical = 3.dp)) {
                     Text("45", color = timerText, fontSize = 12.sp, fontWeight = FontWeight.ExtraBold)
                 }
                 Text(":", color = timerBg, fontSize = 14.sp, fontWeight = FontWeight.Bold)
                 Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 6.dp, vertical = 3.dp)) {
                     Text("12", color = timerText, fontSize = 12.sp, fontWeight = FontWeight.ExtraBold)
                 }
             }
           }
           Text("Show More", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Medium, modifier = Modifier.clickable { onCircleDealsClick(null) })
        }
        Spacer(modifier = Modifier.height(12.dp))
      }
      
      item {
        val circleDeals = mockProducts.filter { it.isCircleDeal }.shuffled()
        LazyRow(
            contentPadding = PaddingValues(horizontal = 16.dp),
            horizontalArrangement = Arrangement.spacedBy(12.dp),
            modifier = Modifier.fillMaxWidth()
        ) {
            items(circleDeals) { product ->
                ProductCard(product, modifier = Modifier.width(140.dp).clickable { onCircleDealsClick(product.id.toString()) })
            }
        }
      }
      
      item {
        Spacer(modifier = Modifier.height(24.dp))"""

content = content.replace("      item {\n        Spacer(modifier = Modifier.height(24.dp))\n        SectionTitle(\"Categories\", \"See All\")", circle_deals_section + "\n        SectionTitle(\"Categories\", \"See All\")")

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

