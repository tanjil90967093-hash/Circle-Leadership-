import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

nav_bar_target = """    bottomBar = {
      NavigationBar(
        modifier = Modifier.offset { androidx.compose.ui.unit.IntOffset(x = 0, y = bottomBarOffsetHeightPx.floatValue.toInt()) },
        containerColor = MaterialTheme.colorScheme.surface,
        tonalElevation = 8.dp
      ) {"""

nav_bar_replacement = """    bottomBar = {
      Box(
        modifier = Modifier
          .fillMaxWidth()
          .offset { androidx.compose.ui.unit.IntOffset(x = 0, y = bottomBarOffsetHeightPx.floatValue.toInt()) }
          .padding(start = 16.dp, end = 16.dp, bottom = 16.dp)
      ) {
        NavigationBar(
          modifier = Modifier
            .fillMaxWidth()
            .shadow(16.dp, RoundedCornerShape(24.dp))
            .clip(RoundedCornerShape(24.dp)),
          containerColor = Color.White,
          tonalElevation = 0.dp,
          windowInsets = WindowInsets(0, 0, 0, 0)
        ) {"""

content = content.replace(nav_bar_replacement, nav_bar_target)


nav_items_target = """            NavigationBarItem(
              icon = {
                Icon(
                  imageVector = if (currentDestination?.hierarchy?.any { it.route == screen.route } == true) screen.selectedIcon else screen.icon,
                  contentDescription = screen.title
                )
              },
              label = { Text(screen.title, fontSize = 10.sp) },
              selected = currentDestination?.hierarchy?.any { it.route == screen.route } == true,
              onClick = {
                navController.navigate(screen.route) {
                  popUpTo(navController.graph.findStartDestination().id) {
                    saveState = true
                  }
                  launchSingleTop = true
                  restoreState = true
                }
              },
              colors = NavigationBarItemDefaults.colors(
                selectedIconColor = MaterialTheme.colorScheme.onSecondaryContainer,
                selectedTextColor = MaterialTheme.colorScheme.onSecondaryContainer,
                indicatorColor = MaterialTheme.colorScheme.secondaryContainer,
                unselectedIconColor = MaterialTheme.colorScheme.onSurfaceVariant,
                unselectedTextColor = MaterialTheme.colorScheme.onSurfaceVariant
              )
            )"""

nav_items_replacement = """            NavigationBarItem(
              icon = {
                Icon(
                  imageVector = if (currentDestination?.hierarchy?.any { it.route == screen.route } == true) screen.selectedIcon else screen.icon,
                  contentDescription = screen.title
                )
              },
              label = { Text(screen.title, fontSize = 10.sp, maxLines = 1, overflow = TextOverflow.Ellipsis) },
              selected = currentDestination?.hierarchy?.any { it.route == screen.route } == true,
              onClick = {
                navController.navigate(screen.route) {
                  popUpTo(navController.graph.findStartDestination().id) {
                    saveState = true
                  }
                  launchSingleTop = true
                  restoreState = true
                }
              },
              colors = NavigationBarItemDefaults.colors(
                selectedIconColor = Color(0xFF00643C),
                selectedTextColor = Color(0xFF00643C),
                indicatorColor = Color(0xFFE8F5E9),
                unselectedIconColor = Color.Gray,
                unselectedTextColor = Color.Gray
              )
            )"""

content = content.replace(nav_items_replacement, nav_items_target)


header_target = """           Row(
               modifier = Modifier
                   .fillMaxWidth()
                   .windowInsetsPadding(androidx.compose.foundation.layout.WindowInsets.statusBars)
                   .padding(horizontal = 16.dp, vertical = 6.dp),
               horizontalArrangement = Arrangement.SpaceBetween,
               verticalAlignment = Alignment.CenterVertically
           ) {
               // Logo and Title (Left aligned)
               Row(
                   verticalAlignment = Alignment.CenterVertically
               ) {
                   Image(
                       painter = androidx.compose.ui.res.painterResource(id = R.drawable.circle_bazar_icon_1784463007760),
                       contentDescription = "Logo",
                       modifier = Modifier.size(28.dp).clip(CircleShape),
                       contentScale = ContentScale.Crop
                   )
                   Spacer(modifier = Modifier.width(10.dp))
                   Text(
                       "Circle Bazar", 
                       style = MaterialTheme.typography.titleLarge.copy(
                           fontWeight = FontWeight.ExtraBold,
                           fontStyle = androidx.compose.ui.text.font.FontStyle.Italic,
                           fontFamily = FontFamily.SansSerif,
                           fontSize = 18.sp,
                           color = Color(0xFF00643C)
                       )
                   )
               }
               
               // Icons (Right aligned, better styling)
               Row(
                   horizontalArrangement = Arrangement.spacedBy(16.dp),
                   verticalAlignment = Alignment.CenterVertically
               ) {
                   Icon(painter = androidx.compose.ui.res.painterResource(R.drawable.ic_custom_search), contentDescription = "Search", tint = Color(0xFF333333), modifier = Modifier.size(20.dp).clickable { onSearchClick() })
                   Icon(painter = androidx.compose.ui.res.painterResource(R.drawable.ic_custom_notification), contentDescription = "Notifications", tint = Color(0xFF333333), modifier = Modifier.size(20.dp).clickable { })
               }
           }"""

