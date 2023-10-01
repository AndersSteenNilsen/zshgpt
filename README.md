
[![PyPI - Version](https://img.shields.io/pypi/v/zshgpt.svg)](https://pypi.org/project/zshgpt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/zshgpt.svg)](https://pypi.org/project/zshgpt)
[![zshgpt](https://snapcraft.io/zshgpt/badge.svg)](https://snapcraft.io/zshgpt)
# zshgpt

-----

**Table of Contents**

- [About](#about)
- [Installation](#installation)
- [Future plans](#future-plans)
- [License](#license)

## About
![Gif of usage](<Peek 2023-07-17 17-27.gif>)

Heavily inspired by the abandoned project [https://github.com/microsoft/Codex-CLI](https://github.com/microsoft/Codex-CLI)
Made into a oh-my-zsh plugin.

In your zsh console, type a question, starting with comment sign `#`, hit `ctrl+g` and get an answer.
```bash
# Who edited README.MD last according to git history?
```
ChatGPT will then answer with e.g.:
```bash
git log -1 --format="%an" README.md
```
Hit `enter` to execute or `ctrl+c` to deny.

If asked a question that will not resolve in a command, GPT is instructed to use `#`.

```bash
# Who was Norways first prime minister?
# Norway's first prime minister was Frederik Stang, serving from 1873 to 1880.
```

## LOGO
*Made with DALL-E*

![Icon](icon.png)
## Prerequisite
* ⚠️ Valid Openai API-key
    * make sure to save under `OPENAI_API_KEY` env.
    * **`export OPENAI_API_KEY='sk-...'`**

### Nice to have
* Python
* pipx
* Oh-my-zsh
* zplug

## Installation standalone package
With zshgpt alone, you can ask questions with:
```sh
zshgpt "# Show me all my drives"
```
and it will return an answer from GPT. But the true ✨magic✨ comes when you also add the zsh plugin.
### Snap
```sh
sudo snap install zshgpt --edge
```

### pipx
```sh
pipx install zshgpt
```

# Install the plugin
The plugin consists of just a small script linking `<C-g>` to `zshgpt` and does some buffer tricks such taht you can just hit `enter` and don't have to copy paste the command.
### zsh
```zsh
curl https://raw.githubusercontent.com/AndersSteenNilsen/zshgpt/main/zshgpt.plugin.zsh -o ~ # Copy plugin
echo "source ~/zshgpt.plugin.zsh" >> ~/.zshrc # Add to zshrc
exec zsh # Reload zsh
```

### oh-my-zsh
```zsh
mkdir $ZSH_CUSTOM/plugins/zshgpt
curl https://raw.githubusercontent.com/AndersSteenNilsen/zshgpt/main/zsh_plugin/zsh_plugin.zsh -o $ZSH_CUSTOM/plugins/zshgpt/zshgpt.plugin.zsh
```
Then add zshgpt in your list of plugins in `~/.zshrc`

```
plugins(
    ...
    zshgpt
    ...
)
```

```zsh
omz reload
```

### zplug
`~/.zshrc`
```
...
zplug "AndersSteenNilsen/zshgpt"
zplug load
```

## Future plans

### Functionaliy
* Remember last couple messages so you could do something like:
```bash
# Open README.md <-- USER
# You can open the README.md file using a text editor of your choice. Here's an example using vim:

vim README.md
# But I don't have vim, can you open it in VSCode? <-- USER
code README.md
```
* Cycle through choices
* Give possibility to switch model
* Give info about how many token has been used

### CI/CD
* Pre-commit.
* Add to flatpack or similar to ease installation.
* Publish as part of git flow.
## License

`zshgpt` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
