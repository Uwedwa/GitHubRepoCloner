# GitHubRepoCloner

GitHubRepoCloner is a simple script to clone all repositories from a specific GitHub topic page. It scrapes the given topic URL and clones each repository found on that page.

## Features

- Scrapes GitHub topic pages for repositories.
- Clones all found repositories to your local machine.
- Simple and easy to use.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation

1. Clone the repository or download the script.

    ```bash
    git clone https://github.com/yourusername/GitHubRepoCloner.git
    cd GitHubRepoCloner
    ```

2. Install the required Python libraries.

    ```bash
    pip install requests beautifulsoup4
    ```

## Usage

1. Run the script.

    ```bash
    python GitHubRepoCloner.py
    ```

2. Enter the GitHub topic URL when prompted.

    ```plaintext
    Enter the GitHub topic URL: https://github.com/topics/zartzurt
    ```

The script will clone all repositories listed on the specified topic page.

## Example

```bash
$ python GitHubRepoCloner.py
Enter the GitHub topic URL: https://github.com/topics/zartzurt
All projects have been cloned.
