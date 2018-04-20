# hqpwner

![hqimage](https://i.imgur.com/r6a6Ss9.png) ![botimage](https://imgur.com/a/L2uGliP)

A simple python script built to interact with Philips Hue lights.


To use this script, a **"tokens.json"** file is required, which looks like:
```
{
    "key":"somekeysomekeysomekey",
    "cx":"someidsomeidsomeid"
}
```

*Only MacOS is currently supported.*

---
*Setup example:*

```
>>> brew install tesseract

>>> git clone https://github.com/collinmurch/hqpwner

>>> cd ./hqpwner

>>> echo '{"key":"somekey","cx":"someid"}' > tokens.json

>>> python3 hqpwner.py
```
