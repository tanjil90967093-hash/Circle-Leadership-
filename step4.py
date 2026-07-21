import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

circle_deals_screen = """
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun CircleDealsScreen(highlightProductId: String? = null, onBack: () -> Unit = {}, onProductClick: (Int) -> Unit = {}) {
    val context = androidx.compose.ui.platform.LocalContext.current
    val shareIntent = android.content.Intent(android.content.Intent.ACTION_SEND).apply {
        type = "text/plain"
        putExtra(android.content.Intent.EXTRA_SUBJECT, "Circle Bazar - Circle Deals")
        putExtra(android.content.Intent.EXTRA_TEXT, "Check out the amazing Circle Deals on Circle Bazar! \\n\\nhttps://circlebazar.com/deals")
    }

    val circleDealsProducts = remember(highlightProductId) {
        val allDeals = mockProducts.filter { it.isCircleDeal }.toMutableList()
        if (highlightProductId != null) {
            val highlighted = allDeals.find { it.id.toString() == highlightProductId }
            if (highlighted != null) {
                allDeals.remove(highlighted)
                allDeals.add(0, highlighted) // Put at the top
            }
        }
        allDeals
    }

    // Animated Placeholder for Search
    val searchHints = listOf("Search Circle Deals", "Wireless Earbuds", "Samsung Galaxy", "Nike Shoes", "Laptop", "Bluetooth Speaker", "Women's Handbag", "Gaming Mouse")
    var currentHintIndex by remember { androidx.compose.runtime.mutableIntStateOf(0) }
    
    LaunchedEffect(Unit) {
        while (true) {
            kotlinx.coroutines.delay(2000)
            currentHintIndex = (currentHintIndex + 1) % searchHints.size
        }
    }

    Scaffold(
        topBar = {
            Column(modifier = Modifier.fillMaxWidth().background(Color.White).shadow(4.dp)) {
                // Top Row: Back, Title, Cart, Share
                Row(
                    modifier = Modifier.fillMaxWidth().statusBarsPadding().height(56.dp).padding(horizontal = 4.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Outlined.ArrowBack, contentDescription = "Back", tint = Color.Black)
                    }
                    
                    // Animated Title
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
                        colors = listOf(Color(0xFF4CAF50), Color(0xFF00C853), Color(0xFF4CAF50)),
                        start = androidx.compose.ui.geometry.Offset(translateAnim.value, translateAnim.value),
                        end = androidx.compose.ui.geometry.Offset(translateAnim.value + 200f, translateAnim.value + 200f)
                    )
                    
                    Text(
                        text = "Circle Deals",
                        style = MaterialTheme.typography.titleLarge.copy(
                            fontWeight = FontWeight.ExtraBold,
                            fontFamily = FontFamily.Serif,
                            brush = brush
                        ),
                        modifier = Modifier.weight(1f).padding(horizontal = 8.dp),
                        maxLines = 1,
                        overflow = TextOverflow.Ellipsis
                    )
                    
                    IconButton(onClick = { /* Open Cart */ }) {
                        Icon(Icons.Outlined.ShoppingCart, contentDescription = "Cart", tint = Color.Black)
                    }
                    IconButton(onClick = {
                        val chooser = android.content.Intent.createChooser(shareIntent, "Share Circle Deals")
                        context.startActivity(chooser)
                    }) {
                        Icon(Icons.Outlined.Share, contentDescription = "Share", tint = Color.Black)
                    }
                }
                
                // Search Box Row
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(horizontal = 16.dp, vertical = 8.dp)
                        .height(44.dp)
                        .clip(RoundedCornerShape(22.dp))
                        .background(Color(0xFFF5F5F5))
                        .clickable { /* Navigate to search */ }
                        .padding(horizontal = 12.dp),
                    verticalAlignment = Alignment.CenterVertically
                ) {
                    Icon(Icons.Outlined.Search, contentDescription = "Search", tint = Color(0xFF00643C), modifier = Modifier.size(20.dp))
                    Spacer(modifier = Modifier.width(8.dp))
                    
                    androidx.compose.animation.AnimatedContent(
                        targetState = searchHints[currentHintIndex],
                        transitionSpec = {
                            androidx.compose.animation.slideInVertically { height -> height } + androidx.compose.animation.fadeIn() togetherWith
                            androidx.compose.animation.slideOutVertically { height -> -height } + androidx.compose.animation.fadeOut()
                        },
                        modifier = Modifier.weight(1f),
                        label = "searchHintAnimation"
                    ) { targetHint ->
                        Text(
                            text = targetHint,
                            color = Color.Gray,
                            fontSize = 13.sp,
                            maxLines = 1,
                            overflow = TextOverflow.Ellipsis
                        )
                    }
                    
                    Icon(
                        Icons.Outlined.CameraAlt, 
                        contentDescription = "Image Search", 
                        tint = Color(0xFF00643C), 
                        modifier = Modifier.size(20.dp).clickable { /* Lens */ }
                    )
                    Spacer(modifier = Modifier.width(12.dp))
                    Icon(
                        Icons.Outlined.Mic, 
                        contentDescription = "Voice Search", 
                        tint = Color(0xFF00643C), 
                        modifier = Modifier.size(20.dp).clickable { /* Voice */ }
                    )
                }
                Spacer(modifier = Modifier.height(4.dp))
            }
        }
    ) { paddingValues ->
        LazyColumn(
            contentPadding = PaddingValues(top = paddingValues.calculateTopPadding(), bottom = 24.dp),
            modifier = Modifier.fillMaxSize().background(MaterialTheme.colorScheme.background)
        ) {
            item {
                // Banner Slider
                var bannerIndex by remember { androidx.compose.runtime.mutableIntStateOf(0) }
                LaunchedEffect(Unit) {
                    while (true) {
                        kotlinx.coroutines.delay(3000)
                        bannerIndex = (bannerIndex + 1) % 3
                    }
                }
                Box(
                    modifier = Modifier.fillMaxWidth().height(140.dp).padding(16.dp).clip(RoundedCornerShape(12.dp)).background(Color.LightGray)
                ) {
                    androidx.compose.animation.AnimatedContent(
                        targetState = bannerIndex,
                        transitionSpec = {
                            androidx.compose.animation.slideInHorizontally { width -> width } + androidx.compose.animation.fadeIn() togetherWith
                            androidx.compose.animation.slideOutHorizontally { width -> -width } + androidx.compose.animation.fadeOut()
                        },
                        label = "bannerAnimation"
                    ) { index ->
                        val colors = listOf(Color(0xFFE8F5E9), Color(0xFFE3F2FD), Color(0xFFFFF3E0))
                        Box(modifier = Modifier.fillMaxSize().background(colors[index]), contentAlignment = Alignment.Center) {
                            Text("Circle Deals Campaign ${index + 1}", fontWeight = FontWeight.Bold, color = Color(0xFF00643C))
                        }
                    }
                    // Indicators
                    Row(modifier = Modifier.align(Alignment.BottomCenter).padding(8.dp), horizontalArrangement = Arrangement.spacedBy(4.dp)) {
                        for (i in 0 until 3) {
                            Box(modifier = Modifier.size(if (i == bannerIndex) 8.dp else 6.dp).clip(CircleShape).background(if (i == bannerIndex) Color(0xFF00643C) else Color.Gray))
                        }
                    }
                }
            }
            
            item {
                // Categories
                val categories = listOf("Electronics", "Fashion", "Beauty", "Shoes", "Home", "Sports", "Baby")
                LazyRow(
                    contentPadding = PaddingValues(horizontal = 16.dp),
                    horizontalArrangement = Arrangement.spacedBy(16.dp),
                    modifier = Modifier.padding(bottom = 16.dp)
                ) {
                    items(categories.size) { index ->
                        Column(horizontalAlignment = Alignment.CenterHorizontally, modifier = Modifier.clickable { }) {
                            Box(modifier = Modifier.size(56.dp).clip(CircleShape).background(Color.White).border(1.dp, Color(0xFFE0E0E0), CircleShape), contentAlignment = Alignment.Center) {
                                Icon(Icons.Outlined.Star, contentDescription = categories[index], tint = Color(0xFF00643C))
                            }
                            Spacer(modifier = Modifier.height(4.dp))
                            Text(categories[index], fontSize = 11.sp, fontWeight = FontWeight.Medium, maxLines = 1, overflow = TextOverflow.Ellipsis)
                        }
                    }
                }
            }
            
            val chunkedProducts = circleDealsProducts.chunked(2)
            items(chunkedProducts) { rowProducts ->
                Row(
                    modifier = Modifier.fillMaxWidth().padding(horizontal = 12.dp, vertical = 6.dp),
                    horizontalArrangement = Arrangement.spacedBy(12.dp)
                ) {
                    for (product in rowProducts) {
                        ProductCard(product, modifier = Modifier.weight(1f).clickable { onProductClick(product.id) })
                    }
                    if (rowProducts.size == 1) {
                        Spacer(modifier = Modifier.weight(1f))
                    }
                }
            }
        }
    }
}
"""

content += circle_deals_screen

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
