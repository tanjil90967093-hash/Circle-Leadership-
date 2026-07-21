import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# 1. Update Product data class
content = content.replace("val maxStock: Int = 100", "val maxStock: Int = 100,\n  val isCircleDeal: Boolean = false")

# 2. Update mockProducts
content = content.replace("stock = 20,\n    maxStock = 100\n  )", "stock = 20,\n    maxStock = 100,\n    isCircleDeal = index % 3 == 0\n  )")

# 3. Add ProductDetails route in NavHost
# Search for `composable(Screen.Home.route) { HomeScreen`
nav_target = """composable(Screen.Home.route) { HomeScreen(onSearchClick = { navController.navigate(Screen.Search.route) }, onCameraClick = { navController.navigate(Screen.CameraSearch.route) }) }"""
nav_replacement = """composable(Screen.Home.route) { HomeScreen(onSearchClick = { navController.navigate(Screen.Search.route) }, onCameraClick = { navController.navigate(Screen.CameraSearch.route) }, onCircleDealsClick = { id -> navController.navigate("circleDeals" + (if(id != null) "?productId=$id" else "")) }, onProductClick = { id -> navController.navigate("productDetails/$id") }) }
      composable("productDetails/{productId}", arguments = listOf(androidx.navigation.navArgument("productId") { type = androidx.navigation.NavType.IntType })) { backStackEntry ->
        val productId = backStackEntry.arguments?.getInt("productId") ?: 0
        ProductDetailsScreen(productId = productId, onBack = { navController.popBackStack() })
      }
      composable("circleDeals?productId={productId}", arguments = listOf(androidx.navigation.navArgument("productId") { nullable = true; type = androidx.navigation.NavType.StringType })) { backStackEntry ->
        val productId = backStackEntry.arguments?.getString("productId")
        CircleDealsScreen(highlightProductId = productId, onBack = { navController.popBackStack() }, onProductClick = { id -> navController.navigate("productDetails/$id") })
      }"""
content = content.replace(nav_target, nav_replacement)

# Update HomeScreen signature
content = content.replace("fun HomeScreen(onSearchClick: () -> Unit = {}, onCameraClick: () -> Unit = {})", "fun HomeScreen(onSearchClick: () -> Unit = {}, onCameraClick: () -> Unit = {}, onCircleDealsClick: (String?) -> Unit = {}, onProductClick: (Int) -> Unit = {})")

# Update ProductCard to support clicks and badge
content = re.sub(
    r"@Composable\nfun ProductCard\(product: Product, modifier: Modifier = Modifier\) \{\n  Card\(",
    r"@Composable\nfun ProductCard(product: Product, modifier: Modifier = Modifier) {\n  Card(",
    content
)

# Wait, ProductCard is called in HomeScreen. I need to make it clickable if it is not already.
# I will use a different script to modify HomeScreen specifically.

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
