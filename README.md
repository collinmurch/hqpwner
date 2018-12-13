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

Read more at: [medium article](https://medium.com/@collinmurch/a-modern-approach-to-cracking-trivia-3c24f357fd5e),
or my follow-up: [other medium article](https://medium.com/@collinmurch/a-new-approach-to-my-hq-trivia-bot-d9a8d1b52d9f)

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
