
Symbol | Description | Example | Output
--------|-------------|-------|--------
\# | Headers (# 1 lvl, ## 2 lvl, ### 3 lvl and etc.) | # Some text | At end of the table 
\* or \_ | Italics | \*Some text* or \_Some text_ | *Some text*
** or \__ | Bold | \*\*Some text** or \_\_Some text__ | **Some text**
*** or \___ | Italics & bold | \*\*\*Text*** or \_\_\_text___ | ***Some text***
~~ | Cross out | \~~Some ext~~ | ~~Some text~~
\``` | Code in text | Some text \```code\``` text | Some text ```code``` text
\``` | Code on several lines | \```Code``` | At end of the table
\[]() | Link to sourse | My \[Github](https://github.com/Alekselion) | My [Github](https://github.com/Alekselion)
\!\[]() | Link to image | \!\[Picture](https://i.pinimg.com/originals/b6/4d/ee/b64dee73545128824e6c31ddb946e03e.gif) | ![Picture](https://i.pinimg.com/originals/b6/4d/ee/b64dee73545128824e6c31ddb946e03e.gif)
\* or \- | Bulleted list | \* item or \- item | At end of the table
1\. | Numbered list | 1\. item | At end of the table
\- [ ] and - [x] | Execution list | \- [x] Done | At end of the table
\> | Quote (> 1 lvl, >> 2 lvl, >>> 3 lvl and etc.) | > quote | At end of the table
--- | Line | --- | At end of the table

Table

header1 | header2 | header3  
\----------|----------|----------  
col 1, row 1 | col 2, row 1 | col 3, row 1  
col 1, row 2 | col 2, row 2 | col 3, row 2  
col 1, row 3 | col 2, row 3 | col 3, row 3

Output

header1 | header2 | header3
----------|----------|----------
col 1, row 1 | col 2, row 1 | col 3, row 1
col 1, row 2 | col 2, row 2 | col 3, row 2
col 1, row 3 | col 2, row 3 | col 3, row 3

# Header 1
## Header 2
### Header 3

# Code on several lines
```python
def hello(name:str):
    return f"Hello, {name}"


if __name__ == "__main__":
    print(hello("Alekselion"))
```

# Bulleted list
- step 1
- step 2
  - step 2.1
  - step 2.2
- step 3

# Numbered list
1. step 1
2. step 2
   1. step 2.1
   2. step 2.2
3. step 3

# Execution list
- [x] Done
- [x] Done
- [ ] Not done
- [ ] Not done
- [ ] Not done

# Quote
> quote 1
>> quote 2
>>> quote 3

# Line
---

# Bonus
- [Shields](https://shields.io/)
- [Emoji](https://www.webfx.com/tools/emoji-cheat-sheet/) :smile: :blush: :relaxed: :exclamation: :question: :x: :no_entry:
