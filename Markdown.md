# This is a test file for the Markdown format

### List 1
- item 1
- item 2
- item 3

### Code

```
row_1 = ['Facebook', 0.0, 'USD', 2974676, 3.5]
row_2 = ['Instagram', 0.0, 'USD', 2161558, 4.5]
row_3 = ['Clash of Clans', 0.0, 'USD', 2130805, 4.5]
row_4 = ['Temple Run', 0.0, 'USD', 1724546, 4.5]
row_5 = ['Pandora - Music & Radio', 0.0, 'USD', 1126879, 4.0]

data_set = [row_1, row_2, row_3, row_4, row_5]
print(data_set)

def open_file(file_name):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)
    return data

apps_data = open_file('AppleStore.csv')
print(apps_data[0:5])
```

### Table

| Header 1 | Header 2 |
| ---: | :---: |
| item 1 | item 2 |
| item 3 | item 4|
