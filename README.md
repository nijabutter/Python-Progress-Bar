# Python Progress Bar

`█████████████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░ 55%`

### Usage

`ProgressBar(value=0, maximum=100, length=25, empty='░', fill='█')`

Use the `.set()` method to ensure the value does not exceed the maximum, otherwise set `.value`.

`.get()` does not add a `\n` so you can use `\b`

