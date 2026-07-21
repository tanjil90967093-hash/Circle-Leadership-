import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

product_details_screen = """
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ProductDetailsScreen(productId: Int, onBack: () -> Unit = {}) {
    val product = mockProducts.find { it.id == productId } ?: return
    
    val context = androidx.compose.ui.platform.LocalContext.current
    val shareIntent = android.content.Intent(android.content.Intent.ACTION_SEND).apply {
        type = "text/plain"
        putExtra(android.content.Intent.EXTRA_SUBJECT, "Circle Bazar - Product")
        putExtra(android.content.Intent.EXTRA_TEXT, "Check out this product on Circle Bazar! \\n\\nhttps://circlebazar.com/product/${product.id}")
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Product Details", style = MaterialTheme.typography.titleMedium) },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Outlined.ArrowBack, contentDescription = "Back")
                    }
                },
                actions = {
                    IconButton(onClick = {
                        val chooser = android.content.Intent.createChooser(shareIntent, "Share")
                        context.startActivity(chooser)
                    }) {
                        Icon(Icons.Outlined.Share, contentDescription = "Share")
                    }
                    IconButton(onClick = { }) {
                        Icon(Icons.Outlined.ShoppingCart, contentDescription = "Cart")
                    }
                },
                colors = TopAppBarDefaults.topAppBarColors(containerColor = Color.White)
            )
        },
        bottomBar = {
            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .background(Color.White)
                    .shadow(elevation = 16.dp)
                    .padding(16.dp),
                horizontalArrangement = Arrangement.spacedBy(12.dp)
            ) {
                androidx.compose.material3.OutlinedButton(
                    onClick = { /* Add to cart */ },
                    modifier = Modifier.weight(1f),
                    border = BorderStroke(1.dp, Color(0xFF00643C)),
                    colors = androidx.compose.material3.ButtonDefaults.outlinedButtonColors(contentColor = Color(0xFF00643C))
                ) {
                    Text("Add to Cart")
                }
                Button(
                    onClick = { /* Buy Now */ },
                    modifier = Modifier.weight(1f),
                    colors = androidx.compose.material3.ButtonDefaults.buttonColors(containerColor = Color(0xFF00643C))
                ) {
                    Text("Buy Now")
                }
            }
        }
    ) { paddingValues ->
        LazyColumn(
            contentPadding = PaddingValues(top = paddingValues.calculateTopPadding(), bottom = 80.dp),
            modifier = Modifier.fillMaxSize().background(Color(0xFFF5F5F5))
        ) {
            item {
                // Product Image View
                Box(
                    modifier = Modifier
                        .fillMaxWidth()
                        .height(300.dp)
                        .background(Color.White)
                ) {
                    AsyncImage(
                        model = product.imageUrl,
                        contentDescription = product.title,
                        contentScale = ContentScale.Fit,
                        modifier = Modifier.fillMaxSize().padding(16.dp)
                    )
                }
            }
            
            if (product.isCircleDeal) {
                item {
                    // Animated Circle Deal Timer Card
                    val infiniteTransition = androidx.compose.animation.core.rememberInfiniteTransition(label = "pulse")
                    val scale by infiniteTransition.animateFloat(
                        initialValue = 0.98f,
                        targetValue = 1.02f,
                        animationSpec = androidx.compose.animation.core.infiniteRepeatable(
                            animation = androidx.compose.animation.core.tween(1000, easing = androidx.compose.animation.core.FastOutSlowInEasing),
                            repeatMode = androidx.compose.animation.core.RepeatMode.Reverse
                        ), label = "pulseScale"
                    )
                    
                    Box(modifier = Modifier.fillMaxWidth().background(Color.White).padding(bottom = 8.dp)) {
                        Card(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(horizontal = 16.dp, vertical = 8.dp)
                                .androidx.compose.ui.draw.scale(scale),
                            colors = CardDefaults.cardColors(containerColor = Color(0xFFFFF8E1)),
                            border = BorderStroke(1.dp, Color(0xFFFFC107)),
                            shape = RoundedCornerShape(12.dp)
                        ) {
                            Row(
                                modifier = Modifier.padding(16.dp).fillMaxWidth(),
                                verticalAlignment = Alignment.CenterVertically,
                                horizontalArrangement = Arrangement.SpaceBetween
                            ) {
                                Column {
                                    Text("⚡ CIRCLE DEAL", color = Color(0xFFFF9800), fontWeight = FontWeight.ExtraBold, fontSize = 16.sp)
                                    Text("Ends in", color = Color.Gray, fontSize = 12.sp)
                                }
                                
                                val timerBg = Color(0xFFFF9800)
                                val timerText = Color.White
                                Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                                    Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 8.dp, vertical = 4.dp)) {
                                        Text("02", color = timerText, fontSize = 16.sp, fontWeight = FontWeight.ExtraBold)
                                    }
                                    Text(":", color = timerBg, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                                    Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 8.dp, vertical = 4.dp)) {
                                        Text("45", color = timerText, fontSize = 16.sp, fontWeight = FontWeight.ExtraBold)
                                    }
                                    Text(":", color = timerBg, fontSize = 18.sp, fontWeight = FontWeight.Bold)
                                    Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 8.dp, vertical = 4.dp)) {
                                        Text("12", color = timerText, fontSize = 16.sp, fontWeight = FontWeight.ExtraBold)
                                    }
                                }
                            }
                        }
                    }
                }
            }
            
            item {
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Color.White)
                        .padding(16.dp)
                ) {
                    if (product.isCircleDeal) {
                        CircleDealsBadge()
                        Spacer(modifier = Modifier.height(4.dp))
                    }
                    Text(
                        text = product.title,
                        style = MaterialTheme.typography.titleMedium,
                        fontWeight = FontWeight.Bold
                    )
                    Spacer(modifier = Modifier.height(8.dp))
                    Row(verticalAlignment = Alignment.Bottom) {
                        Text("৳ ${product.price.toInt()}", style = MaterialTheme.typography.headlineMedium, color = Color(0xFF00643C), fontWeight = FontWeight.Bold)
                        if (product.oldPrice != null) {
                            Spacer(modifier = Modifier.width(8.dp))
                            Text("৳ ${product.oldPrice.toInt()}", style = MaterialTheme.typography.bodyMedium, color = Color.Gray, textDecoration = androidx.compose.ui.text.style.TextDecoration.LineThrough)
                        }
                        if (product.discount != null) {
                            Spacer(modifier = Modifier.width(8.dp))
                            Text("-${product.discount}%", style = MaterialTheme.typography.labelMedium, color = Color.Red, modifier = Modifier.background(Color(0xFFFFEBEE), RoundedCornerShape(4.dp)).padding(horizontal = 4.dp, vertical = 2.dp))
                        }
                    }
                    
                    Spacer(modifier = Modifier.height(16.dp))
                    Row(verticalAlignment = Alignment.CenterVertically) {
                        Icon(Icons.Filled.Star, contentDescription = "Rating", tint = Color(0xFFFFC107), modifier = Modifier.size(16.dp))
                        Spacer(modifier = Modifier.width(4.dp))
                        Text("${product.rating}", style = MaterialTheme.typography.bodyMedium)
                        Spacer(modifier = Modifier.width(16.dp))
                        Text("${product.soldCount} Sold", style = MaterialTheme.typography.bodyMedium, color = Color.Gray)
                    }
                }
                
                Spacer(modifier = Modifier.height(8.dp))
                
                // Description placeholder
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .background(Color.White)
                        .padding(16.dp)
                ) {
                    Text("Product Description", style = MaterialTheme.typography.titleMedium, fontWeight = FontWeight.Bold)
                    Spacer(modifier = Modifier.height(8.dp))
                    Text(
                        "This is a premium product available on Circle Bazar. It features top-notch quality and durability. Get it now while stocks last! Especially during Circle Deals, you can enjoy massive discounts.",
                        style = MaterialTheme.typography.bodyMedium,
                        color = Color.DarkGray,
                        lineHeight = 20.sp
                    )
                }
            }
        }
    }
}
"""

content += product_details_screen

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
