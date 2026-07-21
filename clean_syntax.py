import re

with open('app/src/main/java/com/example/MainActivity.kt', 'r') as f:
    content = f.read()

# Fix the extra braces after NavigationBar
nav_bar_braces_target = """        }
      }
    }
  ) { innerPadding ->"""

nav_bar_braces_replacement = """        }
      }
  ) { innerPadding ->"""
content = content.replace(nav_bar_braces_target, nav_bar_braces_replacement)


# Fix the leftover from NavHost
leftover_target = """      composable(Screen.CameraSearch.route) { CameraSearchScreen(onBack = { navController.popBackStack() }) }
        val productId = backStackEntry.arguments?.getString("productId")
      }
    }
  }
}"""

leftover_replacement = """      composable(Screen.CameraSearch.route) { CameraSearchScreen(onBack = { navController.popBackStack() }) }
    }
  }
}"""
content = content.replace(leftover_target, leftover_replacement)

with open('app/src/main/java/com/example/MainActivity.kt', 'w') as f:
    f.write(content)

