import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Remove CircleDeals Screen object
content = re.sub(r'  object CircleDeals : Screen\("circle_deals", "Circle Deals", Icons\.Outlined\.LocalOffer, Icons\.Filled\.LocalOffer\)\n', '', content)

# Remove NavHost route
content = re.sub(r'        CircleDealsScreen\(onBack = \{ navController\.popBackStack\(\) \}, onProductClick = \{\}\) \n', '', content)
content = re.sub(r'      composable\(\n        "circleDeals\?productId=\{productId\}",\n        arguments = listOf\(androidx\.navigation\.navArgument\("productId"\) \{ nullable = true; type = androidx\.navigation\.NavType\.StringType \}\),\n        deepLinks = listOf\(androidx\.navigation\.navDeepLink \{ uriPattern = "https://circlebazar\.com/deals" \}\)\n      \) \{ backStackEntry -> \n', '', content)


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

# Also remove circleDealsList definition
circle_deals_list_def = r"""  var circleDealsList by remember \{ 
      val doubled = mockProducts \+ mockProducts
      mutableStateOf\(doubled\.shuffled\(\)\.take\(20\)\)
  \}
  
  LaunchedEffect\(Unit\) \{
      while \(true\) \{
          kotlinx\.coroutines\.delay\(1000\) // Sell a product every second
          if \(circleDealsList\.isNotEmpty\(\)\) \{
              val randomIndex = circleDealsList\.indices\.random\(\)
              val product = circleDealsList\[randomIndex\]
              if \(product\.stock > 0\) \{
                  val updatedProduct = product\.copy\(
                      stock = product\.stock - 1,
                      soldCount = product\.soldCount \+ 1
                  \)
                  val newList = circleDealsList\.toMutableList\(\)
                  newList\[randomIndex\] = updatedProduct
                  circleDealsList = newList
              \}
          \}
      \}
  \}
  """
content = re.sub(circle_deals_list_def, "", content)

# Remove CircleDealCard function
content = re.sub(r'@Composable\nfun CircleDealCard\(.*?\n\}\n', '', content, flags=re.DOTALL)

# Remove CircleDealsScreen function
content = re.sub(r'@OptIn\(ExperimentalMaterial3Api::class\)\n@Composable\nfun CircleDealsScreen\(.*?\n\}\n', '', content, flags=re.DOTALL)


with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
