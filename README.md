# Ask Ernie

Ask Ernie is an application that fills out masked queries using [distillbert](https://huggingface.co/transformers/model_doc/distilbert.html).

If you ask Ernie:

    "Hello, This is Farmer Ernie. You might wonder why a city kid like me is doing out here in the [MASK]?"

You'll receive a range of responses like:

    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the woods?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the desert?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the rain?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the city?
    hello, this is farmer ernie. you might wonder why a city kid like me is doing out here in the dark?

Where Ernie has predicted the word that replaces the `[MASK]` symbol.

## Running ernie

### Create a new virtual env and install dependencies

```shell
python3 -m venv venv
source venv/bin/activate
pip install -e .[dev]
```

### Running Ernie locally

``` shell
FLASK_ENV=development FLASK_APP=ernie:app flask run
```

