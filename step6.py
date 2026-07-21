import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

home_search_target = """              Row(
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

home_search_replacement = """              // Animated Placeholder for Search
              val searchHints = listOf("Search Circle Bazar", "Wireless Earbuds", "Samsung Galaxy", "Nike Shoes", "Laptop", "Bluetooth Speaker", "Women's Handbag", "Gaming Mouse")
              var currentHintIndex by remember { androidx.compose.runtime.mutableIntStateOf(0) }
              
              LaunchedEffect(Unit) {
                  while (true) {
                      kotlinx.coroutines.delay(2000)
                      currentHintIndex = (currentHintIndex + 1) % searchHints.size
                  }
              }

              Row(
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
                      modifier = Modifier.padding(horizontal = 8.dp).size(20.dp).clickable(
                         interactionSource = remember { androidx.compose.foundation.interaction.MutableInteractionSource() },
                         indication = null
                      ) { 
                         onCameraClick()
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

content = content.replace(home_search_target, home_search_replacement)
content = content.replace("import androidx.compose.animation.togetherWith\n", "")
content = content.replace("import androidx.compose.animation.togetherWith", "")
# add it once at top
content = content.replace("import androidx.compose.animation.core.animateFloatAsState", "import androidx.compose.animation.core.animateFloatAsState\nimport androidx.compose.animation.togetherWith")

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)
