# Mnemonic Generator [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?text=Get%20over%20170%20free%20design%20blocks%20based%20on%20Bootstrap%204&url=https://froala.com/design-blocks&via=froala&hashtags=bootstrap,design,templates,blocks,developers)

Mnemonic Generator is a Python library for generating mnemonic phrases. It allows for the ability to specify the word count, min word length, repeatability, and a custom word-list (JSON formatted).

## Installation

Clone the repository, and copy the needed files to your project. All that is needed is generator.py and wordlist.json

## Usage

```python
from mnemonic_generator import generateMnemonic

# returns your mnemonic
generateMnemonic(word_count, allow_repeating, wordlist, min_length)
    '''
    Parameters:
        word_count: The number of words for the mnemoinic. DEFAULT = 12
        allow_repeating: Allow words to repeat.  DEFAULT = FALSE
        wordlist: Specify file to use custom wordlist. Note - You can also just add to the given wordlist. DEFAULT = None
        min_length: The minimum length of the words in the mnemoinic. DEFAULT = 3
    Returns:
        str[]: List of the mnemoinic's composition.
    '''


```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[cc4.0](https://creativecommons.org/licenses/by/4.0/)
