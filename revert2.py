import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Revert homescreen signature
homescreen_sig_replacement = """fun HomeScreen(onSearchClick: () -> Unit = {}, onCameraClick: () -> Unit = {}, onCircleDealsClick: (String?) -> Unit = {}) {"""
homescreen_sig_target = """fun HomeScreen(onSearchClick: () -> Unit = {}, onCameraClick: () -> Unit = {}) {"""
content = content.replace(homescreen_sig_replacement, homescreen_sig_target)

# Revert circle deals click handler in NavHost
navhost_home_replacement = """composable(Screen.Home.route) { HomeScreen(onSearchClick = { navController.navigate(Screen.Search.route) }, onCameraClick = { navController.navigate(Screen.CameraSearch.route) }, onCircleDealsClick = { id -> navController.navigate("circleDeals" + (if(id != null) "?productId=$id" else "")) }) }"""
navhost_home_target = """composable(Screen.Home.route) { HomeScreen(onSearchClick = { navController.navigate(Screen.Search.route) }, onCameraClick = { navController.navigate(Screen.CameraSearch.route) }) }"""
content = content.replace(navhost_home_replacement, navhost_home_target)


# Remove the whole Circle Deals section in HomeScreen
circle_deals_section = r"""      item \{
        Spacer\(modifier = Modifier\.height\(24\.dp\)\)
        Row\(modifier = Modifier\.fillMaxWidth\(\)\.padding\(horizontal = 16\.dp\), horizontalArrangement = Arrangement\.SpaceBetween, verticalAlignment = Alignment\.CenterVertically\) \{
           Row\(verticalAlignment = Alignment\.CenterVertically\) \{
             Text\("Circle Deals", fontSize = 18\.sp, fontWeight = FontWeight\.Bold, color = MaterialTheme\.colorScheme\.primary\)
             Spacer\(modifier = Modifier\.width\(8\.dp\)\)
             val timerBg = Color\(0xFFFCE4EC\)
             val timerText = Color\(0xFFD81B60\)
             Row\(verticalAlignment = Alignment\.CenterVertically, horizontalArrangement = Arrangement\.spacedBy\(4\.dp\)\) \{
                 Box\(modifier = Modifier\.clip\(RoundedCornerShape\(6\.dp\)\)\.background\(timerBg\)\.padding\(horizontal = 6\.dp, vertical = 3\.dp\)\) \{
                     Text\("14", color = timerText, fontSize = 12\.sp, fontWeight = FontWeight\.ExtraBold\)
                 \}
                 Text\(":", color = timerBg, fontSize = 14\.sp, fontWeight = FontWeight\.Bold\)
                 Box\(modifier = Modifier\.clip\(RoundedCornerShape\(6\.dp\)\)\.background\(timerBg\)\.padding\(horizontal = 6\.dp, vertical = 3\.dp\)\) \{
                     Text\("35", color = timerText, fontSize = 12\.sp, fontWeight = FontWeight\.ExtraBold\)
                 \}
                 Text\(":", color = timerBg, fontSize = 14\.sp, fontWeight = FontWeight\.Bold\)
                 Box\(modifier = Modifier\.clip\(RoundedCornerShape\(6\.dp\)\)\.background\(timerBg\)\.padding\(horizontal = 6\.dp, vertical = 3\.dp\)\) \{
                     Text\("12", color = timerText, fontSize = 12\.sp, fontWeight = FontWeight\.ExtraBold\)
                 \}
             \}
           \}
           Text\("Show More", color = MaterialTheme\.colorScheme\.primary, fontSize = 12\.sp, fontWeight = FontWeight\.Medium, modifier = Modifier\.clickable \{ onCircleDealsClick\(null\) \}\)
        \}
        Spacer\(modifier = Modifier\.height\(12\.dp\)\)
      \}
      
      item \{
        androidx\.compose\.foundation\.lazy\.grid\.LazyHorizontalGrid\(
            rows = androidx\.compose\.foundation\.lazy\.grid\.GridCells\.Fixed\(2\),
            contentPadding = PaddingValues\(horizontal = 16\.dp\),
            horizontalArrangement = Arrangement\.spacedBy\(12\.dp\),
            verticalArrangement = Arrangement\.spacedBy\(12\.dp\),
            modifier = Modifier\.fillMaxWidth\(\)\.height\(480\.dp\) // Approximate height for 2 rows of 240dp cards \+ spacing
        \) \{
            items\(circleDealsList\.size\) \{ index ->
                CircleDealCard\(circleDealsList\[index\], modifier = Modifier\.width\(130\.dp\)\.clickable \{ onCircleDealsClick\(circleDealsList\[index\]\.id\.toString\(\)\) \}\)
            \}
        \}
      \}
      """
content = re.sub(circle_deals_section, "", content)

# Remove CircleDeals Badge
badge_regex = r"@Composable\nfun CircleDealsBadge\(\) \{.*?\n\}"
content = re.sub(badge_regex, "", content, flags=re.DOTALL)

# Revert ProductCard
content = re.sub(r"        // Show badge for half the products to simulate some being Circle Deals.*?\n        \}\n", "", content, flags=re.DOTALL)
content = content.replace(".clickable { \n    if (product.id.hashCode() % 2 == 0) onCircleDealsClick(product.id.toString()) else {} \n}", "")

# Remove CircleDealsScreen from NavHost
nav_route_regex = r"""      composable\(
        "circleDeals\?productId=\{productId\}",
        arguments = listOf\(androidx\.navigation\.navArgument\("productId"\) \{ nullable = true; type = androidx\.navigation\.NavType\.StringType \}\),
        deepLinks = listOf\(androidx\.navigation\.navDeepLink \{ uriPattern = "https://circlebazar\.com/deals" \}\)
      \) \{ backStackEntry ->
        val productId = backStackEntry\.arguments\?\.getString\("productId"\)
        CircleDealsScreen\(onBack = \{ navController\.popBackStack\(\) \}, onProductClick = \{ /\* open detail \*/ \}\)
      \}"""
content = re.sub(nav_route_regex, "", content)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
