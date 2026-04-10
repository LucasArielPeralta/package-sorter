# Package Sorter

## Objective
Sort packages into stacks based on volume and mass.

## Rules

- **Bulky**:
  - Volume ≥ 1,000,000 cm³ OR
  - Any dimension ≥ 150 cm
- **Heavy**:
  - Mass ≥ 20 kg

## Output

| Condition                  | Result     |
|---------------------------|------------|
| Not bulky & not heavy     | STANDARD   |
| Bulky OR heavy            | SPECIAL    |
| Bulky AND heavy           | REJECTED   |

## Usage

```python
from sorter import sort

print(sort(100, 100, 100, 10))  # SPECIAL
