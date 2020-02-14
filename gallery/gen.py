#!/usr/bin/env python3

data = \
  [ ("Eternity", "Photography")
  , ("Herding", "Photography")
  , ("Block", "Photography")
  , ("Spinning Coaster", "Photography")
  , ("One Way", "Photography")
  , ("Home", "Photography")
  , ("Lab", "Photography")
  , ("Stop", "Photography")
  , ("Hope", "Photography")
  , ("Wind", "Mixed media mask")
  , ("Cat", "Mixed media mask")
  ]

def item(title, medium):
    filename = title.lower().replace(" ", "_")
    return f"""<li>
  <a href="gallery/{filename}.jpg">
    <img src="gallery/{filename}_thumbnail.jpg"
         alt="{title}"/></a>
  <h4>{title}</h4>
  <p><i>{medium}.</i></p>
</li>"""

print(*(item(*entry) for entry in data), sep="\n\n")
