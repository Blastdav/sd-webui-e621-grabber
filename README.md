# sd-webui-e621-grabber

## Features

- Uses the provided search tag to grab tags from posts containing that tag
- Can grab a single random image's tags and apply it across the range of images in a batch, or use a random image each time
- The resulting list of tags can be altered in the following ways:
    1. Removal of tags matching a regex expression
    2. Increase weight of tags matching those in a list
    3. Further increase weight on a second list
    4. The specific overall weight addition can be altered
- Tags can be applied to every request (It's advisable to keep at least "order:Random" otherwise... Well I feel like that's obvious?)

## Requirements

- Python 3.10+
- sd-webui v1.3.2 (may work with the previous versions, but untested)

## Development

1. Clone into `extensions` folder
2. `cp .env.example .env` for setting `PYTHONPATH`. It is required for IDE autocompletions to work (tested with vscode, if you use PyCharm your mileage may vary). If you using unix-like OS, replace semicolon with a colon

## Something wrong?

Open an issue on Github if there is some weird error, or use Discussions tab for general questions.

Please adhere to the Github TOS and **do not post** any NSFW imagery or tags in the issues or discussions.

## Changelog

### 11/08/2023

- First release
