def process_file(filename):
    print(filename)
    with open(filename) as fh:
        content = fh.read()
    
    result = 100 / int(content)
    print(f"100 / {content} = {result}")
