from lxml import etree

text = "<div>sfsdf</div>"

html = etree.HTML(text)
print(etree.tostring(html))

print([i for i in html.xpath("//div/text()")])
