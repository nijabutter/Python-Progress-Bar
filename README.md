# Python Progress Bar

### Examples
- Width: 20
- Maximum Value: 100
- Set Value: 60

`████████████░░░░░░░░ 60%`

- Width: 60
- Maximum Value 1560
- Set Value 873

`█████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░ 55%`

### Usage
`ProgressBar(maximum value, value=, width=, empty=, full=)`
Defaults:
- Value: 0
- Width: 100
- Empty: `░ U+2591 LIGHT SHADE`
- Full: `█ U+2588 FULL BLOCK`
```python
from progressbar import *
bar = ProgressBar(120, width=20) # Initialise with a maximum value of 120 and a width of 20
bar.Display(47) # Display the bar with a value of 47
```
`███████░░░░░░░░░░░░░ 39%`

### Methods
- `Show()` : Display with the current value
- `Display(value)` : Update value and display
- `SetMaximum(maximum)` : Set the maximum value to a new number
- `Add(value)` : Add onto the current value
- `Set(value)` : Set the new value
- `getPercentage()`: Return the percentage complete in decimal


