# pynotes

> Create daily notes/log with markdown.

## How to install

Verify if you have [python 3.x](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/) installed.

```sh
$ python -m pip install pynotes
```

<hr>

## Usage

*Show this help message and exit*

```sh
$ pynotes -h
```

*Optional arguments*

Short argument | Argument      | Description  |
:------------  | :-----------  | :----------- |
-h             | --help        | Show this help message and exit
-nf            | --new_file    | Create a note file
-al            | --add_link    | Add a new link
-at            | --add_tag     | Add a new tag
-r             | --read        | Read note file and show
-l             | --links       | Get all links and show
-t             | --tags        | Get all tags and show

## Example note file

`23-07-2018.md`

```
# Notes: 23-07-2018

> Tags: `python`, `cli`, `pip`, `html`

## Links:

- [Link 1](#url1)
- [Link 2](#url2)
- [Link 3](#url3)
```

## Versioning

To keep better organization of releases we follow the [Semantic Versioning 2.0.0](http://semver.org/) guidelines.

## Contributing

Find on our [issues](https://github.com/afonsopacifer/pynotes/issues/) the next steps of the project ;)
<br>
Want to contribute? [Follow these recommendations](https://github.com/afonsopacifer/pynotes/blob/master/CONTRIBUTING.md).

## History

See [Releases](https://github.com/afonsopacifer/pynotes/releases) for detailed changelog.

## License

[MIT License](https://github.com/afonsopacifer/pynotes/blob/master/LICENSE.md) © [Afonso Pacifer](https://afonsopacifer.github.io/)