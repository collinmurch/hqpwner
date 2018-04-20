# hqpwner

A python script to both parse and analyze trivia questions from the game "HQ Trivia".

*Only MacOS is currently supported.*

To use this script, a **"tokens.json"** file is required, which looks like:
```
{
    "key":"somekeysomekeysomekey",
    "cx":"someidsomeidsomeid"
}
```

Both the key and CSE ID can be found on [Google's CSE API page](https://developers.google.com/custom-search/json-api/v1/overview).

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
