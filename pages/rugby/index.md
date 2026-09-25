---
#
# Use the widgets beneath and the content will be
# inserted automagically in the webpage. To make
# this work, you have to use › layout: frontpage
#
layout: frontpage
header:
  pattern_class: pattern-rugby
widget1:
  title: "Current Predictions"
  url: '/pages/rugby/Current_Projections'
  #image: widget-1-302x182.jpg
  text: 'All the ongoing competitions'
widget2:
  title: "Player and Club Rankings"
  url: '/pages/rugby/player_rankings'
  text: 'Ranks for all clubs, and all players'
widget3:
  title: "Model Accuracies"
  url: '/pages/rugby/accuracy_page'
  #image: widget-github-303x182.jpg
  text: 'Deep dive into the rugby models'
#
# Use the call for action to show a button on the frontpage
#
# To make internal links, just use a permalink like this
# url: /getting-started/
#
# To style the button in different colors, use no value
# to use the main color or success, alert or secondary.
# To change colors see sass/_01_settings_colors.scss
#
callforaction:
  url: https://linktr.ee/rugbyclubranks
  text: Check out the project across the web ›
  style: alert
#
# This is a nasty hack to make the navigation highlight
# this page as active in the topbar navigation
#
homepage: false
categories: rugby
---

