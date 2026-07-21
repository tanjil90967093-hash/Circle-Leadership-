import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

target = """        Row(
           modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
           horizontalArrangement = Arrangement.SpaceBetween,
           verticalAlignment = Alignment.CenterVertically
        ) {
           Row(verticalAlignment = Alignment.CenterVertically) {"""

replacement = """        Row(
           modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
           horizontalArrangement = Arrangement.SpaceBetween,
           verticalAlignment = Alignment.CenterVertically
        ) {
           Row(verticalAlignment = Alignment.CenterVertically, modifier = Modifier.weight(1f)) {"""

content = content.replace(target, replacement)

target2 = """                 Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 6.dp, vertical = 3.dp)) {
                     Text("12", color = timerText, fontSize = 12.sp, fontWeight = FontWeight.ExtraBold)
                 }             }
            }
            Text("Show More", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Medium, modifier = Modifier.clickable { onCircleDealsClick() })
         }"""

replacement2 = """                 Box(modifier = Modifier.clip(RoundedCornerShape(6.dp)).background(timerBg).padding(horizontal = 6.dp, vertical = 3.dp)) {
                     Text("12", color = timerText, fontSize = 12.sp, fontWeight = FontWeight.ExtraBold)
                 }
             }
           }
           Spacer(modifier = Modifier.width(8.dp))
           Text("Show More", color = MaterialTheme.colorScheme.primary, fontSize = 12.sp, fontWeight = FontWeight.Medium, maxLines = 1, overflow = TextOverflow.Ellipsis, modifier = Modifier.clickable { onCircleDealsClick() })
        }"""

content = content.replace(target2, replacement2)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

