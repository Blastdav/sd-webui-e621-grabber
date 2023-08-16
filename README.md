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

## Installation

1. Clone into `extensions` folder

## Usage

Within the setting area of A1111 there are several options which should be set before starting.
There are default settings in place which should get you started; however, it is recommended to go over the settings and make sure it is set up to suit your needs.

The settings are as follows:
# Things to include with every search
    This option will append the provided text to the search query. This is where you would put things like order:random or -animated etc.
# Regex of tags to remove
    This box allows for regular expressions to be used to remove certain tags. This is so that you can remove character identifying traits if you want to
# Tags to increase the weight of
    Is is a comma separated list of tags which, when seen, will have brackets put around it as well as the weight from the 'Amount of weight to add to tags' box (e.g. if "female" is in the list and 1:4 is in the "amount of weight to add to tags" box, the result would be (female:1.4) )
# Tags to add extra brackets around
    This is similar to the above option, but will just add brackets. It can be used with the above option. (e.g. If "female" is used in both boxes, the result would be ((female:1.4)) whereas just using it in this option would result in (female) )
# Amount of weight to add to tags
    This is the value to add to the tags listed in "Tags to increase the weight of". By default it is 1.4

The extension itself works as follows:
# Enable E621 Grabber
    This enables the extension
# Random prompt every time
    If this **is not ticked**, a single query will be used across all images in a batch
    If this **is ticked**, a different query will be used for each image in the batch
# Search query
    This is the query to use (along with the text from the "Things to include with every search" box). The top query will be used and injected at the top of the prompt.
    It is important to note that this works the same way as the E621 search box. An example query would be "female solo rating:safe"

    If there are no results found (currently) an error will flag up in the console and the generation will continue without adding anything to the prompt.

## Something wrong?

Open an issue on Github if there is some weird error, or use Discussions tab for general questions.

Please adhere to the Github TOS and **do not post** any NSFW imagery or tags in the issues or discussions.

## Changelog

### 16/08/2023
- Updating readme
- Updated text in the settings page
- Changed text on labels in extension

### 11/08/2023
- First release
