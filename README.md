# Numword Georgia

* Converts numbers to words in Georgian
* Supports number up to millions

```text
Number 5909 is 'ხუთი ათას ცხრაას ცხრაი'
Number 9999 is 'ცხრაი ათას ცხრაას ოთხმოცდაცხრამეტი'
Number 7000 is 'შვიდი ათასი'
Number 7707 is 'შვიდი ათას შვიდას შვიდი'
Number 91 is 'ოთხმოცდათერთმეტი'
```

## Examples

```python
from numword_georgia import translate

translate(0)  # Returns "ნული"
translate(16) # Returns "თექვსმეტი"
```
