import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Update NavHost composable
navhost_target = """      composable(
        Screen.CircleDeals.route,"""
navhost_replacement = """      composable(
        "circleDeals?productId={productId}",
        arguments = listOf(androidx.navigation.navArgument("productId") { nullable = true; type = androidx.navigation.NavType.StringType }),"""
content = content.replace(navhost_target, navhost_replacement)

# Update CircleDealsScreen definition in NavHost
screen_def_target = """) { CircleDealsScreen(onBack = { navController.popBackStack() }) }"""
screen_def_replacement = """) { backStackEntry -> 
        val productId = backStackEntry.arguments?.getString("productId")
        CircleDealsScreen(onBack = { navController.popBackStack() }, onProductClick = {}) 
      }"""
content = content.replace(screen_def_target, screen_def_replacement)

# Wait, `CircleDealsScreen` in NavHost was:
#      composable(
#        Screen.CircleDeals.route,
#        deepLinks = listOf(androidx.navigation.navDeepLink { uriPattern = "https://circlebazar.com/deals" })
#      ) { CircleDealsScreen(onBack = { navController.popBackStack() }) }

# Let's write a better replacement using regex
import re
navhost_regex = r"composable\(\s*Screen\.CircleDeals\.route,\s*deepLinks\s*=\s*listOf\(androidx\.navigation\.navDeepLink\s*\{\s*uriPattern\s*=\s*\"https://circlebazar\.com/deals\"\s*\}\)\s*\)\s*\{\s*CircleDealsScreen\(onBack\s*=\s*\{\s*navController\.popBackStack\(\)\s*\}\)\s*\}"

new_navhost = """composable(
        "circleDeals?productId={productId}",
        arguments = listOf(androidx.navigation.navArgument("productId") { nullable = true; type = androidx.navigation.NavType.StringType }),
        deepLinks = listOf(androidx.navigation.navDeepLink { uriPattern = "https://circlebazar.com/deals" })
      ) { backStackEntry ->
        val productId = backStackEntry.arguments?.getString("productId")
        CircleDealsScreen(onBack = { navController.popBackStack() }, onProductClick = { /* open detail */ })
      }"""
content = re.sub(navhost_regex, new_navhost, content)

# update HomeScreen signature
homescreen_target = """fun HomeScreen(onSearchClick: () -> Unit = {}, onCameraClick: () -> Unit = {}, onCircleDealsClick: () -> Unit = {}) {"""
homescreen_replacement = """fun HomeScreen(onSearchClick: () -> Unit = {}, onCameraClick: () -> Unit = {}, onCircleDealsClick: (String?) -> Unit = {}) {"""
content = content.replace(homescreen_target, homescreen_replacement)

# update HomeScreen call in NavHost
homescreen_call_target = """composable(Screen.Home.route) { HomeScreen(onSearchClick = { navController.navigate(Screen.Search.route) }, onCameraClick = { navController.navigate(Screen.CameraSearch.route) }, onCircleDealsClick = { navController.navigate(Screen.CircleDeals.route) }) }"""
homescreen_call_replacement = """composable(Screen.Home.route) { HomeScreen(onSearchClick = { navController.navigate(Screen.Search.route) }, onCameraClick = { navController.navigate(Screen.CameraSearch.route) }, onCircleDealsClick = { id -> navController.navigate("circleDeals" + (if(id != null) "?productId=$id" else "")) }) }"""
content = content.replace(homescreen_call_target, homescreen_call_replacement)

# Update Circle Deals Click in HomeScreen (the "Show More" button)
show_more_target = """Text("Show More", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Medium, maxLines = 1, overflow = TextOverflow.Ellipsis, modifier = Modifier.clickable { onCircleDealsClick() })"""
show_more_replacement = """Text("Show More", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Medium, maxLines = 1, overflow = TextOverflow.Ellipsis, modifier = Modifier.clickable { onCircleDealsClick(null) })"""
content = content.replace(show_more_target, show_more_replacement)

# Update CircleDealCard clicks in HomeScreen 
# (Currently they don't seem to have clicks, let's add them)
card_target = """CircleDealCard(product, modifier = Modifier.width(160.dp))"""
card_replacement = """CircleDealCard(product, modifier = Modifier.width(160.dp).clickable { onCircleDealsClick(product.id) })"""
content = content.replace(card_target, card_replacement)

product_card_target = """ProductCard(product, modifier = Modifier.weight(1f))"""
product_card_replacement = """ProductCard(product, modifier = Modifier.weight(1f).clickable { 
    if (product.id.hashCode() % 2 == 0) onCircleDealsClick(product.id) else {} 
})"""
content = content.replace(product_card_target, product_card_replacement)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