header_replacement = """           Row(
               modifier = Modifier
                   .fillMaxWidth()
                   .windowInsetsPadding(androidx.compose.foundation.layout.WindowInsets.statusBars)
                   .padding(horizontal = 16.dp, vertical = 12.dp),
               horizontalArrangement = Arrangement.SpaceBetween,
               verticalAlignment = Alignment.CenterVertically
           ) {
               // Logo and Title (Left aligned)
               Row(
                   verticalAlignment = Alignment.CenterVertically,
                   modifier = Modifier.weight(1f)
               ) {
                   Image(
                       painter = androidx.compose.ui.res.painterResource(id = R.drawable.circle_bazar_icon_1784463007760),
                       contentDescription = "Logo",
                       modifier = Modifier.size(32.dp).clip(CircleShape),
                       contentScale = ContentScale.Crop
                   )
                   Spacer(modifier = Modifier.width(12.dp))
                   Text(
                       "Circle Bazar", 
                       style = MaterialTheme.typography.titleLarge.copy(
                           fontWeight = FontWeight.ExtraBold,
                           fontFamily = FontFamily.Serif,
                           letterSpacing = 0.5.sp,
                           fontSize = 20.sp,
                           color = Color(0xFF00643C)
                       ),
                       maxLines = 1,
                       overflow = TextOverflow.Ellipsis
                   )
               }
               
               Spacer(modifier = Modifier.width(8.dp))
               
               // Icons (Right aligned, premium styling)
               Row(
                   horizontalArrangement = Arrangement.spacedBy(12.dp),
                   verticalAlignment = Alignment.CenterVertically
               ) {
                   Box(
                       modifier = Modifier
                           .size(36.dp)
                           .clip(CircleShape)
                           .background(Color(0xFFF0F5F2))
                           .clickable { onSearchClick() },
                       contentAlignment = Alignment.Center
                   ) {
                       Icon(
                           Icons.Outlined.Search,
                           contentDescription = "Search",
                           tint = Color(0xFF00643C),
                           modifier = Modifier.size(18.dp)
                       )
                   }
                   Box(
                       modifier = Modifier
                           .size(36.dp)
                           .clip(CircleShape)
                           .background(Color(0xFFF0F5F2))
                           .clickable { },
                       contentAlignment = Alignment.Center
                   ) {
                       Icon(
                           Icons.Outlined.Notifications,
                           contentDescription = "Notifications",
                           tint = Color(0xFF00643C),
                           modifier = Modifier.size(18.dp)
                       )
                       // Notification Badge
                       Box(
                           modifier = Modifier
                               .align(Alignment.TopEnd)
                               .padding(top = 8.dp, end = 8.dp)
                               .size(6.dp)
                               .clip(CircleShape)
                               .background(Color.Red)
                       )
                   }
               }
           }"""

content = content.replace(header_replacement, header_target)

search_bar_target = """              Row(
                  modifier = Modifier
                      .fillMaxWidth()
                      .height(46.dp)
                      .shadow(8.dp, RoundedCornerShape(23.dp))
                      .background(Color.White, RoundedCornerShape(23.dp))
                      .clickable { onSearchClick() }
                      .padding(horizontal = 16.dp),
                  verticalAlignment = Alignment.CenterVertically
              ) {
                  Icon(Icons.Outlined.Search, contentDescription = "Search", tint = Color.Gray)
                  Spacer(Modifier.width(8.dp))
                  Text("Search products, brands and stores", color = Color.Gray, fontSize = 14.sp, modifier = Modifier.weight(1f))
                  Icon(
                      Icons.Outlined.CameraAlt, 
                      contentDescription = "Image Search", 
                      tint = MaterialTheme.colorScheme.primary, 
                      modifier = Modifier.padding(horizontal = 8.dp).size(20.dp).clickable(
                         interactionSource = remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                         indication = null
                      ) { 
                         try { context.startActivity(chooserIntent) } catch(e: Exception) {} 
                      }
                  )
                  Icon(
                      Icons.Outlined.Mic, 
                      contentDescription = "Voice Search", 
                      tint = MaterialTheme.colorScheme.primary, 
                      modifier = Modifier.padding(start = 8.dp).size(20.dp).clickable(
                         interactionSource = remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                         indication = null
                      ) { 
                         try { context.startActivity(voiceIntent) } catch(e: Exception) {} 
                      }
                  )
              }"""

search_bar_replacement = """              Row(
                  modifier = Modifier
                      .fillMaxWidth()
                      .height(46.dp)
                      .shadow(8.dp, RoundedCornerShape(23.dp))
                      .background(Color.White, RoundedCornerShape(23.dp))
                      .clickable { onSearchClick() }
                      .padding(horizontal = 16.dp),
                  verticalAlignment = Alignment.CenterVertically
              ) {
                  Icon(Icons.Outlined.Search, contentDescription = "Search", tint = Color.Gray, modifier = Modifier.size(20.dp))
                  Spacer(Modifier.width(8.dp))
                  Text(
                      "Search products, brands and stores", 
                      color = Color.Gray, 
                      fontSize = 13.sp, 
                      maxLines = 1,
                      overflow = TextOverflow.Ellipsis,
                      modifier = Modifier.weight(1f)
                  )
                  Icon(
                      Icons.Outlined.CameraAlt, 
                      contentDescription = "Image Search", 
                      tint = Color(0xFF00643C), 
                      modifier = Modifier.padding(horizontal = 8.dp).size(20.dp).clickable(
                         interactionSource = remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                         indication = null
                      ) { 
                         try { context.startActivity(chooserIntent) } catch(e: Exception) {} 
                      }
                  )
                  Icon(
                      Icons.Outlined.Mic, 
                      contentDescription = "Voice Search", 
                      tint = Color(0xFF00643C), 
                      modifier = Modifier.padding(start = 8.dp).size(20.dp).clickable(
                         interactionSource = remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                         indication = null
                      ) { 
                         try { context.startActivity(voiceIntent) } catch(e: Exception) {} 
                      }
                  )
              }"""

content = content.replace(search_bar_replacement, search_bar_target)


with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

