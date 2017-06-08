# Loki Token #

For protecting authentication tokens on the streams.

## Usage ##

- Copy-past the content of `loki_token.sh` to `.bashrc` or `.zshrc` or what shell init file you use.
- To lock a new token run `lock_token` command:
    - Enter you Access Token (the input is not displayed)
    - Enter a password to protect the token with
    - Copy-past the output (in a form of `export ACCESS_TOKEN='<base64-garbage>'`) to your `.*rc` file.
- Then to unlock a token invoke `unlock_token`:
    - Enter the password you protected the token with
    - `$ACCESS_TOKEN` now contains the decrypted token. Don't show it to anyone.
- After restarting the shell you have to unlock the token again.
