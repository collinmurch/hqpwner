# hqpwner

A python script to both parse and analyze out trivia questions from the game "HQ Trivia".

*Only MacOS is currently supported.*

To use this script, a **"tokens.json"** file is required, which looks like:
```
{
    "key":"somekeysomekeysomekey",
    "cx":"someidsomeidsomeid"
}
```

---
*Setup example:*

```
>>> brew install tesseract

>>> git clone https://github.com/collinmurch/hqpwner

>>> cd ./hqpwner

>>> echo '{"key":"somekey","cx":"someid"}' > tokens.json

>>> python3 hqpwner.py
```
---
![botimage](https://i.imgur.com/Ty0RZH4.png)