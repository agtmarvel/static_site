import unittest
from textnode_to_htmlnode import *
from htmlnode import *
from textnode import TextNode, TextType
from extract_links import *

def test_paragraphs(self):
    md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

def test_codeblock(self):
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )

def test_quoteblock(self):
    md = """
>Kingdom Hearts isn't darkness. 
>It's light!
"""
    
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><blockquote>Kingdom Hearts isn't darkness.\nIt's light!</blockquote></div>",
    )
    
def test_headingblocks(self):
    md = """
# Kingdom Hearts Maps
## Hollow Bastion
### Area 1
### Area 2
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><h1>Kingdom Hearts Maps</h1>\n<h2>Hollow Bastion</h2>\n<h3>Area 1</h3>\n<h3>Area 2</h3></div>",
    )

def test_olblocks(self):
    md = """
1. Red
2. Orange
3. Yellow
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li>Red</li><li>Orange</li><li>Yellow</li></ol></div>",
    )

def test_olblocks_with_inline(self):
    md = """
1. **Red** is bright
2. *Orange* is nice
3. `Yellow` code
"""
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ol><li><b>Red</b> is bright</li><li><i>Orange</i> is nice</li><li><code>Yellow</code> code</li></ol></div>"
    )

def test_ulblocks(self):
    md = """
- Melee
- Caster
- Half-Caster
"""    
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Melee</li><li>Caster</li><li>Half-Caster</li></ul></div>",
    )

def test_nested_ulblocks(self):
    md = """
- Melee
  * Fighter
  * Barbarian
- Caster
  * Wizard
  * Sorceror
- Half-Caster
  * Bard
  * Ranger
"""    
    node = markdown_to_html_node(md)
    html = node.to_html()
    self.assertEqual(
        html,
        "<div><ul><li>Melee<ul><li>Fighter</li><li>Barbarian</li></ul></li><li>Caster><ul><li>Wizard</li><li>Sorceror</li></ul></li><li>Half-Caster<ul><li>Bard</li><li>Ranger</li></ul></li></ul></div>",    
    )    
    
if __name__ == "__main__":
	unittest.main()
    