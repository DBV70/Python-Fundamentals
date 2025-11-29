article_title = input()
article_content = input()

comments = []
while True:
    command = input()
    if command == 'end of comments':
        break
    comments.append(command)

print(f"<h1>\n    {article_title}\n</h1>")
print(f"<article>\n    {article_content}\n</article>")
for comment in comments:
    print(f"<div>\n        {comment}\n</div>")