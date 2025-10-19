import markdown as md

def convertToHtml(source, dest):
  try:
    with open(source, 'r') as f:
      md_text = f.read()
    html_text = md.markdown(md_text)
    with open(dest, 'w') as f:
      f.write(html_text)
  except:
    print("some Error")
    
convertToHtml('sample.md', 'md.html')    