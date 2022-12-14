# advent-of-code-2022

Requirements:
- Python 3.11.05b

Dev requirements:
- poetry
- pytest
- mypy (optional, note that only dev trunk has typing.Self)


Design goals:
- No dependencies
- Don't require any `__init__.py` files
- Prefer iterators & their `typing` annotations
- Don't consume iterators until strategically important
- Look for reasons to use `yield from`
- Look for reasons to use `match`
- Find walrus operations that I love and that I hate
- Produce all final results as a dataclass of crunched result
- Result dataclass has a classmethod trigger to run main task
- Each file runnable directly with printed result dataclass
- Embed a pytest function inside each task file

## Setup

Ought to be dockerized, but until then:

```shell
git clone https://github.com/tiliv/advent-of-code-2022.git
cd advent-of-code-2022

brew install pyenv poetry
pyenv install 3.11.0b5
poetry env use 3.11.0b5

poetry install
poetry shell
(.venv) pytest  # run everything and verify
(.venv) cd '01 Calorie Counting'
(.venv) pytest  # run a single day
(.venv) pytest A__largest_group.py  # run a single task
(.venv) python A__ruthless.py  # run minimalist version
```
